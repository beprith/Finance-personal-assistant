import json
from pathlib import Path
from mcp.server.fastmcp import FastMCP

# Initialize MCP server
mcp = FastMCP("local-financial-mcp")

# Resolve path to test data directory
data_dir = Path("./test_data_dir")
print("Resolved data_dir:", data_dir.resolve())

# Helper: Load JSON by phone number + filename
def load_json(phone_number: str, filename: str):
    file_path = data_dir / phone_number / filename
    if file_path.exists():
        with open(file_path, "r") as file:
            return json.load(file)
    return {}

# Dummy authentication
@mcp.tool()
def authenticate_user(phone_number: str) -> str:
    phone_number = phone_number.strip()
    allowed = {p.name.strip() for p in data_dir.iterdir() if p.is_dir()}
    print(f"Input: '{phone_number}'")
    print(f"Allowed: {allowed}")
    if phone_number in allowed:
        return f"Authenticated {phone_number} successfully."
    return f"Authentication failed. Allowed numbers: {allowed}"

@mcp.tool()
def fetch_net_worth(phone_number: str) -> str:
    """Fetch user's net worth details from local data."""
    data = load_json(phone_number, "fetch_net_worth.json")
    if not data:
        return "No net worth data found."

    net_worth = data.get("netWorthResponse", {})
    total = net_worth.get("totalNetWorthValue", {}).get("units", "N/A")
    assets = net_worth.get("assetValues", [])
    liabilities = net_worth.get("liabilityValues", [])  # May be missing

    output_lines = [f"💰 Total Net Worth: ₹{total}"]

    if assets:
        output_lines.append("\n📊 Assets:")
        for asset in assets:
            attr = asset.get("netWorthAttribute", "Unknown")
            value = asset.get("value", {}).get("units", "0")
            output_lines.append(f"- {attr}: ₹{value}")

    if liabilities:
        output_lines.append("\n💸 Liabilities:")
        for liab in liabilities:
            attr = liab.get("netWorthAttribute", "Unknown")
            value = liab.get("value", {}).get("units", "0")
            output_lines.append(f"- {attr}: ₹{value}")

    return "\n".join(output_lines)

@mcp.tool()
def fetch_credit_report(phone_number: str) -> str:
    """Fetch user's credit report summary from local data."""
    data = load_json(phone_number, "fetch_credit_report.json")
    if not data:
        return "No credit report data found."

    reports = data.get("creditReports", [])
    if not reports:
        return "No credit reports available."

    report = reports[0]  # Assume single report
    score = report.get("creditReportData", {}).get("score", {}).get("bureauScore", "N/A")
    accounts = report.get("creditReportData", {}).get("creditAccount", {}).get("creditAccountDetails", [])

    output_lines = [f"🔢 Credit Score: {score}", "\n📄 Credit Accounts Summary:"]

    for acc in accounts[:5]:
        bank = acc.get("subscriberName", "Unknown")
        open_date = acc.get("openDate", "N/A")
        balance = acc.get("currentBalance", "0")
        due = acc.get("amountPastDue", "0")
        rating = acc.get("paymentRating", "N/A")
        status = acc.get("accountStatus", "N/A")

        output_lines.append(
            f"🏦 {bank} | Opened: {open_date} | Balance: ₹{balance} | Due: ₹{due} | Status: {status} | Rating: {rating}"
        )

    return "\n".join(output_lines)

@mcp.tool()
def fetch_bank_transactions(phone_number: str) -> str:
    """Fetch user's bank transaction details."""
    data = load_json(phone_number, "fetch_bank_transactions.json")
    if not data:
        return "No bank transaction data found."

    txns_data = data.get("bankTransactions", [])
    if not txns_data:
        return "No banks found in transaction data."

    output_lines = []

    for bank_entry in txns_data:
        bank_name = bank_entry.get("bank", "Unknown Bank")
        txns = bank_entry.get("txns", [])

        output_lines.append(f"\n📘 {bank_name} – Last Transactions:")

        for txn in txns[:5]:
            amount, narration, date, txn_type, mode, balance = txn

            txn_type_label = {
                1: "CREDIT", 2: "DEBIT", 3: "OPENING", 4: "INTEREST",
                5: "TDS", 6: "INSTALLMENT", 7: "CLOSING", 8: "OTHERS"
            }.get(txn_type, "UNKNOWN")

            output_lines.append(
                f"🗓️ {date} | ₹{amount} | {txn_type_label} via {mode} | {narration} | Balance: ₹{balance}"
            )

    return "\n".join(output_lines)

@mcp.tool()
def fetch_epf_details(phone_number: str) -> str:
    """Fetch user's EPF details and balances."""
    data = load_json(phone_number, "fetch_epf_details.json")
    if not data:
        return "No EPF data found."

    uan_accounts = data.get("uanAccounts", [])
    if not uan_accounts:
        return "No UAN account details available."

    output_lines = []

    for account in uan_accounts:
        raw = account.get("rawDetails", {})
        ests = raw.get("est_details", [])
        overall = raw.get("overall_pf_balance", {})

        output_lines.append("🏢 Employment History:")
        for est in ests:
            output_lines.append(
                f"- {est.get('est_name', 'Unknown')}\n"
                f"  • Member ID: {est.get('member_id', 'N/A')}\n"
                f"  • DOJ: {est.get('doj_epf')} → DOE: {est.get('doe_epf')}\n"
                f"  • PF Balance: ₹{est['pf_balance'].get('net_balance', '0')}"
            )

        pension = overall.get("pension_balance", "0")
        curr_pf = overall.get("current_pf_balance", "0")
        emp_total = overall.get("employee_share_total", {}).get("balance", "0")

        output_lines.append("\n💰 Overall EPF Summary:")
        output_lines.append(f"- Pension Balance: ₹{pension}")
        output_lines.append(f"- Current PF Balance: ₹{curr_pf}")
        output_lines.append(f"- Total Employee Share Balance: ₹{emp_total}")

    return "\n".join(output_lines)

@mcp.tool()
def fetch_mf_transactions(phone_number: str) -> str:
    """Fetch user's mutual fund transaction history."""
    data = load_json(phone_number, "fetch_mf_transactions.json")
    if not data:
        return "No mutual fund transaction data found."

    mf_data = data.get("mfTransactions", [])
    if not mf_data:
        return "No mutual fund investments available."

    output_lines = []

    for mf in mf_data:
        scheme = mf.get("schemeName", "Unknown Scheme")
        folio = mf.get("folioId", "N/A")
        txns = mf.get("txns", [])

        output_lines.append(f"\n📈 {scheme} (Folio: {folio})")

        for txn in txns[:5]:
            order_type, date, nav, units, amount = txn
            order_type_label = "BUY" if order_type == 1 else "SELL"
            output_lines.append(
                f"🗓️ {date} | {order_type_label} | ₹{amount} @ ₹{nav}/unit | Units: {units:.4f}"
            )

    return "\n".join(output_lines)

# Entry point
if __name__ == "__main__":
    mcp.run(transport="stdio")

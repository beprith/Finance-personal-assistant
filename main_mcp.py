import json
from pathlib import Path
from mcp.server.fastmcp import FastMCP

# Initialize MCP server
mcp = FastMCP("local-financial-mcp")

# Resolve path to test data directory
data_dir = Path("./test_data_dir")
print("Resolved data_dir:", data_dir.resolve())

def load_json(phone_number: str, filename: str):
    """Return parsed JSON for *phone_number/filename* or {} if missing."""
    file_path = data_dir / phone_number / filename
    if file_path.exists():
        with open(file_path, "r", encoding="utf-8") as fp:
            return json.load(fp)
    return {}

# Cache allowed phone numbers (folder names)
allowed_numbers = {p.name for p in data_dir.iterdir() if p.is_dir()}

# -----------------------------------------------------------------------------
# Tools
# -----------------------------------------------------------------------------

@mcp.tool()
def authenticate_user(phone_number: str) -> str:
    """Dummy login — succeeds if *phone_number* directory exists."""
    phone_number = phone_number.strip()
    if phone_number in allowed_numbers:
        return f"✅ Authenticated {phone_number}"
    return "❌ Authentication failed — unknown phone number."

# -----------------------------------------------------------------------------
# Net‑worth
# -----------------------------------------------------------------------------

@mcp.tool()
def fetch_net_worth(phone_number: str) -> str:
    data = load_json(phone_number, "fetch_net_worth.json")
    if not data:
        return "No net‑worth data found."

    nw = data.get("netWorthResponse", {})
    total = nw.get("totalNetWorthValue", {}).get("units", "N/A")
    assets = nw.get("assetValues", [])
    liabilities = nw.get("liabilityValues", [])

    out = [f"💰 Total Net Worth: ₹{total}"]

    if assets:
        out.append("\n📊 Assets:")
        for a in assets:
            out.append(f"- {a.get('netWorthAttribute')}: ₹{a.get('value', {}).get('units')}")
    if liabilities:
        out.append("\n💸 Liabilities:")
        for l in liabilities:
            out.append(f"- {l.get('netWorthAttribute')}: ₹{l.get('value', {}).get('units')}")
    return "\n".join(out)

# -----------------------------------------------------------------------------
# Credit Report (full list, no slicing)
# -----------------------------------------------------------------------------

@mcp.tool()
def fetch_credit_report(phone_number: str) -> str:
    data = load_json(phone_number, "fetch_credit_report.json")
    if not data:
        return "No credit‑report data found."

    rep = (data.get("creditReports") or [{}])[0]
    score = rep.get("creditReportData", {}).get("score", {}).get("bureauScore", "N/A")
    accounts = rep.get("creditReportData", {}).get("creditAccount", {}).get("creditAccountDetails", [])

    lines = [f"🔢 Credit Score: {score}", "\n📄 Credit Accounts:"]
    for acc in accounts:
        lines.append(
            f"🏦 {acc.get('subscriberName')} | Opened: {acc.get('openDate')} | "
            f"Balance: ₹{acc.get('currentBalance')} | Due: ₹{acc.get('amountPastDue')} | "
            f"Status: {acc.get('accountStatus')} | Rating: {acc.get('paymentRating')}"
        )
    return "\n".join(lines)

# -----------------------------------------------------------------------------
# Bank transactions (show all)
# -----------------------------------------------------------------------------

TXN_TYPES = {
    1: "CREDIT", 2: "DEBIT", 3: "OPENING", 4: "INTEREST",
    5: "TDS", 6: "INSTALLMENT", 7: "CLOSING", 8: "OTHERS"
}

@mcp.tool()
def fetch_bank_transactions(phone_number: str) -> str:
    data = load_json(phone_number, "fetch_bank_transactions.json")
    if not data:
        return "No bank‑transaction data found."

    banks = data.get("bankTransactions", [])
    if not banks:
        return "No banks in transaction data."

    out = []
    for bank in banks:
        name = bank.get("bank", "Unknown Bank")
        out.append(f"\n📘 {name} — Transactions:")
        for amt, narr, date, t_type, mode, bal in bank.get("txns", []):
            out.append(
                f"🗓️ {date} | ₹{amt} | {TXN_TYPES.get(t_type, 'UNKNOWN')} via {mode} | {narr} | Bal: ₹{bal}"
            )
    return "\n".join(out)

# -----------------------------------------------------------------------------
# EPF details (unchanged)
# -----------------------------------------------------------------------------

@mcp.tool()
def fetch_epf_details(phone_number: str) -> str:
    data = load_json(phone_number, "fetch_epf_details.json")
    if not data:
        return "No EPF data found."

    uans = data.get("uanAccounts", [])
    if not uans:
        return "No UAN accounts available."

    lines = []
    for acc in uans:
        raw = acc.get("rawDetails", {})
        ests = raw.get("est_details", [])
        ov   = raw.get("overall_pf_balance", {})
        lines.append("🏢 Employment History:")
        for e in ests:
            lines.append(
                f"- {e.get('est_name')} | DOJ {e.get('doj_epf')} → DOE {e.get('doe_epf')} | "
                f"PF Balance: ₹{e['pf_balance'].get('net_balance', '0')}"
            )
        lines.append("\n💰 Overall EPF Summary:")
        lines.append(f"- Pension Balance: ₹{ov.get('pension_balance', '0')}")
        lines.append(f"- Current PF Balance: ₹{ov.get('current_pf_balance', '0')}")
        lines.append(f"- Employee Share Balance: ₹{ov.get('employee_share_total', {}).get('balance', '0')}")
    return "\n".join(lines)

# -----------------------------------------------------------------------------
# Mutual‑fund transactions (show all)
# -----------------------------------------------------------------------------

@mcp.tool()
def fetch_mf_transactions(phone_number: str) -> str:
    data = load_json(phone_number, "fetch_mf_transactions.json")
    if not data:
        return "No mutual‑fund data found."

    mfs = data.get("mfTransactions", [])
    if not mfs:
        return "No mutual‑fund investments available."

    out = []
    for mf in mfs:
        scheme = mf.get("schemeName")
        folio  = mf.get("folioId")
        out.append(f"\n📈 {scheme} (Folio: {folio})")
        for order, date, nav, units, amt in mf.get("txns", []):
            lbl = "BUY" if order == 1 else "SELL"
            out.append(f"🗓️ {date} | {lbl} | ₹{amt} @ ₹{nav}/unit | Units: {units:.4f}")
    return "\n".join(out)

# -----------------------------------------------------------------------------
# Entry point
# -----------------------------------------------------------------------------

if __name__ == "__main__":
    mcp.run(transport="stdio")

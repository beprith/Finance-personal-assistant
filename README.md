# Finance-personal-assistant
# Local Financial MCP Server

A lightweight, file-based **Memory Context Protocol (MCP)** server for demos, hackathons, and local development.  
It serves dummy financial data (net worth, credit report, bank/EPF/MF details) from JSON files on disk—no real integrations required.

---

## Features

* **Dummy authentication** — phone numbers map to folders  
* Net-worth summary  
* Credit-report snapshot  
* Recent bank transactions  
* EPF history & balances  
* Mutual-fund transaction log  
* All data read from local JSON

---

## Folder Layout

```
local-financial-mcp/
├─ main_mcp.py          # MCP server entry point
├─ test_data_dir/
│   ├─ 9999999999/      # phone number → folder
│   │   ├─ fetch_net_worth.json
│   │   ├─ fetch_credit_report.json
│   │   ├─ fetch_bank_transactions.json
│   │   ├─ fetch_epf_details.json
│   │   └─ fetch_mf_transactions.json
│   └─ 8888888888/      # another mock user
├─ requirements.txt
└─ README.md
```

---

## Setup

### 1. Clone & install
```bash
git clone https://github.com/your-org/local-financial-mcp.git
cd local-financial-mcp
pip install -r requirements.txt
```

### 2. Add test users
```bash
mkdir -p test_data_dir/9999999999
# copy or create the five JSON files in that folder…
```

---

## Run the Server

```bash
mcp dev main_mcp.py
```

`mcp dev` starts FastMCP in **stdio** mode (ideal for Langflow).

---

## Available Tools

| Tool | Purpose |
|------|---------|
| `authenticate_user(phone_number)` | Dummy login |
| `fetch_net_worth(phone_number)`   | Net-worth snapshot |
| `fetch_credit_report(phone_number)` | Score & accounts |
| `fetch_bank_transactions(phone_number)` | Recent banking txns |
| `fetch_epf_details(phone_number)` | EPF history & balances |
| `fetch_mf_transactions(phone_number)` | MF purchase/redemption log |

---

## Example (Langflow)

1. Add a **Tool** node.  
2. Choose **`fetch_net_worth`**.  
3. Input `9999999999`.  
4. Run → response:

```
💰 Total Net Worth: ₹1,86,726
📊 Assets:
- ASSET_TYPE_SAVINGS_ACCOUNTS: ₹1,86,726
```

---

## Requirements
* Python 3.8+
* `fastmcp` (included in `requirements.txt`)

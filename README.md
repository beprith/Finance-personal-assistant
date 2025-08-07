# Local Financial MCP Mock Server

This project provides a lightweight, local implementation of the **Model Context Protocol (MCP)** server for simulating financial‑data interactions. It is intended for developers who need a secure, simplified environment for testing applications without connecting to live financial systems or user data.

**See README_UI for UI guide**

---

## ✨ Features

| Capability               | Description                                                                 |
|--------------------------|-----------------------------------------------------------------------------|
| Dummy **Authentication** | Login succeeds if the phone number exists as a directory in `test_data_dir/`. |
| Pre‑canned **Financial Data** | Static JSON files for net‑worth, credit report, bank & MF transactions, EPF. |
| Plug‑and‑Play **Tools**  | Each JSON dataset is exposed as an MCP *tool* (see list below).               |
| **Quick setup**          | Zero external integrations—just clone, install, run.                         |

---

## 📂 Directory Layout

```text
.
├── main_mcp.py        # MCP server implementation (Python)
└── test_data_dir      # Dummy data grouped by phone number
    ├── 1111111111
    │   ├── fetch_net_worth.json
    │   └── ...
    └── 2222222222
        ├── fetch_credit_report.json
        └── ...
```

---

## 🔧 Installation & Run

### Prerequisites
* **Python 3.9+**

### Install dependencies
```bash
pip install mcp mcp-inspector
```

### Start the server
```bash
python main_mcp.py
```
The server runs using **stdio** transport by default.

---

## 🔑 Dummy Authentication

* Login is successful if the supplied phone number matches a folder in `test_data_dir/`.
* Example valid numbers: `1111111111`, `2222222222`, `3333333333`, … (see folders).

---

## 🛠️ Available MCP Tools

| Tool Name                  | Purpose                                        |
|----------------------------|------------------------------------------------|
| `authenticate_user`        | Dummy login check                              |
| `fetch_net_worth`          | Net‑worth summary + assets/liabilities         |
| `fetch_credit_report`      | Credit score & account details                 |
| `fetch_bank_transactions`  | Full bank‑statement style transaction list     |
| `fetch_epf_details`        | EPF balance & employment history               |
| `fetch_mf_transactions`    | Mutual‑fund buy/sell history                   |

All tools accept **`phone_number`** as their sole argument.

---

## 🚀 FastMCP Dev Environment UI

FastMCP ships with a lightweight developer UI that lets you explore any local MCP server, run tools, and inspect raw responses—all from the browser.

### 1. Install the FastMCP CLI (one‑time)
```bash
pip install fastmcp
```

### 2. Launch the Dev UI
From your project root:
```bash
fastmcp dev main_mcp.py
```
⚙️ *This spins up `main_mcp.py` **and** the web UI in one command.*

*Already registered the server in `mcp_servers.json`?*  Simply run:
```bash
fastmcp dev
```
FastMCP will auto‑detect `local-financial-mcp` and start it.

The UI opens at **http://localhost:4400** where you can:

![FastMCP Dev UI](a4c7f9b7-6534-419a-a6f9-902756562c00.png)
- Authenticate with any test phone number (e.g., `2222222222`).
- Invoke tools like `fetch_net_worth`, `fetch_credit_report`, etc.
- Inspect request/response JSON in real time for quick debugging.

### 3. Use alongside other FastMCP‑aware apps
The Dev UI acts purely as a client—you can keep it open while calling the same server from Langflow or the FastMCP CLI.

---

## ⚙️ FastMCP Server‑side Entry

If you want another FastMCP‑aware application (or CLI) to **auto‑launch** this mock server, add the following stanza to its `mcp_servers.json` (or similar) file:

```jsonc
{
  "servers": {
    "local-financial-mcp": {
      "transport": "stdio",          // or "sse" if you expose an HTTP endpoint
      "command": "python",
      "args": ["main_mcp.py"],
      "cwd": "<path-to-project-root>"  // folder containing main_mcp.py & test_data_dir/
    }
  }
}
```

* **transport** – Use `stdio` for the default pipe transport (fastest). Switch to `sse` if you wrap the server with an HTTP layer and expose `/mcp/stream`.
* **cwd** – Ensures relative paths (like `test_data_dir/`) resolve correctly.

Once registered, you can invoke tools directly via FastMCP CLI:

```bash
mcp call local-financial-mcp authenticate_user --phone_number 2222222222
mcp call local-financial-mcp fetch_net_worth --phone_number 2222222222
```

---

## 🧑‍💻 Example Workflow

```python
mcp.call("authenticate_user", phone_number="2222222222")
print(mcp.call("fetch_net_worth", phone_number="2222222222"))
```

---

## 🤝 Contributing
Pull requests are welcome—whether it’s extra dummy scenarios, bug fixes, or new tools.

---

## 🪪 License
This project is provided **as‑is** for educational and testing purposes.

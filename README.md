# Dork Scanner – Advanced Directory & File Discovery Tool

[![Python 3.6+](https://img.shields.io/badge/Python-3.6%2B-blue?logo=python&logoColor=white)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Requests](https://img.shields.io/badge/Requests-2.25+-green?logo=python&logoColor=white)](https://docs.python-requests.org/)
[![Security: Research](https://img.shields.io/badge/Security-Research%20Only-red)](https://github.com/Nobody-555-111/webpath-scanner)

**WebPath Scanner** is a powerful, flexible, and lightweight directory and file brute‑forcer designed for security researchers, penetration testers, and system administrators. It reads custom payload lines (supporting Google Dork‑like syntax) and converts them into real HTTP GET requests to discover hidden paths, backup files, configuration leaks, administrative panels, and other sensitive resources on web servers – **but only on systems you are authorised to test**.

> **IMPORTANT – LEGAL USE ONLY**  
> This tool must **only** be used against systems you own or have **explicit written permission** to test. Unauthorised scanning is illegal in most jurisdictions and may lead to severe penalties. The author assumes **zero liability** for misuse.

---

## 📑 Table of Contents

- [ Key Features](#-key-features)
- [ How It Works](#️-how-it-works)
- [ Requirements](#-requirements)
- [ Installation & Setup](#-installation--setup)
- [ Usage Guide](#-usage-guide)
  - [Basic Example](#basic-example)
  - [Understanding the Output](#understanding-the-output)
- [ Payload Format Deep Dive](#-payload-format-deep-dive)
  - [Supported Operators](#supported-operators)
  - [Conversion Examples](#conversion-examples)
- [ Customisation Options](#️-customisation-options)
  - [Adjusting Timeout & Content Length](#adjusting-timeout--content-length)
  - [Changing Headers](#changing-headers)
  - [Adding Proxy Support](#adding-proxy-support)
- [ Output & Results Management](#-output--results-management)
- [ Legal & Ethical Disclaimer](#️-legal--ethical-disclaimer)
- [ Troubleshooting](#-troubleshooting)
- [ Contributing](#-contributing)
- [ License](#-license)
- [ Author](#-author)

---

##  Key Features

| Feature | Description |
|---------|-------------|
| **Multi‑format payload support** | Understands `inurl:`, `filetype:`, `ext:`, `intitle:`, `intext:`, raw strings, and combined expressions. |
| **Smart path extraction** | Automatically converts each payload line into a clean, valid relative path (e.g., `inurl:(/etc/passwd)` → `/etc/passwd`). Works with parentheses, quotes, and special characters. |
| **Configurable HTTP requests** | Customisable User‑Agent, request timeout, and headers (easily add cookies, referers, etc.). |
| **Intelligent result filtering** | Saves only URLs that return **HTTP 200** AND a response body longer than **100 characters** – avoids empty error pages and minimal responses. |
| **Single‑file script** | No complex framework – just `auto_runner.py`, a payload file, and the `requests` library. |
| **Zero unnecessary dependencies** | Only `requests` – works on any Python 3.6+ environment, including Linux, macOS, Windows, and even Raspberry Pi. |
| **Automatic output organisation** | Creates a `results/` folder and saves discovered URLs as `results/domain.txt`, one URL per line. |
| **Real‑time progress display** | Shows each tested URL and final statistics (total lines, requests sent, successful hits). |

---

## ⚙️ How It Works

1. **Read payloads** – The script reads every non‑empty line from `payloads.txt`.
2. **Replace placeholder** – Any occurrence of `site:TARGET` is replaced with the actual target domain you entered.
3. **Extract a valid path** –  
   - If the line contains `inurl:`, the part after it is used as the path.  
   - If it contains `filetype:` or `ext:`, it creates a dummy file named `test.<extension>`.  
   - If it contains `intitle:` or `intext:`, the quoted text is cleaned and turned into a path (spaces become underscores).  
   - Otherwise, the whole line is treated as a path (after removing disallowed characters).
4. **Send HTTP GET request** – The script builds a full URL: `https://<domain>/<extracted_path>` and sends a request with a 5‑second timeout.
5. **Filter & save** – If the response status code is `200` **and** the response text length exceeds 100 characters, the URL is written to the output file.
6. **Report** – After processing all payloads, the script prints statistics.

---

## Requirements

- **Python** 3.6 or higher (3.10+ recommended)
- **`requests`** library (install via `pip`)

---

## 🚀 Installation & Setup

### 1. Clone the repository (or download the script)

```bash
git clone https://github.com/Nobody-555-111/Dork-scanner.git
cd webpath-scanner

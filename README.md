# WebPath Scanner

A lightweight, flexible directory and file scanner that reads payloads from a text file and sends HTTP requests to discover accessible paths, backup files, configuration files, and administrative panels on a target domain.

> **Use this tool only on systems you own or have explicit written permission to test.**

## Features

- Supports multiple payload formats: `inurl:`, `filetype:`, `ext:`, `intitle:`, `intext:`, and raw strings
- Automatically converts each payload line into a valid relative path
- Sends GET requests with a configurable User-Agent and timeout
- Saves successful URLs (HTTP 200 + content length > 100 characters) to an output file
- Simple, single‑file script – easy to modify and extend

## Requirements

- Python 3.6 or higher
- `requests` library

Install the required library:

```bash
pip install requests

import requests
import os
import re

TARGET_DOMAIN = input("Enter target domain: ").strip()
SAFE_DOMAIN = TARGET_DOMAIN.replace("https://", "").replace("http://", "").strip("/")
OUTPUT_FILE = f"results/{SAFE_DOMAIN}.txt"
PAYLOAD_FILE = "payloads.txt"
os.makedirs("results", exist_ok=True)

headers = {
    "User-Agent": "Mozilla/5.0 (Security Audit)"
}

with open(PAYLOAD_FILE, "r", encoding="utf-8", errors="ignore") as file:
    payloads = file.readlines()

success_count = 0
tested_count = 0

def extract_path_from_payload(line: str) -> str:
    line = re.sub(r'site:\S+', '', line).strip()
    
    if 'inurl:' in line:
        parts = line.split('inurl:', 1)
        if len(parts) > 1:
            path = parts[1].strip()
            if path.startswith('(') and path.endswith(')'):
                path = path[1:-1]
            path = re.sub(r'[^a-zA-Z0-9/\.\?\=\&\-\_]', '', path)
            return path if path else 'index.html'
    
    filetype_match = re.search(r'(?:filetype|ext):(\w+)', line)
    if filetype_match:
        ext = filetype_match.group(1)
        return f"test.{ext}"
    
    for op in ['intitle:', 'intext:']:
        if op in line:
            after = line.split(op, 1)[1].strip()
            after = re.sub(r'^["\']|["\']$', '', after)
            after = re.sub(r'\s+', '_', after)
            after = re.sub(r'[^a-zA-Z0-9_\-]', '', after)
            if after:
                return after
            else:
                return "search"
    
    line = re.sub(r'^["\']|["\']$', '', line)
    line = re.sub(r'\s+', '_', line)
    line = re.sub(r'[^a-zA-Z0-9_\-/]', '', line)
    if line:
        return line
    else:
        return "default"

with open(OUTPUT_FILE, "a", encoding="utf-8") as output:
    for index, line in enumerate(payloads, start=1):
        raw = line.strip()
        if not raw:
            continue
        
        raw = raw.replace("site:TARGET", f"site:{SAFE_DOMAIN}")
        
        tested_count += 1
        
        path = extract_path_from_payload(raw)
        
        if not path:
            continue
        
        url = f"https://{SAFE_DOMAIN}/{path}"
        
        print(f"[TEST {tested_count}] {url}")
        
        try:
            response = requests.get(url, headers=headers, timeout=5)
            if response.status_code == 200 and len(response.text) > 100:
                success_count += 1
                output.write(url + "\n")
                output.flush()
        except requests.RequestException:
            pass

print("\nDone.")
print(f"Total payload lines : {len(payloads)}")
print(f"Requests sent      : {tested_count}")
print(f"Successful URLs    : {success_count}")
print(f"Saved to           : results/{SAFE_DOMAIN}.txt")

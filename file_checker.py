# Beginner Cybersecurity File Checker
# Author: Lores
# Description: Simple static file analysis tool for suspicious indicators

import hashlib
import os

SUSPICIOUS_KEYWORDS = [
    "powershell",
    "cmd.exe",
    "wget",
    "curl",
    "base64",
    "eval(",
    "exec(",
    "nc ",
    "ncat",
    "socket",
    "subprocess",
    "rm -rf",
    "chmod +x"
]

def calculate_hash(file_path):
    sha256 = hashlib.sha256()
    with open(file_path, "rb") as f:
        while True:
            chunk = f.read(4096)
            if not chunk:
                break
            sha256.update(chunk)
    return sha256.hexdigest()

def scan_file(file_path):
    if not os.path.exists(file_path):
        print("❌ File not found.")
        return

    print(f"🔍 Scanning file: {file_path}")
    suspicious_hits = []

    with open(file_path, "rb") as f:
        content = f.read()

    text_content = content.decode(errors="ignore").lower()

    for keyword in SUSPICIOUS_KEYWORDS:
        if keyword in text_content:
            suspicious_hits.append(keyword)

    file_size = os.path.getsize(file_path)
    file_hash = calculate_hash(file_path)

    print(f"📄 File size: {file_size} bytes")
    print(f"🔑 SHA-256 Hash: {file_hash}")

    if suspicious_hits:
        print("\n🚨 RED ALERT: FILE IS SUSPICIOUS 🚨")
        for hit in suspicious_hits:
            print(f" - {hit}")
    else:
        print("\n✅ GREEN ALERT: FILE APPEARS CLEAN")

if __name__ == "__main__":
    file_to_scan = input("Enter path to file to scan: ")
    scan_file(file_to_scan)

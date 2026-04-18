#!/usr/bin/env python3
"""
🔐 Hash Checker
Calculate and verify file hashes - Educational Purpose Only
"""
import hashlib
import sys

def calculate_hash(filepath, algorithm="sha256"):
    """Calculate hash of a file"""
    try:
        hash_obj = hashlib.new(algorithm)
        with open(filepath, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_obj.update(chunk)
        return hash_obj.hexdigest()
    except Exception as e:
        return f"Error: {e}"

def main():
    if len(sys.argv) < 2:
        print("Usage: python hash_checker.py <filepath> [algorithm]")
        print("Algorithms: md5, sha1, sha256, sha512")
        return
    
    filepath = sys.argv[1]
    algorithm = sys.argv[2] if len(sys.argv) > 2 else "sha256"
    
    print(f"🔐 Calculating {algorithm.upper()} hash of: {filepath}")
    hash_value = calculate_hash(filepath, algorithm)
    print(f"\n✅ Hash: {hash_value}")

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
🛡️ Security Headers Checker
Check website security headers - Educational Purpose Only
"""
import requests
import sys

SECURITY_HEADERS = {
    "Content-Security-Policy": "Prevents XSS attacks",
    "X-Content-Type-Options": "Prevents MIME sniffing",
    "X-Frame-Options": "Prevents clickjacking",
    "Strict-Transport-Security": "Enforces HTTPS",
    "X-XSS-Protection": "XSS filtering",
    "Referrer-Policy": "Controls referrer info"
}

def check_headers(url):
    """Check security headers of a website"""
    try:
        response = requests.get(url, timeout=10)
        print(f"\n🔍 Security Headers for: {url}")
        print("=" * 50)
        
        found = []
        missing = []
        
        for header, description in SECURITY_HEADERS.items():
            if header in response.headers:
                found.append((header, response.headers[header]))
                status = "✅"
            else:
                missing.append((header, description))
                status = "❌"
            print(f"{status} {header}")
        
        print("\n📋 Summary:")
        print(f"✅ Found: {len(found)}")
        print(f"❌ Missing: {len(missing)}")
        
        if missing:
            print("\n⚠️ Recommendations:")
            for header, desc in missing:
                print(f"  • Add {header}: {desc}")
                
    except Exception as e:
        print(f"❌ Error: {e}")

def main():
    if len(sys.argv) < 2:
        url = input("Enter URL (e.g., https://example.com): ")
    else:
        url = sys.argv[1]
    
    if not url.startswith(("http://", "https://")):
        url = "https://" + url
    
    check_headers(url)

if __name__ == "__main__":
    main()

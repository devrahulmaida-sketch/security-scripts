#!/usr/bin/env python3
"""
🌐 Network Scanner
Scan local network for active devices - Educational Purpose Only
"""
import socket
import concurrent.futures
from datetime import datetime

def scan_device(ip):
    """Check if device is active"""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((ip, 80))
        sock.close()
        if result == 0:
            return ip, True
    except:
        pass
    return ip, False

def get_local_network():
    """Get local network range"""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
        parts = local_ip.split(".")
        return f"{parts[0]}.{parts[1]}.{parts[2]}.0/24"
    except:
        return "192.168.1.0/24"

def main():
    print("🔍 Network Scanner - Educational Use Only")
    print("-" * 40)
    
    network = get_local_network()
    print(f"📡 Scanning: {network}")
    print()
    
    base_ip = ".".join(network.split(".")[:-1])
    ip_list = [f"{base_ip}.{i}" for i in range(1, 255)]
    
    active_devices = []
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        results = executor.map(scan_device, ip_list)
        for ip, is_active in results:
            if is_active:
                active_devices.append(ip)
                print(f"✅ Device found: {ip}")
    
    print()
    print(f"📊 Found {len(active_devices)} active devices")
    
if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Amana Mart Ecosystem Developer & Server Management CLI (amana-cli)
Usage: amana [status|build|clean|docs|help]
"""

import sys
import os
import subprocess
import urllib.request

COLOR_MINT = "\033[38;2;16;243;162m"
COLOR_BLUE = "\033[38;2;51;181;255m"
COLOR_RESET = "\033[0m"
COLOR_RED = "\033[31m"

def print_banner():
    print(f"{COLOR_MINT}===================================================={COLOR_RESET}")
    print(f"{COLOR_MINT}   🚀 AMANA MART ECOSYSTEM DEVELOPER CLI (v2.5.0)   {COLOR_RESET}")
    print(f"{COLOR_BLUE}   Amana Suite (API) | Amana Mart (Web) | Mobile Apps{COLOR_RESET}")
    print(f"{COLOR_MINT}===================================================={COLOR_RESET}\n")

def check_status():
    print_banner()
    print("📊 [1/4] Checking Domain & API HTTP Statuses...")
    domains = [
        ("Amana Suite Backend API", "https://amanasuite.com/api/v1/config"),
        ("Amana Mart Web Portal", "https://amanamart.com"),
    ]
    for name, url in domains:
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'AmanaCLI/2.5'})
            res = urllib.request.urlopen(req, timeout=5)
            code = res.getcode()
            print(f"  {COLOR_MINT}✓{COLOR_RESET} {name}: HTTP {code} OK")
        except Exception as e:
            print(f"  {COLOR_RED}✗{COLOR_RESET} {name}: {e}")

    print("\n📦 [2/4] Checking PM2 Services...")
    try:
        subprocess.run(["pm2", "status"], check=False)
    except Exception:
        print("  PM2 not found or not active.")

    print("\n💾 [3/4] Checking Server Disk Space...")
    subprocess.run(["df", "-h", "/"], check=False)

    print("\n🧠 [4/4] Checking System Memory...")
    subprocess.run(["free", "-h"], check=False)

def build_app(target):
    print_banner()
    if target == "web":
        print("🔨 Building Next.js Web Portal (https://amanamart.com)...")
        subprocess.run(["/root/amana-mart-master-skill/scripts/build-react-web.sh"])
    elif target in ["user-app", "user"]:
        print("📱 Building Customer User App Release APK...")
        subprocess.run(["/root/amana-mart-master-skill/scripts/build-user-app.sh"])
    elif target in ["driver-app", "driver"]:
        print("🚚 Building Deliveryman Driver App Release APK...")
        export_env = os.environ.copy()
        export_env["ANDROID_HOME"] = "/opt/android-sdk"
        cmd = "cd /www/wwwroot/amanamartdeliverymanapp && /opt/flutter/bin/flutter build apk --release"
        subprocess.run(cmd, shell=True, env=export_env)
    elif target in ["vendor-app", "vendor"]:
        print("🏪 Building Store Merchant App Release APK...")
        export_env = os.parse_env() if hasattr(os, 'parse_env') else os.environ.copy()
        export_env["ANDROID_HOME"] = "/opt/android-sdk"
        cmd = "cd /www/wwwroot/amanamartvendorapp && /opt/flutter/bin/flutter build apk --release"
        subprocess.run(cmd, shell=True, env=export_env)
    else:
        print(f"Unknown build target '{target}'. Supported: web, user-app, driver-app, vendor-app")

def clean_server():
    print_banner()
    print("🧹 Running Server Health Check & Log Maintenance...")
    subprocess.run(["/root/amana-mart-master-skill/scripts/server-maintenance.sh"])

def print_help():
    print_banner()
    print("Usage: amana <command> [options]\n")
    print("Commands:")
    print("  amana status            Check system health, domains, PM2, disk, and memory")
    print("  amana build web         Rebuild Next.js Web Portal (amanamart.com)")
    print("  amana build user-app    Build Customer User App Release APK & sync to Drive")
    print("  amana build driver-app  Build Deliveryman App Release APK")
    print("  amana build vendor-app  Build Store Merchant App Release APK")
    print("  amana clean             Clean system logs & optimize server disk space")
    print("  amana docs              Show Master Skill & documentation path")

def main():
    if len(sys.argv) < 2:
        print_help()
        sys.exit(0)

    cmd = sys.argv[1].lower()
    if cmd == "status":
        check_status()
    elif cmd == "build":
        target = sys.argv[2].lower() if len(sys.argv) > 2 else "web"
        build_app(target)
    elif cmd == "clean":
        clean_server()
    elif cmd == "docs":
        print_banner()
        print("📚 Amana Mart Master Skill Directory: /root/amana-mart-master-skill")
        print("🌐 Interactive HTML Portal: /root/amana-mart-master-skill/index.html")
        print("🐙 GitHub Repository: https://github.com/mahmudulhassan-dev/amana-mart-master-skill")
    else:
        print_help()

if __name__ == "__main__":
    main()

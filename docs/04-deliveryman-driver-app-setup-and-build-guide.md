# Amana Mart Deliveryman Driver App Setup & Build Guide

## 1. Source Directory & Purpose
- **Source Directory:** `/www/wwwroot/amanamartdeliverymanapp`
- **Purpose:** Driver order acceptance, real-time GPS location broadcasting, earnings withdrawal, and customer delivery confirmation.

## 2. Mandatory Configuration
- **API Base URL:** `https://amanasuite.com`
- **Pusher Broadcaster:** Enables live driver location updates on customer tracking map.
- **Background Location Permission:** Requires `ACCESS_FINE_LOCATION` and `ACCESS_BACKGROUND_LOCATION` in `AndroidManifest.xml`.

## 3. Build Command
```bash
export ANDROID_HOME=/opt/android-sdk
cd /www/wwwroot/amanamartdeliverymanapp
/opt/flutter/bin/flutter build apk --release
```

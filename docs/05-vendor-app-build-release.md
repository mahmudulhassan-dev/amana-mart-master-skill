# Amana Mart Store Merchant App — Build & Release Guide

## 1. Android Compilation & Build Commands

### A. Standalone Merchant Release APK
Compile the standalone APK for store owners and merchants:

```bash
export ANDROID_HOME=/opt/android-sdk
cd /www/wwwroot/amanamartvendorapp
/opt/flutter/bin/flutter build apk --release
```

- **Output APK Path:** `/www/wwwroot/amanamartvendorapp/build/app/outputs/flutter-apk/app-release.apk`
- **Google Drive Sync Command:**
  ```bash
  cp /www/wwwroot/amanamartvendorapp/build/app/outputs/flutter-apk/app-release.apk /tmp/AmanaMart_Store_App.apk
  rclone copy /tmp/AmanaMart_Store_App.apk "google drive:All Web Site/Amana Mart/" --drive-chunk-size 32M -P
  ```

---

### B. Google Play Store Release Bundle (.aab)
To publish the merchant app on Google Play Store:

```bash
export ANDROID_HOME=/opt/android-sdk
cd /www/wwwroot/amanamartvendorapp
/opt/flutter/bin/flutter build appbundle --release
```

- **Output AAB Path:** `/www/wwwroot/amanamartvendorapp/build/app/outputs/bundle/release/app-release.aab`

---

## 2. iOS Build & TestFlight Release
For iOS devices:
```bash
cd /path/to/amanamartvendorapp
flutter build ipa --release
```
Upload to App Store Connect / TestFlight via Xcode.

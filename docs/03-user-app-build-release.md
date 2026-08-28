# Amana Mart Customer User App — Build & Release Guide

## 1. Android Compilation & Build Commands

### A. Standard Standalone Release APK (Single Binary)
This command builds a universal, standalone APK suitable for direct installation on any Android phone:

```bash
export ANDROID_HOME=/opt/android-sdk
cd /www/wwwroot/amanamartuserapp
/opt/flutter/bin/flutter build apk --release
```

- **Output Path:** `/www/wwwroot/amanamartuserapp/build/app/outputs/flutter-apk/app-release.apk`
- **Google Drive Sync:**
  ```bash
  cp /www/wwwroot/amanamartuserapp/build/app/outputs/flutter-apk/app-release.apk /tmp/AmanaMart_User_App.apk
  rclone copy /tmp/AmanaMart_User_App.apk "google drive:All Web Site/Amana Mart/" --drive-chunk-size 32M -P
  ```

---

### B. Google Play Store Release (Android App Bundle - AAB)
Google Play Store requires an **Android App Bundle (.aab)** for publishing:

```bash
export ANDROID_HOME=/opt/android-sdk
cd /www/wwwroot/amanamartuserapp
/opt/flutter/bin/flutter build appbundle --release
```

- **Output Path:** `/www/wwwroot/amanamartuserapp/build/app/outputs/bundle/release/app-release.aab`

---

### C. Split Per-ABI APKs (Smaller Binary Size)
To split into smaller architecture-specific APKs (ARM64 vs ARMv7 vs x86_64):

```bash
export ANDROID_HOME=/opt/android-sdk
cd /www/wwwroot/amanamartuserapp
/opt/flutter/bin/flutter build apk --release --target-platform android-arm,android-arm64,android-x64 --split-per-abi
```

---

## 2. iOS Build & Release (Xcode / TestFlight / App Store)

For iOS devices, Apple requires code signing via Xcode on macOS:

```bash
cd /path/to/amanamartuserapp
flutter build ipa --release
```

- Open `ios/Runner.xcworkspace` in Xcode.
- Configure Signing & Capabilities with your Apple Developer Team ID.
- Archive and upload to **TestFlight** or **App Store Connect**.

# Amana Mart Store Merchant App — Environment & PATH Setup Guide

## 1. Environment Variables Configuration

To develop and build the **Amana Mart Store Merchant App** (`amanamartvendorapp`), set up the following environment PATH variables on your machine:

### A. Linux Server & Workstation Environment (`~/.bashrc`)
```bash
export ANDROID_HOME=/opt/android-sdk
export JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
export PATH=$PATH:$ANDROID_HOME/cmdline-tools/latest/bin:$ANDROID_HOME/platform-tools:/opt/flutter/bin
```

### B. App Constants File Setup (`lib/util/app_constants.dart`)
In `/www/wwwroot/amanamartvendorapp/lib/util/app_constants.dart`:

```dart
class AppConstants {
  static const String appName = 'Amana Mart Store';
  static const String baseUrl = 'https://amanasuite.com';
  static const double appVersion = 4.1;
  static const String fontFamily = 'DMSans';
}
```

---

## 2. Dependencies Resolution & Build Test

Execute the following commands to fetch merchant app dependencies:

```bash
export ANDROID_HOME=/opt/android-sdk
cd /www/wwwroot/amanamartvendorapp
/opt/flutter/bin/flutter pub get
```

To test building the Merchant Release APK:
```bash
/opt/flutter/bin/flutter build apk --release
```

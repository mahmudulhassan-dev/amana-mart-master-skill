# Amana Mart Deliveryman Driver App — Prerequisites & Architecture Guide

## 1. Application Overview & Source Path
The **Amana Mart Deliveryman Driver Application** (`amanamartdeliverymanapp`) is a dedicated mobile app for delivery drivers to accept order assignments, broadcast real-time background GPS locations to customer tracking maps, navigate routes, and request earnings withdrawals.

- **Local Source Directory:** `/www/wwwroot/amanamartdeliverymanapp`
- **Main Entry Point:** `lib/main.dart`
- **Configuration Constants:** `lib/util/app_constants.dart`

---

## 2. Environment & Tooling Specifications

| Tool / Environment | Version / Requirement | Server / Workstation Path |
| :--- | :--- | :--- |
| **Flutter SDK** | Version 3.41.9 / 3.44.7 (Stable) | `/opt/flutter/bin/flutter` |
| **Android SDK** | API Levels 31, 33, 34, 35, 36 | `/opt/android-sdk` |
| **Java JDK** | OpenJDK 17 | `/usr/lib/jvm/java-17-openjdk-amd64` |
| **IDE** | Android Studio / VS Code | Local Workstation |
| **iOS Toolchain** | Xcode 15+ / 16+ | macOS Workstation |

---

## 3. Environment Readiness Diagnostic

Verify Flutter SDK and Java JDK readiness before building the driver app:

```bash
export ANDROID_HOME=/opt/android-sdk
cd /www/wwwroot/amanamartdeliverymanapp
/opt/flutter/bin/flutter doctor -v
```


# Amana Mart Deliveryman Driver App — Environment & PATH Setup Guide

## 1. System Environment & PATH Variables Setup

To develop and build the **Amana Mart Deliveryman Driver App** (`amanamartdeliverymanapp`), configure the following PATH variables:

### Linux / Server Workstation (`~/.bashrc`)
```bash
export ANDROID_HOME=/opt/android-sdk
export JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
export PATH=$PATH:$ANDROID_HOME/cmdline-tools/latest/bin:$ANDROID_HOME/platform-tools:/opt/flutter/bin
```

---

## 2. White-Labeled App Constants Setup (`lib/util/app_constants.dart`)

Configure the driver app branding in `/www/wwwroot/amanamartdeliverymanapp/lib/util/app_constants.dart`:

```dart
class AppConstants {
  static const String appName = 'Amana Mart Delivery';
  static const String baseUrl = 'https://amanasuite.com';
  static const double appVersion = 4.1;
  static const String fontFamily = 'DMSans';
}
```

---

## 3. Resolving Dependencies & Test Build

Fetch dependencies and verify compilation readiness:

```bash
export ANDROID_HOME=/opt/android-sdk
cd /www/wwwroot/amanamartdeliverymanapp
/opt/flutter/bin/flutter pub get
```

Compile Driver Release APK:
```bash
/opt/flutter/bin/flutter build apk --release
```

# Amana Mart Customer User App — Development Prerequisites Guide

## 1. Application Overview & Source Path
The **Amana Mart Customer User Application** is built with **Flutter 3.x** and **Dart** to deliver a high-performance cross-platform mobile app for Android and iOS.

- **Local Source Directory:** `/www/wwwroot/amanamartuserapp`
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
| **iOS Build Tool** | Xcode 15+ / 16+ | macOS Workstation |

---

## 3. Verifying Development Environment

Run the following command to verify Flutter and Android SDK readiness on your server/workstation:

```bash
export ANDROID_HOME=/opt/android-sdk
/opt/flutter/bin/flutter doctor
```

Verify Java 17 installation:
```bash
java -version
```
Expected output: `openjdk version "17.0.x"`

# Amana Mart Mobile App Development Environment Setup Guide

## 1. System Environment Variables Configuration

To develop and build **Amana Mart** mobile applications across Linux, macOS, or Windows, configure the following environment variables:

### A. Linux Server & Workstation (`~/.bashrc` / `~/.zshrc`)
```bash
export ANDROID_HOME=/opt/android-sdk
export JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
export PATH=$PATH:$ANDROID_HOME/cmdline-tools/latest/bin:$ANDROID_HOME/platform-tools:/opt/flutter/bin
```

Apply immediately:
```bash
source ~/.bashrc
```

### B. Windows Development Environment
1. **Flutter PATH:** Add `C:\flutter\bin` to System Environment Variables > `Path`.
2. **Android SDK:** Set `ANDROID_HOME` = `C:\Users\<User>\AppData\Local\Android\Sdk`.
3. **Java JDK 17:** Set `JAVA_HOME` = `C:\Program Files\Android\Android Studio\jbr`.

---

## 2. Amana Mart App Constants & Identity (`lib/util/app_constants.dart`)

Configure the white-labeled app constants in `/www/wwwroot/amanamartuserapp/lib/util/app_constants.dart`:

```dart
class AppConstants {
  static const String appName = 'Amana Mart';
  static const String webHostedUrl = 'https://amanamart.com';
  static const String baseUrl = 'https://amanasuite.com';
  static const double appVersion = 4.1;
  static const String fontFamily = 'DMSans';
}
```

---

## 3. Flutter & Android SDK Readiness Check

Run the readiness diagnostic to confirm all licenses and toolchains are active:

```bash
export ANDROID_HOME=/opt/android-sdk
/opt/flutter/bin/flutter doctor -v
```

If Android licenses are unaccepted:
```bash
yes | /opt/android-sdk/cmdline-tools/latest/bin/sdkmanager --licenses
```

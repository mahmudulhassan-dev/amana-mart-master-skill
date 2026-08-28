# Amana Mart Customer User App Setup & Build Guide

## 1. Source Directory & Configuration
- **Source Directory:** `/www/wwwroot/amanamartuserapp`
- **Configuration File:** `lib/util/app_constants.dart`

### Essential App Constants
```dart
class AppConstants {
  static const String appName = 'Amana Mart';
  static const String webHostedUrl = 'https://amanamart.com';
  static const String baseUrl = 'https://amanasuite.com';
  static const double appVersion = 4.1;
}
```

## 2. Build Environment
- **Flutter SDK:** `/opt/flutter/bin/flutter`
- **Android SDK:** `/opt/android-sdk`
- **Java Version:** OpenJDK 17

## 3. Android Build Configuration (`android/gradle.properties`)
```properties
org.gradle.jvmargs=-Xmx3072m -XX:MaxMetaspaceSize=1024m -XX:ReservedCodeCacheSize=512m -XX:+HeapDumpOnOutOfMemoryError
android.useAndroidX=true
android.enableJetifier=true
```

## 4. Automated Build Command
```bash
export ANDROID_HOME=/opt/android-sdk
cd /www/wwwroot/amanamartuserapp
/opt/flutter/bin/flutter build apk --release
```
**Output APK Path:** `/www/wwwroot/amanamartuserapp/build/app/outputs/flutter-apk/app-release.apk`

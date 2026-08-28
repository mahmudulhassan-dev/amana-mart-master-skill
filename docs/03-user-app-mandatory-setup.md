# Amana Mart Customer User App — Mandatory Setup & Branding Guide

## 1. App Name & Identity Configuration
Configure the Amana Mart brand identity in the following 3 files:

### A. Dart Constants (`lib/util/app_constants.dart`)
```dart
class AppConstants {
  static const String appName = 'Amana Mart';
  static const String webHostedUrl = 'https://amanamart.com';
  static const String baseUrl = 'https://amanasuite.com';
  static const double appVersion = 4.1;
}
```
*(CRITICAL: Ensure no trailing slash `/` at the end of `baseUrl`)*.

### B. Android Manifest (`android/app/src/main/AndroidManifest.xml`)
```xml
<application
    android:label="Amana Mart"
    android:icon="@mipmap/ic_launcher">
```

### C. iOS Properties (`ios/Runner/Info.plist`)
```xml
<key>CFBundleDisplayName</key>
<string>Amana Mart</string>
<key>CFBundleName</key>
<string>Amana Mart</string>
```

---

## 2. Branding Assets & App Icons Replacement
1. **App Logo:** Replace `/assets/images/logo.png` with the 512x512 PNG/WEBP Amana Mart logo.
2. **App Launcher Icon:** Replace `android/app/src/main/res/mipmap-*` folders with generated Amana Mart launcher icons.
3. **Notification Icon:** Replace `android/app/src/main/res/drawable/notification_icon.png` with a solid white PNG icon.

---

## 3. Package Identifier Setup (`com.amanamart.user`)
Update the Android package name in `android/app/build.gradle.kts`:
```kotlin
android {
    namespace = "com.amanamart.user"
    defaultConfig {
        applicationId = "com.amanamart.user"
        // ...
    }
}
```

---

## 4. Firebase FCM Push Notification Setup

### A. Android `google-services.json`
1. Open [Firebase Console](https://console.firebase.google.com/) > Select Amana Mart Project.
2. Register Android app with Package Name `com.amanamart.user`.
3. Download `google-services.json` and place it in `/www/wwwroot/amanamartuserapp/android/app/google-services.json`.

### B. Inline Firebase Initialization (`lib/main.dart`)
```dart
await Firebase.initializeApp(
  options: const FirebaseOptions(
    apiKey: "YOUR_FIREBASE_API_KEY",
    appId: "YOUR_FIREBASE_APP_ID",
    messagingSenderId: "YOUR_SENDER_ID",
    projectId: "amana-mart-project-id",
  ),
);
```

---

## 5. Google Maps API Keys Integration

Ensure the following 8 Google APIs are enabled in your Google Cloud Console: **Direction API, Distance Matrix API, Geocoding API, Maps SDK for Android, Maps SDK for iOS, Maps JavaScript API, Places API (New), Routes API**.

### A. Android Integration (`android/app/src/main/AndroidManifest.xml`)
```xml
<meta-data
    android:name="com.google.android.geo.API_KEY"
    android:value="YOUR_GOOGLE_MAPS_API_KEY" />
```

### B. iOS Integration (`ios/Runner/AppDelegate.swift`)
```swift
GMSServices.provideAPIKey("YOUR_GOOGLE_MAPS_API_KEY")
```

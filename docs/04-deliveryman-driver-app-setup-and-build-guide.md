# Amana Mart Deliveryman Driver App — Mandatory Setup & Branding Guide

## 1. App Name & Package Identity (`com.amanamart.deliveryman`)

### A. Dart Constants (`lib/util/app_constants.dart`)
```dart
class AppConstants {
  static const String appName = 'Amana Mart Delivery';
  static const String baseUrl = 'https://amanasuite.com';
  static const double appVersion = 4.1;
}
```

### B. Android Package & Manifest
In `android/app/build.gradle.kts`:
```kotlin
android {
    namespace = "com.amanamart.deliveryman"
    defaultConfig {
        applicationId = "com.amanamart.deliveryman"
        // ...
    }
}
```

In `android/app/src/main/AndroidManifest.xml`:
```xml
<application
    android:label="Amana Mart Delivery"
    android:icon="@mipmap/ic_launcher">
```

---

## 2. Background Location Permissions for Real-Time Tracking
Delivery drivers require background GPS location broadcasting to share live location with customer tracking maps:

In `android/app/src/main/AndroidManifest.xml`:
```xml
<uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />
<uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION" />
<uses-permission android:name="android.permission.ACCESS_BACKGROUND_LOCATION" />
```

---

## 3. Firebase FCM Push Notification Setup
1. Register Android app `com.amanamart.deliveryman` under Amana Mart Firebase Project.
2. Download `google-services.json` and place in `/www/wwwroot/amanamartdeliverymanapp/android/app/google-services.json`.
3. Notification Icon: Place white logo in `android/app/src/main/res/drawable/notification_icon.png`.

---

## 4. Google Maps API Integration
In `android/app/src/main/AndroidManifest.xml`:
```xml
<meta-data
    android:name="com.google.android.geo.API_KEY"
    android:value="YOUR_GOOGLE_MAPS_API_KEY" />
```
*(Enabled APIs: Direction API, Distance Matrix API, Geocoding API, Maps SDK for Android/iOS, Places API (New), Routes API)*.

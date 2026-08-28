# Amana Mart Customer User App — Version & Force Update Playbook

## 1. Overview of Force Update Architecture
To ensure all customers run the latest, bug-free, and secure build of **Amana Mart**, a backend-driven **Force Update System** is integrated between the Flutter mobile app and the Amana Suite API (`https://amanasuite.com`).

---

## 2. Step-by-Step Safe Live Update Procedure

### Step 1: Update Version in Flutter Source Code
Open `/www/wwwroot/amanamartuserapp/lib/util/app_constants.dart` and update `appVersion`:

```dart
class AppConstants {
  static const String appName = 'Amana Mart';
  static const double appVersion = 4.1; // Update to new version (e.g. 4.2)
  // ...
}
```
*(CRITICAL: Version must be a valid double value e.g., `4.1`, `4.2`, `5.0`)*.

---

### Step 2: Compile & Upload Updated App Binaries
1. **Android App Bundle (.aab):**
   ```bash
   export ANDROID_HOME=/opt/android-sdk
   cd /www/wwwroot/amanamartuserapp
   /opt/flutter/bin/flutter build appbundle --release
   ```
   Upload the generated `.aab` file to **Google Play Console > Production Track**.

2. **Standalone Universal APK:**
   ```bash
   /opt/flutter/bin/flutter build apk --release
   ```
   Sync to Google Drive for direct customer downloads (`google drive:All Web Site/Amana Mart/AmanaMart_User_App.apk`).

---

### Step 3: Trigger Force Update from Amana Suite Admin Panel
Once the updated build is live on Play Store / Google Drive:
1. Log in to **Amana Suite Admin Panel** at `https://amanasuite.com/login/admin`.
2. Open **Configurations > 3rd Party > App Settings**.
3. **Minimum Android App Version:** Set to `4.1` (or new release version).
4. **Minimum iOS App Version:** Set to `4.1`.
5. Click **Save Changes**.

---

## 3. How the Customer App Responds
When a customer opens an older version of the app (e.g., v4.0):
1. The app calls `/api/v1/config` on startup.
2. The config API returns `min_app_version_android: 4.1`.
3. Since local `appVersion (4.0) < min_app_version_android (4.1)`, the app immediately locks user input and pops up an un-dismissible **"Update Required"** dialog with a direct button to Google Play Store / download link.

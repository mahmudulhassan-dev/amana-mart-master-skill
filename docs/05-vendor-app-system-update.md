# Amana Mart Store Merchant App — Version & Force Update Playbook

## 1. Merchant App Force Update Logic
To ensure store owners and merchants are running the latest order-processing features and security patches, **Amana Suite** enforces version checks against `https://amanasuite.com`.

---

## 2. Step-by-Step Update Procedure

### Step 1: Update Version Double Value
Open `/www/wwwroot/amanamartvendorapp/lib/util/app_constants.dart` and update `appVersion`:

```dart
class AppConstants {
  static const String appName = 'Amana Mart Store';
  static const double appVersion = 4.1; // Update to double e.g. 4.2
  // ...
}
```

---

### Step 2: Compile & Upload Merchant App Binaries
```bash
export ANDROID_HOME=/opt/android-sdk
cd /www/wwwroot/amanamartvendorapp
/opt/flutter/bin/flutter build appbundle --release
/opt/flutter/bin/flutter build apk --release
```

---

### Step 3: Admin Panel Force Update Threshold
1. Log in to **Amana Suite Admin Panel** at `https://amanasuite.com/login/admin`.
2. Open **Configurations > 3rd Party > App Settings**.
3. **Minimum Store App Version:** Set to `4.1` (or new release version).
4. Click **Save Changes**.

When a merchant opens an older app, the app detects `localVersion < minimumVersion` and locks screen with a mandatory Play Store / Drive update link.

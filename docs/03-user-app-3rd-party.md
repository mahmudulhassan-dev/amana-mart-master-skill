# Amana Mart Customer App — 3rd Party Integrations Guide

## 1. Google Social Login Setup

### A. Firebase Authentication Console
1. Open [Firebase Console](https://console.firebase.google.com/) > Select **Amana Mart** Project.
2. Go to **Authentication > Sign-in method** > Enable **Google**.

### B. SHA1 & SHA256 Fingerprint Addition
1. Add Debug & Release SHA1/SHA256 signatures under **Project Settings > Android Apps > Add Fingerprint**.
2. Download updated `google-services.json` and place in `/www/wwwroot/amanamartuserapp/android/app/google-services.json`.

### C. Dart Client ID (`lib/util/app_constants.dart`)
```dart
static const String googleServerClientId = 'YOUR_GOOGLE_SERVER_CLIENT_ID.apps.googleusercontent.com';
```

---

## 2. Facebook Social Login Setup

### A. Facebook Developer Console (`developers.facebook.com`)
1. Create a Facebook App named **Amana Mart**.
2. Add product: **Facebook Login**.
3. Set Privacy Policy URL (`https://amanamart.com/privacy-policy`) and Terms URL (`https://amanamart.com/terms-and-conditions`).

### B. Android Configuration (`android/app/src/main/res/values/strings.xml`)
```xml
<resources>
  <string name="app_name">Amana Mart</string>
  <string name="facebook_app_id">YOUR_FACEBOOK_APP_ID</string>
  <string name="fb_login_protocol_scheme">fbYOUR_FACEBOOK_APP_ID</string>
  <string name="facebook_client_token">YOUR_FACEBOOK_CLIENT_TOKEN</string>
</resources>
```

---

## 3. Apple Sign-In Integration

### A. Apple Developer Account (`developer.apple.com`)
1. Obtain **Team ID** from Membership details.
2. Create Service ID and download `.p8` Private Auth Key (`AuthKey_XXXXXXXXXX.p8`).

### B. Amana Suite Admin Panel Setup
1. Open **Admin Panel > 3rd Party > Apple Login**.
2. Input:
   - **Client ID for Web:** Service ID identifier
   - **Client ID for App:** `com.amanamart.user`
   - **Team ID:** Apple Team ID
   - **Key ID:** `XXXXXXXXXX`
   - **Service File:** Upload `AuthKey_XXXXXXXXXX.p8`
3. Toggle status **Active**.

---

## 4. Firebase Phone OTP Verification Setup

### A. Firebase Console
1. Go to **Firebase Console > Authentication > Sign-in method** > Enable **Phone**.
2. Add authorized domain: `amanamart.com` and `amanasuite.com` under **Authorized Domains**.

### B. Amana Suite Admin Configuration
1. Copy **Web API Key** from Firebase Project Settings.
2. Open **Admin Panel > Settings > 3rd Party > Firebase OTP Verification**.
3. Paste **Web API Key** and toggle **Firebase OTP Verification = ON**.
4. Turn on **Customer Verification** in Admin Panel > Login Setup.

# Amana Mart React / Next.js Web Portal — Mandatory Web Configuration Guide

## 1. Environment & API Configuration (`/www/wwwroot/amanamart/.env.production`)

Configure the core API and Google Maps keys in `.env.production`:

```env
NEXT_PUBLIC_BASE_URL="https://amanasuite.com"
NEXT_PUBLIC_GOOGLE_MAP_KEY="YOUR_GOOGLE_MAPS_API_KEY"
NEXT_PUBLIC_APP_NAME="Amana Mart"
NEXT_PUBLIC_WEB_HOST="https://amanamart.com"
```

*(CRITICAL: Ensure no trailing slash `/` at the end of `NEXT_PUBLIC_BASE_URL`)*.

---

## 2. Social Login Credentials Setup (`src/utils/staticCredential.js`)

Configure Google and Facebook OAuth app credentials in `/www/wwwroot/amanamart/src/utils/staticCredential.js`:

```javascript
export const google_client_id = "YOUR_GOOGLE_CLIENT_ID.apps.googleusercontent.com";
export const fb_app_id = "YOUR_FACEBOOK_APP_ID";
```

### Required Google OAuth Credentials:
- Open [Google Cloud Console Credentials](https://console.cloud.google.com/apis/credentials).
- Add `https://amanamart.com` to **Authorized JavaScript Origins**.
- Add `https://amanamart.com/auth/google/callback` to **Authorized Redirect URIs**.
- Enable **People API** in Google Cloud Console.

---

## 3. Web Firebase Push Notification Setup (`public/firebase-messaging-sw.js`)

Place `firebase-messaging-sw.js` in `/www/wwwroot/amanamart/public/`:

```javascript
importScripts('https://www.gstatic.com/firebasejs/9.0.0/firebase-app-compat.js');
importScripts('https://www.gstatic.com/firebasejs/9.0.0/firebase-messaging-compat.js');

firebase.initializeApp({
  apiKey: "YOUR_FIREBASE_API_KEY",
  authDomain: "amana-mart.firebaseapp.com",
  projectId: "amana-mart",
  storageBucket: "amana-mart.appspot.com",
  messagingSenderId: "YOUR_SENDER_ID",
  appId: "YOUR_APP_ID"
});

const messaging = firebase.messaging();
```

---

## 4. Mandatory Dual-Language Setup (English + Bengali ONLY)
Configure Next.js i18next language options:
- `src/language/en.js` (English UI Keys)
- `src/language/bn.js` (Bengali UI Keys — 100% Translated)
- `src/components/header/top-navbar/language/languageList.js` configured with US (`en`) and Bangladesh (`bn`) flags.

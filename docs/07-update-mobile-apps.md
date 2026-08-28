# Amana Mart Mobile Applications Version Update Playbook

## 1. Overview of Mobile Apps Upgrade Strategy
The 3 Flutter mobile applications in the **Amana Mart Ecosystem**—**Customer User App** (`amanamartuserapp`), **Deliveryman Driver App** (`amanamartdeliverymanapp`), and **Store Merchant App** (`amanamartvendorapp`)—share core networking, UI themes, and API models. Follow this playbook when upgrading Flutter mobile app versions.

---

## 2. Git Branch Merge Upgrade Procedure for Flutter Apps

### Step 1: Commit & Backup Mobile Source Code
Before making file modifications, commit and push live custom mobile code to your Git repository:

```bash
cd /www/wwwroot/amanamartuserapp # (or deliveryman / vendor app)
git status
git add .
git commit -m "chore: backup live custom mobile app source code before version upgrade"
git push origin main
```

---

### Step 2: Merge Upgrade Package
Create an upgrade branch, extract changed files or new version files, and merge into `main`:

```bash
git checkout -b feature/mobile-upgrade-v4.2
# Replace changed files in lib/ and assets/
git add .
git commit -m "feat: apply v4.2 mobile app source updates"

git checkout main
git merge feature/mobile-upgrade-v4.2
```

---

### Step 3: Update Version Constants (`app_constants.dart`)
In `lib/util/app_constants.dart`:
```dart
static const double appVersion = 4.2; // Match new release version
```

---

### Step 4: Clean Build Cache & Test Compilation
Run Flutter clean and dependency resolution before building release APKs:

```bash
export ANDROID_HOME=/opt/android-sdk
/opt/flutter/bin/flutter pub cache clean -f
/opt/flutter/bin/flutter clean
/opt/flutter/bin/flutter pub get
/opt/flutter/bin/flutter build apk --release
```

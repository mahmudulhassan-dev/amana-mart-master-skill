# Amana Mart Troubleshooting & Playbook

## 1. Web Portal Text Stays in English When Switching to Bengali
- **Cause:** `src/language/bn.js` contains English values instead of Bengali text.
- **Fix:** Translate all keys in `src/language/bn.js` using `scripts/update-translations.py` and rebuild Next.js.

## 2. Flutter Release APK Fails on Gradle Memory Limit
- **Cause:** Gradle daemon attempting to allocate 8GB heap memory.
- **Fix:** Update `android/gradle.properties`:
  `org.gradle.jvmargs=-Xmx3072m -XX:MaxMetaspaceSize=1024m -XX:ReservedCodeCacheSize=512m`

## 3. Mobile App Frozen on Native Splash Screen
- **Cause:** Missing JS bundle or SVG import crash in React Native/Expo.
- **Fix:** Embed offline bundle (`assets/index.android.bundle`) or replace raw `.svg` `require()` imports with Native Vector Icons (`Ionicons`).

## 4. Server Disk Full (100% Used)
- **Cause:** Uncapped `/var/log/syslog` or `/var/log/mail.log` growing > 100GB.
- **Fix:** Run `/root/amana-mart-master-skill/scripts/server-maintenance.sh`.

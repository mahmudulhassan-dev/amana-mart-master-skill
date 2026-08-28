# Amana Mart React Web Frontend Setup & Deploy Guide

## 1. Directory & Language Rules
- **Server Directory:** `/www/wwwroot/amanamart`
- **Supported Languages:** **English (`en`)** and **Bengali (`bn`) ONLY**.
- **Translation Files:**
  - `src/language/en.js` (English UI Keys)
  - `src/language/bn.js` (Bengali UI Keys — 100% Translated)

## 2. i18n & Flag Configuration
- `src/components/header/top-navbar/language/languageList.js` configured with US and Bangladesh flags.
- `rtlLanguageList.js` set to empty (no RTL languages).

## 3. Build and Deployment Command
```bash
cd /www/wwwroot/amanamart
npm run build
pm2 restart amanamart
```

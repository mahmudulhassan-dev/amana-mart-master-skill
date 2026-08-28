# Amana Mart React / Next.js Web Portal — Theme & i18n Customization Guide

## 1. Brand Theme & Color Options (`src/theme/`)

Configure Amana Mart's brand colors in `/src/theme/dark-theme-options.js` and `/src/theme/light-theme-options.js`:

- **Primary Neon Mint:** `#10F3A2`
- **Secondary Cyan Blue:** `#33B5FF`
- **Background Pitch Black:** `#0B0E14`
- **Paper Surface Card:** `#121722`

```javascript
// src/theme/dark-theme-options.js
export const darkThemeOptions = {
  palette: {
    mode: 'dark',
    primary: {
      main: '#10F3A2',
      light: '#50F8BC',
      dark: '#02C074',
    },
    secondary: {
      main: '#33B5FF',
    },
    background: {
      default: '#0B0E14',
      paper: '#121722',
    },
  },
};
```

---

## 2. Typography & Fonts (`src/theme/base-theme-options.js`)

Configure the font family in `src/theme/base-theme-options.js`:

```javascript
typography: {
  fontFamily: '"Plus Jakarta Sans", "Noto Sans Bengali", sans-serif',
}
```

---

## 3. Mandatory Dual-Language Setup (English + Bengali ONLY)

### A. i18n Configuration (`src/language/i18n.js`)
```javascript
import i18n from 'i18next';
import { initReactI18next } from 'react-i18next';
import english from './en.js';
import bengali from './bn.js';

const resources = {
  en: { translation: english },
  bn: { translation: bengali },
};

i18n.use(initReactI18next).init({
  resources,
  lng: 'en',
  fallbackLng: 'en',
  interpolation: { escapeValue: false },
});

export default i18n;
```

### B. Language List Component (`src/components/header/top-navbar/language/languageList.js`)
Configure language switcher dropdown with Bangladesh and US flags:

```javascript
import usFlag from '../../../../../public/static/country-flags/us.png';
import bdFlag from '../../../../../public/static/country-flags/bd.png';

export const languageList = [
  { languageCode: 'en', languageName: 'English', countryCode: 'US', countryFlag: usFlag },
  { languageCode: 'bn', languageName: 'Bengali - বাংলা', countryCode: 'BD', countryFlag: bdFlag },
];
```

---

## 4. Default Country Filter Setup (`CustomPhoneInput.js`)
In `src/components/custom-component/CustomPhoneInput.js`:
- Set default country to **Bangladesh (`bd`)**.
- Lock country selection or restrict to `onlyCountries={['bd']}` for local Bangladesh operations.

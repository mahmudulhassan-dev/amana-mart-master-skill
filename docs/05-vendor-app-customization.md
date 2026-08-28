# Amana Mart Store Merchant App — Theme, Language & Customization Guide

## 1. Brand Theme & Color Palette (`lib/theme/`)
Configure Amana Mart Store brand colors in `lib/theme/light_theme.dart` and `dark_theme.dart`:

- **Primary Brand Color (Neon Mint):** `#10F3A2`
- **Secondary Accent (Cyan Blue):** `#33B5FF`
- **Dark Theme Background (Pitch Black):** `#0B0E14`
- **Card Surface Color:** `#121722`

```dart
ThemeData dark({Color color = const Color(0xFF10F3A2)}) => ThemeData(
  fontFamily: AppConstants.fontFamily,
  primaryColor: color,
  secondaryHeaderColor: const Color(0xFF33B5FF),
  scaffoldBackgroundColor: const Color(0xFF0B0E14),
  cardColor: const Color(0xFF121722),
  brightness: Brightness.dark,
);
```

---

## 2. Language Setup (English + Bengali Only)
The merchant app localization files live in `/assets/language/`:
- `/assets/language/en.json` (English merchant strings)
- `/assets/language/bn.json` (Bengali merchant strings)

In `/www/wwwroot/amanamartvendorapp/lib/util/app_constants.dart`:
```dart
static List<LanguageModel> languages = [
  LanguageModel(imageUrl: Images.bangladesh, languageName: 'Bengali', countryCode: 'BD', languageCode: 'bn'),
  LanguageModel(imageUrl: Images.us, languageName: 'English', countryCode: 'US', languageCode: 'en'),
];
```

---

## 3. Merchant Order Ringtone & Notification Sound
Store merchants require a clear audio alert when a new customer order arrives:
1. **Android Sound:** Replace `/android/app/src/main/res/raw/notification.wav` with a distinct order alert chime.
2. **Assets Sound:** Replace `/assets/notification.mp3` with your merchant chime file.

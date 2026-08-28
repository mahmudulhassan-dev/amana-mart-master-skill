# Amana Mart Customer User App — Theme, UI & Customization Guide

## 1. App Theme & Brand Color Palette
Customize Amana Mart's brand colors in `lib/theme/light_theme.dart` and `lib/theme/dark_theme.dart`:

### A. Brand Colors Specifications
- **Primary Color (Neon Mint):** `#10F3A2`
- **Secondary Color (Cyan Blue):** `#33B5FF`
- **Dark Background (Pitch Black):** `#0B0E14`
- **Card Surface:** `#121722`

### B. `lib/theme/dark_theme.dart` Configuration
```dart
ThemeData dark({Color color = const Color(0xFF10F3A2)}) => ThemeData(
  fontFamily: AppConstants.fontFamily,
  primaryColor: color,
  secondaryHeaderColor: const Color(0xFF33B5FF),
  disabledColor: const Color(0xFFA0AEC0),
  scaffoldBackgroundColor: const Color(0xFF0B0E14),
  cardColor: const Color(0xFF121722),
  brightness: Brightness.dark,
  // ...
);
```

---

## 2. Language & Internationalization Setup (English + Bengali Only)
The mobile app uses JSON files in `/assets/language/` for UI localization.

### A. Supported Languages (`assets/language/`)
- `/assets/language/en.json` (English translations)
- `/assets/language/bn.json` (Bengali translations)

*(Remove all unused language JSON files like Spanish `es.json` or Arabic `ar.json` to keep app binary compact)*.

### B. Language Model Definition (`lib/util/app_constants.dart`)
```dart
static List<LanguageModel> languages = [
  LanguageModel(imageUrl: Images.bangladesh, languageName: 'Bengali', countryCode: 'BD', languageCode: 'bn'),
  LanguageModel(imageUrl: Images.us, languageName: 'English', countryCode: 'US', languageCode: 'en'),
];
```

---

## 3. Font Family Setup (`DMSans` / `PlusJakartaSans`)
Font configuration in `pubspec.yaml` and `AppConstants`:

```yaml
flutter:
  fonts:
    - family: DMSans
      fonts:
        - asset: assets/font/DMSans-Regular.ttf
        - asset: assets/font/DMSans-Bold.ttf
          weight: 700
```

In `lib/util/app_constants.dart`:
```dart
static const String fontFamily = 'DMSans';
```

---

## 4. Custom Notification Sounds
1. **Android Ringtone:** Replace `/android/app/src/main/res/raw/notification.wav` with a short Amana Mart alert sound.
2. **Assets Sound:** Replace `/assets/notification.mp3` with your preferred sound file.

---

## 5. Web Share Link (`webHostedUrl`)
In `lib/util/app_constants.dart`:
```dart
static const String webHostedUrl = 'https://amanamart.com';
```
*(When customers share a store or product link, the app generates a share link pointing to `https://amanamart.com`)*.

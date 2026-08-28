Skip to content

6amMart Documentation

[ Installation ](/installation)

[ Customization ](/customization)

[ Any Question? ](https://wa.me/8801810494911?text=Hi%2C%20I%20want%20to%20chat%20about%206amMart.)

View Categories

Table of Contents

  * Language
    * Add New Language
    * Remove Existing Language
  * Change App Color
    * Change App Font 
  * Change notification sound



Setup Essentials

Requirements for 6amMart Installation

**Admin & Web (V4.1)**

  * PHP **8.3** or higher
  * MySQL **5.7** or higher
  * Laravel **12**



**Mobile App (V4.1)**

  * IDE:[ ](https://developer.android.com/studio)Android Studio latest version
  * Flutter SDK (version **3.44.7** Stable)
  * Install [JDK 17](https://www.oracle.com/java/technologies/javase/jdk17-archive-downloads.html)
  * Xcode **26.2** for IPA file build



**For React (V4.1)**

  * Node js **v16.8** or higher
  * Npm / Yarn 
  * Vs code / Webstrom



**For Rental Module (V2.1)**

  * You need to use minimum code version **4.0**



Don’t Show It Again

GOT IT

## **Language** #

### **Add New Language** #

If you want to add any new language then follow this steps:

  * Go to **/assets/language** and press the right button on the language folder and create a new file and name it with your language code(.json). For example, if your language is Spanish, then you have to name your file as **es.json**. You have to name it with a proper and valid language code otherwise, the app won’t work. To get the language and country code, you can visit this URL: <https://docs.oracle.com/cd/E13214_01/wli/docs92/xref/xqisocodes.html>


  * Copy all data from **en.json** and paste it into your created file.
  * Translate all English text placed here after colon(:) to your expected language. Their texts are in key-value format. You have to translate the value only, not the key. Otherwise, it won’t work. For example: **“office”****:********“Office”** , -> **“office”** : **“Oficina”,**
  * Add your country picture in the **< Project>/assets/images** folder. Must keep the file extension in png format. For example, **spanish.png**
  * Go to** <Project>/lib/utils/images.dart **file**,** add a variable**** with your country picture name. For example, if your added country picture name is **spanish.png** , then add a variable like -> static const String _spanish_ = ‘assets/image/spanish.png’;
  * Go to **< Project>/lib/utils/app_constrants.dart **file, scroll down to the bottom and add one more **LanguageModel** under**the languages** array with your**imageUrl** , **languageName** , **countryCode** and**languageCode**. Again must remember that your language code and country code should be valid otherwise, the app won’t work



### **Remove Existing Language** #

  * If you wish to eliminate any currently present language, simply exclude the particular **LanguageModel** from the languages list.



Make Default Language

  * To set your language as the default language, place your **LanguageModel** at the first index of your language list.



Now uninstall your application from your devices and install it again.

## **Change App Color** #

If you want to customize app theme color then follow these steps :

  * Open the **< project>/lib/theme/light_theme.dart **file. Set **primaryColor** , **foregroundColor, secondary** and other colors, and adjust them according to your preferences.
  * In the same way for the dark theme, open the **< project>/lib/theme/dark_theme.dart **file. Set**primaryColor** , **foregroundColor** ,**secondary** and other colors, and adjust them according to your preferences.



### **Change App Font** #

At 6amMart, we use the **Poppins** font. However, if you want to change the app’s font, then follow these steps:

  * Download your preferred font from the internet. Google has many free fonts you can check them: <https://fonts.google.com/>
  * Unzip fonts and paste them to **< project>/assets/font/** folder.
  * Mentioned them in** <project>/pubspec.yaml** file like


    
    
    fonts:
        - family: YOUR_FONT_FAMILY_NAME
          fonts:
            - assets/font/YOUR_FONT_FILE_NAME.ttf
              weight: YOUR_FONT_WEIGHT
    
    
    fonts:
        - family: YOUR_FONT_FAMILY_NAME
          fonts:
            - assets/font/YOUR_FONT_FILE_NAME.ttf
              weight: YOUR_FONT_WEIGHT

  * Replace the font family name in the **< project>/lib/util/app_constants.dart** file.


    
    
    static const String fontFamily = YOUR_FONT_FAMILY_NAME;
    
    
    static const String fontFamily = YOUR_FONT_FAMILY_NAME;

## **Change notification sound** #

If you wish to change the notification sound for the iOS app and also for the Android app, then you need to follow these steps : 

**Android App :**

  * Go to **< project>/android/app/src/main/res/raw/notification.wav** file. Replace this file with your desired ringtone file. Ensure that you do not change the filename. It must remain as **notification.wav**
  * If you find**notification.mp3 or notification.wav** file in** <project>/assets** file. Replace this also with your desired ringtone file. Ensure that you do not change the filename. It must remain as **notification.mp3 or notification.wav**



**Note**

Please use the exact file name as described. And make sure the audio file is **small in duration and file size**. Otherwise, it will not work.

#### Share This Article :

  * [](https://www.facebook.com/sharer/sharer.php?u=)
  * [](https://twitter.com/intent/tweet?url=)
  * [](https://www.linkedin.com/shareArticle?mini=true&url=)
  * [](https://pinterest.com/pin/create/button/?url=)



[ Mandatory Setup]()[App Build & Release ]()

Manage Consent

We use cookies to give you a smoother experience and improve our services.

[Cookies Policy](https://6ammart.app/cookie-policy-for-6ammart/) | [Privacy policy](https://6ammart.app/privacy-policy/)

Functional Functional Always active 

The technical storage or access is strictly necessary for the legitimate purpose of enabling the use of a specific service explicitly requested by the subscriber or user, or for the sole purpose of carrying out the transmission of a communication over an electronic communications network.

Preferences Preferences

The technical storage or access is necessary for the legitimate purpose of storing preferences that are not requested by the subscriber or user.

Statistics Statistics

The technical storage or access that is used exclusively for statistical purposes. The technical storage or access that is used exclusively for anonymous statistical purposes. Without a subpoena, voluntary compliance on the part of your Internet Service Provider, or additional records from a third party, information stored or retrieved for this purpose alone cannot usually be used to identify you.

Marketing Marketing

The technical storage or access is required to create user profiles to send advertising, or to track the user on a website or across several websites for similar marketing purposes.

  * Manage options
  * Manage services
  * Manage {vendor_count} vendors
  * [Read more about these purposes](https://cookiedatabase.org/tcf/purposes/)



Accept Deny View preferences Save preferences View preferences

  * {title}
  * {title}
  * {title}



Manage consent

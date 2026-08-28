Skip to content

6amMart Documentation

[ Installation ](/installation)

[ Customization ](/customization)

[ Any Question? ](https://wa.me/8801810494911?text=Hi%2C%20I%20want%20to%20chat%20about%206amMart.)

View Categories

Table of Contents

  * Country Filter​
  * Add New Local Language​
  * Change App color​
  * Change App Font​



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

## **Country Filter**[**​**](https://docs.6amtech.com/docs-six-am-mart/react-web-app/customization#country-filter) #

To change the country filter, follow the steps below-

  * If you want your country only in country choosing dialog which we saw in login, registration and forget password page, you have to set your default country first from admin panel Business Setup section. Then open <project>src/components/custom-component/CustomPhoneInput.js file and search onlyCountries Now add a parameter with value like this: onlyCountries={[defaultCountry]}
  * If you want to disable the country choosing dialog then just change disableDropdown=”false” to disableDropdown=”true”.



**TIP**

Recommended tutorial is below 👇

## **Add New Local Language**[**​**](https://docs.6amtech.com/docs-six-am-mart/react-web-app/customization#add-new-local-language) #

To add a new language, follow the steps below-

  * Go to project /src/language and press the right button on the language folder and create a new file and name it with your language code (.js). For example if your language is Bengali then you have to name your file as bn.js. You have to name it with proper and valid language code otherwise app won’t work. For getting language and country code you can visit this url: <https://docs.oracle.com/cd/E13214_01/wli/docs92/xref/xqisocodes.html>
  * Copy all data from en.js and paste it in your created file.
  * Translate all English text placed here after colon(:) to your local language. Their texts are in key-value format. You have to translate the value only, not the key , otherwise it won’t work. For example: “home”: “Home” -> “home”: “বাড়ি”*
  * Import your language file i18n.js which is placed in the same folder.after that in i18n.js file (resources object) add your language as like other.
  * You can set initial language by following way I18n.js file set lng: “your initial language” and set fallbackLng:”your initial language”.
  * Open src/components/header/top-navbar/language/languageLists.js file and add one more object under the languageLists array with your languageCode, languageName, countryCode, countryFlag. Again must remember that your language code and country code should valid otherwise it won’t work. In countryFlag you have to import countryFlag with correct path.



/src/language?/i18n.js
    
    
    const resources = {
       en: {
           translation: english,
       },
       bn: {
           translation: bengali,
       },
       ar: {
           translation: arabic,
       },
    }
    
    i18n.use(initReactI18next) // passes i18n down to react-i18next
       .init({
           resources,
           lng: 'en',
           fallbackLng: 'en',
           interpolation: {
               escapeValue: false,
           },
       })

**TIP**

Recommended tutorials are below 👇

## **Change App color**[**​**](https://docs.6amtech.com/docs-six-am-mart/react-web-app/customization#change-app-color) #

To change the app color, follow the steps below-

  * Open <project>/src/theme/light-theme-options.js file and set preferred primary colors for light themes.
  * In the same way open <project>/src/theme/dark-theme-options.js file and set preferred primary, accent and etc. colors for dark theme.



**TIP**

Recommended tutorial is below 👇

## **Change App Font**[**​**](https://docs.6amtech.com/docs-six-am-mart/react-web-app/customization#change-app-font) #

To change website font you have to go to <project>src/theme/base-theme-options.then line 299 fontFamily: ‘”Signika Negative”, “sans-serif”‘, replace fontFamily. Path: project/src/theme/base-theme-options Example :
    
    
    fontFamily:”your font family”

#### Share This Article :

  * [](https://www.facebook.com/sharer/sharer.php?u=)
  * [](https://twitter.com/intent/tweet?url=)
  * [](https://www.linkedin.com/shareArticle?mini=true&url=)
  * [](https://pinterest.com/pin/create/button/?url=)



[ Mandatory Setup (Web)]()[Site Build and Deploy ]()

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

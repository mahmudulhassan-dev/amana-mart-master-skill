Skip to content

6amMart Documentation

[ Installation ](/installation)

[ Customization ](/customization)

[ Any Question? ](https://wa.me/8801810494911?text=Hi%2C%20I%20want%20to%20chat%20about%206amMart.)

View Categories

Table of Contents

  * Run an existing react project on IDE​
  * Change Base URL
  * Add Google Map API Key​
  * Setup Firebase for Push Notification​
  * Social Logins​



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

## **Run an existing react project on IDE**[**​**](https://docs.6amtech.com/docs-six-am-mart/react-web-app/mandatory-setup#run-an-existing-react-project-on-ide) #

  * Run the purchased and downloaded NextJS project on your preferred IDE.
  * Before running the project in your local machine,
    * You have to set your **CodeCanyon username** and **purchased license key** in your admin panel.
    * You have to change your project .env.development and .env.production-> NEXT_PUBLIC_BASE_URL variables with your activated admin url as base url.



**TIP**

Recommended tutorial is below 👇

## **Change Base URL** #

[**​**](https://docs.6amtech.com/docs-six-am-mart/react-web-app/mandatory-setup#change-base-url)To change the base URL follow the steps given below –

Add NEXT_PUBLIC_BASE_URL variable in both env files. Then assign your URL as a variable value. For example:

  * Must remember that don’t put slash(/) at the end of your base url.
  * Use your admin url as base url.
  * First you have to install your admin panel. For example: If your admin url is https://your_domain.com/admin then base url will be https://your_domain.com .
  * Create .env.production and .env.development file in your project


    
    
    NEXT_PUBLIC_BASE_URL=”Your URL”
    
    
    NEXT_PUBLIC_BASE_URL=”Your URL”

## **Add Google Map API Key**[**​**](https://docs.6amtech.com/docs-six-am-mart/react-web-app/mandatory-setup#add-google-map-api-key) #

  * You need to generate the google API key. Visit this link- <https://developers.google.com/maps/documentation/embed/get-api-key>
  * You need to enabled mention APIs: Direction API, Distance Matrix API, Geocoding API, , Place API.
  * You have to enable billing account. Visit this url for activating: <https://support.google.com/googleapi/answer/6158867?hl=en>
  * After generating API key, you have to put it on your project .env file.
  * Open <project>.env.production and <project>.env.development and add your api key inside those files at NEXT_PUBLIC_GOOGLE_MAP_KEY. For example:


    
    
    NEXT_PUBLIC_GOOGLE_MAP_KEY = YOUR_MAP_API_KEY_HERE
    
    
    NEXT_PUBLIC_GOOGLE_MAP_KEY = YOUR_MAP_API_KEY_HERE

**TIP**

Recommended tutorial is below 👇

## **Setup Firebase for Push Notification**[**​**](https://docs.6amtech.com/docs-six-am-mart/react-web-app/mandatory-setup#setup-firebase-for-push-notification) #

**TIP**

Recommended tutorial is below 👇

## **Social Logins**[**​**](https://docs.6amtech.com/docs-six-am-mart/react-web-app/mandatory-setup#social-logins) #

For using social logins of Facebook and Google, you need to add app keys and secret keys.

Go to <project>/src/utils/staticCredential.js
    
    
    export const google_client_id="xxxxxxxxx";
    
    
    export const google_client_id="xxxxxxxxx";
    
    
    export const fb_app_id = "000-0000";
    
    
    export const fb_app_id = "000-0000";

Add your google client id and facebook app id there.

#### Share This Article :

  * [](https://www.facebook.com/sharer/sharer.php?u=)
  * [](https://twitter.com/intent/tweet?url=)
  * [](https://www.linkedin.com/shareArticle?mini=true&url=)
  * [](https://pinterest.com/pin/create/button/?url=)



[ Mandatory setup (Admin panel)]()[Customization Setup ]()

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

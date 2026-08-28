Skip to content

6amMart Documentation

[ Installation ](/installation)

[ Customization ](/customization)

[ Any Question? ](https://wa.me/8801810494911?text=Hi%2C%20I%20want%20to%20chat%20about%206amMart.)

View Categories

Table of Contents

  * Run an existing flutter project on IDE
  * Change App Logo​ and Icon
    * App Logo : 
    * App Icon : 
  * Change App Name​
  * Change Base URL​
  * Change App Package​
  * Setup Firebase for Push Notification​
    * Android Setup : 
    * IOS Setup : 
    * Admin Setup : 
  * Add Google Map API Key​



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

**Info**

Same documentation will be applicable for provider and serviceman app 

## **Run an existing flutter project on IDE** #

To begin, it’s essential to verify that your **Flutter** and **Integrated Development Environment (IDE)** setup has been configured accurately

  * Execute the command **flutter doctor** in your terminal. If any issues arise during this process, make sure to address and resolve them promptly.
  * Then open your project. Once the project is open, Android Studio may prompt you to install the dependencies. If not, you can run the **flutter pub get** from the terminal in the project directory to fetch the dependencies.
  * After the dependencies are installed, you should be able to run the app.



## **Change App Logo**[**​**](https://docs.6amtech.com/docs-demandium/mobile-apps/mandatory-setup#change-app-logo)**and Icon** #

To change **App logo** and **App Icon** you need to follow these steps :

### **App Logo :** #

  * Go to **< project>/assets/images/** and replace **logo.png** with your own logo.



**Note**

Please use the exact file name as described; otherwise, it will not work.

### **App Icon :** #

You can generate your app icon using this site [Visit](https://www.appicon.co)

  * Then go to **/android/app/src/main/res** and replace all mipmap folders with your **< generated icon>/android** folder.
  * Again go to**/ios/Runner/Assets.xcassets** and replace **Assets.xcassets** with your generated **Assets.xcassets** folder.



## **Change App Name**[**​**](https://docs.6amtech.com/docs-demandium/mobile-apps/mandatory-setup#change-app-logo) #

You need to set your app name in three different places.

  * Go to **< project>/lib/util/app_constrants.dart** and set the value of **appName**


    
    
     static const String appName = ‘YOUR_APP_NAME’;
    
    
    static const String appName = ‘YOUR_APP_NAME’;

  * Change the value of**label** from **< project>/android/app/src/main/AndroidManifest.xml**


    
    
    android:label="YOUR_APP_NAME"
    
    
    android:label="YOUR_APP_NAME"

  * Change the value of **CFBundleName** from **< project>/iOS/Runner/info.plist**


    
    
    <key>CFBundleDisplayName</key>
    <string>YOUR_APP_NAME</string>
    <key>CFBundleName</key>
    <string>YOUR_APP_NAME</string>
    
    
    <key>CFBundleDisplayName</key>
    <string>YOUR_APP_NAME</string>
    <key>CFBundleName</key>
    <string>YOUR_APP_NAME</string>

## **Change Base URL**[**​**](https://docs.6amtech.com/docs-demandium/mobile-apps/mandatory-setup#change-base-url) #

First you have to install your admin panel. For example: If your admin login url is **https://your_domain.com/admin/auth/login** then the base url will be <https://your_domain.com>

  * Open **< project>****/lib/util/app_constrants.dart** and replace **baseUrl** variable value with your own URL.



Ensure that **don’t put slash(/)** at the end of your base url like
    
    
    static const String baseUrl = 'https://your_domain.com/';  
    
    
    static const String baseUrl = 'https://your_domain.com/';  

Put your base url like that –
    
    
    static const String baseUrl = 'https://your_domain.com'; 
    
    
    static const String baseUrl = 'https://your_domain.com'; 

## **Change App Package**[**​**](https://docs.6amtech.com/docs-demandium/mobile-apps/mandatory-setup#change-app-package) #

First, you have to find out the existing package name. You can find it out from the top of the ****android/app/src/main/AndroidManifest.xml**** file. Now right-click on the project folder from Android Studio and click on replace in the path. You will get a popup window with two input boxes. In the first box, you have to put the existing package name that you saw in the **AndroidManifest.xml** file previously and write down your preferred package name in the second box and then click on the **Replace All** button.

## **Setup Firebase for Push Notification**[**​**](https://docs.6amtech.com/docs-demandium/mobile-apps/mandatory-setup#setup-firebase-for-push-notification) #

First, you have to change your package name. If you didn’t, then follow [this](https://docs.6amtech.com/docs-stack-food/mobile-apps/mandatory-setup#change-app-package). Then have to create a Firebase project from [https://console.firebase.google.com](https://console.firebase.google.com/)

**WARNING**

Do not create multiple projects on your firebase console, if you have multiple apps like User App or Web, Provider App and Serviceman App. Create only one project and add multiple apps under the project.

### **Android Setup :** #

  * Add an Android app under your firebase project with your own package name and app name.
  * Click the **register app** button and download the **google-services.json** file from there.
  * Copy that **google-services.json** file and go to your **< project>/android/app/** folder then delete the existing **google-services.json** file and paste the **google-services.json** file that you downloaded**.**
  * Create a totally white PNG logo for the notification icon. Paste it on **< project>/android/app/src/main/res/drawable/** and replace **notification_icon.png** with your whiter version logo. Must keep the icon name **notification_icon.png**
  * Go to **< project>/lib/main.dart** file, and find the **FirebaseOption** function, Change your firebase project’s
    * **apiKey:**
    * **appId:**
    * **messagingSenderId:**
    * **projectId:**



### **IOS Setup :** #

  * Again add an app under the same project and download **GoogleService-Info.plist** and paste it under **< project>/iOS/ folder**. Also, follow this documentation for full setup for IOS: <https://firebase.flutter.dev/docs/messaging/apple-integration>



Paste the Firebase **Service account** key in the admin panel Firebase Notification section. You can get the **Service account** key from Firebase **project settings- >Service accounts->Generate new private key**.

### **Admin Setup :** #

  * Again add and **web app** under the same project, and there you will find **firebaseConfigData** for setting up **admin firebase configuration** data.
  * For service file setup, follow: [**)



After your setup, please restart your IDE and uninstall your previously installed app then run it. Also, don’t try to test it on an emulator or simulator. Emulators and simulators are unable to get push. Use a real device in this case.

**WARNING**

Don’t forget to setup the admin firebase configuration <

## **Add Google Map API Key**[**​**](https://docs.6amtech.com/docs-demandium/mobile-apps/mandatory-setup#add-google-map-api-key) #

  * You need to generate the google API key. Visit this link – <https://developers.google.com/maps/documentation/embed/get-api-key>
  * You need to enable the mentioned APIs: Direction API, Distance Matrix API, Geocoding API, Maps SDK for Android, Maps SDK for iOS, Maps JavaScript API, Place API, Geolocation API, Routes API, Place API (New)
  * You have to enable a billing account. Visit this url for activating: <https://support.google.com/googleapi/answer/6158867?hl=en>
  * After generating the API key, you have to put it in 3 different places for Android, iOS and web.



**NOTE**

You must need to add Billing to your Google Console for using this map key.

**WARNING**

If your map key was generated before **March 1, 2025** , please make sure to newly enable the following APIs: **Routes API** and **Places API (New)**. All other settings can remain unchanged.

For android: open <project>/android/app/src/main/AndroidManifest.xml and place the value of com.google.android.geo.API_KEY

  * /android/app/src/main/AndroidManifest.xml


    
    
    <meta-data android:name="com.google.android.geo.API_KEY" android:value=“YOUR_MAP_API_KEY_HERE”/>
    
    
    <meta-data android:name="com.google.android.geo.API_KEY" android:value=“YOUR_MAP_API_KEY_HERE”/>

For iOS: open <project>/iOS/Runner/AppDelegate.swift and place the value of GMSServices.provideAPIKey

  * /iOS/Runner/AppDelegate.swift


    
    
    GMSServices.provideAPIKey(“YOUR_MAP_API_KEY_HERE")
    
    
    GMSServices.provideAPIKey(“YOUR_MAP_API_KEY_HERE")

For web: open <project>/web/index.html and place the value of https://maps.googleapis.com/maps/api/js?key

  * /web/index.html


    
    
    <script src="https://maps.googleapis.com/maps/api/js?key=YOUR_MAP_API_KEY_HERE"></script>
    
    
    <script src="https://maps.googleapis.com/maps/api/js?key=YOUR_MAP_API_KEY_HERE"></script>

#### Share This Article :

  * [](https://www.facebook.com/sharer/sharer.php?u=)
  * [](https://twitter.com/intent/tweet?url=)
  * [](https://www.linkedin.com/shareArticle?mini=true&url=)
  * [](https://pinterest.com/pin/create/button/?url=)



[ Environment Setup]()[Customisation ]()

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

Skip to content

6amMart Documentation

[ Installation ](/installation)

[ Customization ](/customization)

[ Any Question? ](https://wa.me/8801810494911?text=Hi%2C%20I%20want%20to%20chat%20about%206amMart.)

View Categories

Table of Contents

  * Google Login
    * Android Setup : 
    * iOS Setup :
    * Web Setup : 
  * Facebook Login
  * Apple Login
  * Firebase OTP Login



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

## **Google Login** #

If you want to enable your Google login then go to [https://console.firebase.google.com](https://console.firebase.google.com/) and find your project that you have already created for push notification setup then open your **Project- >Authentication->Sign-in method-> Add new Provider->Additional providers** then select **Google** and enable finlay Save.

### **Android Setup :** #

  * You need to set a fingerprint in firebase, go to **Project >Project settings > Android apps **then select your user app at the bottom you will find**add fingerprint** then enter your **SHA1** and **SHA256** and Save. Visit this site here you will get the instruction how you will get SHA1 and SHA256 [Link](https://developers.google.com/android/guides/client-auth)
  * After publishing on the play store you need to add your **SHA1** and **SHA256** form App integrity. To found App integrity App signing, go to google play console **Project- > Release > Setup > App integrity > App signing**
  * Download your **google-service.json** file and Copy that file and paste it under **< project>/android/app/** folder.
  * Go to your project’s **< project>/lib/util/app_constants.dart** file and add googleServerClientId


    
    
     static const String googleServerClientId = 'YOUR_CLIENT_ID';
    
    
     static const String googleServerClientId = 'YOUR_CLIENT_ID';

### **iOS Setup :** #

  * Go to your downloaded **GoogleService-Info.plist** file, there you’ll find **REVERSED_CLIENT_ID** , copy this.
  * Go to **< project>/ios/Runner/Info.plist **and add your Client ID


    
    
    dict>
       <key>CFBundleTypeRole</key>
       <string>Editor</string>
       <key>CFBundleURLSchemes</key>
       <array>
           <string>YOUR_REVERSED_CLIENT_ID</string>
       </array>
    </dict>
    
    
    dict>
       <key>CFBundleTypeRole</key>
       <string>Editor</string>
       <key>CFBundleURLSchemes</key>
       <array>
           <string>YOUR_REVERSED_CLIENT_ID</string>
       </array>
    </dict>

### **Web Setup :** #

  * Go to **< project>/web/index.html** and set your **CLIENT_ID**


    
    
     <meta name="google-signin-client_id" content="YOUR_CLIENT_ID">
    
    
    <meta name="google-signin-client_id" content="YOUR_CLIENT_ID">

  * Go to your <https://console.cloud.google.com/apis/credentials/oauthclient> then add your web app hosted **domain** in Authorized javascript origin section.
    * **APIs and Services - > Credentials -> OAuth 2.0 Client IDs **set your domain there. Like:_https://demo.com_
  * Go to your <https://console.cloud.google.com/apis/credentials/oauthclient> then, need to enable**People Api** , 
    * **APIs and Services - > People Api -> Enable**



## **Facebook Login** #

  * If you want to configure Facebook login in your project then create your own app form <https://developers.facebook.com/apps>
  * Configure your app settings from **App Settings- >Basic** with your own Display name, Contact email, Privacy Policy URL, Terms of Service URL, App icon, web app domain
  * Add Facebook Login form products section .
  * Add your platform (web/android/ios) with click Add platform and configure your app.
  * To Configuration settings in the app, Facebook Login->Settings->Client OAuth settings enable Client OAuth login, Web OAuth login, Enforce HTTPS, Use Strict Mode for redirect URIs, Login with the JavaScript SDK.
  * Also, you need to add your Allowed Domains for the JavaScript SDK (ex- [https://6ammart-web.6amtech.com](https://6ammart-web.6amtech.com/)) 
  * To get profile information you need to request access in **App Review- >Permissions and features** get access for **public_profile**
  * Now open your flutter project go to **< project>/lib/main.dart **and replace with your facebook appID
  * For android go to **< project>/android/app/src/main/res/values/string.xml **and set value.


    
    
    <resources>
      <string name="app_name">6amMart</string>
      <string name="facebook_app_id">YOUR_APP_ID</string>
      <string name="fb_login_protocol_scheme">fb_YOUR_APP_ID</string>
      <string name="facebook_client_token">Go_to_your_fb_app->Settings->Advance->Security->Client token</string>
    </resources>
    
    
    <resources>
      <string name="app_name">6amMart</string>
      <string name="facebook_app_id">YOUR_APP_ID</string>
      <string name="fb_login_protocol_scheme">fb_YOUR_APP_ID</string>
      <string name="facebook_client_token">Go_to_your_fb_app->Settings->Advance->Security->Client token</string>
    </resources>

  * For ios go to **ios/Runner/Info.plist** and set value


    
    
    <array>
       <dict>
           <key>CFBundleURLSchemes</key>
           <array>
             <string>fb_your_app_id</string>
           </array>
       </dict>
    <array>
    
    <key>FacebookAppID</key>
    <string>app_id</string>
    <key>FacebookClientToken</key>
    <string>
       Go_to_your_fb_app->Settings->Advance->Security->Client  token
    </string>
    <key>FacebookDisplayName</key>
    <string>name</string>
    
    
    
    <array>
       <dict>
           <key>CFBundleURLSchemes</key>
           <array>
             <string>fb_your_app_id</string>
           </array>
       </dict>
    <array>
    
    <key>FacebookAppID</key>
    <string>app_id</string>
    <key>FacebookClientToken</key>
    <string>
       Go_to_your_fb_app->Settings->Advance->Security->Client  token
    </string>
    <key>FacebookDisplayName</key>
    <string>name</string>
    

  * For the web go to **< project>/lib/main.dart** set your appID.


    
    
    await FacebookAuth.instance.webAndDesktopInitialize(
    appId: "YOUR_FB_APP_ID",
       cookie: true,
       xfbml: true,
       version: "v15.0",
    );
    
    
    
    await FacebookAuth.instance.webAndDesktopInitialize(
    appId: "YOUR_FB_APP_ID",
       cookie: true,
       xfbml: true,
       version: "v15.0",
    );
    

## **Apple Login** #

To configure Apple Login follow the steps mentioned below –

**Step 1: Find out Team ID**

  * Visit the [Apple Developer page](https://developer.apple.com/).
  * Go to **Account** and find the **Membership details** section. There you will find **TeamID**.



Step 2: Create or Use App ID

**INFO**

If you already have an App ID that you want to use for Apple Sign-In, you can skip creating a new one and proceed to the next step.

  * Go to the Identifiers list.
  * Click the Plus icon besides **Identifiers** , and then select **App IDs** and continue
  * Select type **App** and continue.
  * Provide a brief description and a **Bundle ID** (the same one used for your app). This identifier will serve as the **Client ID** for Apple Sign-In.
  * In Capabilities, select the required options like **Push Notifications** ,**Sign In with Apple** , and**Associated Domains**.
  * Click **Continue** and proceed.



**Step 3: Create Service ID**

  * Go again to the Identifiers list.
  * Click the Plus icon beside**Identifiers** , and then select **Service IDs** and continue
  * Add a **description** and an**identifier** for your service, then click **Continue**
  * Download the file labeled as **AuthKey_example.p8**. This is the**Service File** , and the segment “example” within the file name is indicative of the **KeyID**. To illustrate, if your file is titled **AuthKey_XXXXXXXXXX.p8** , then **XXXXXXXXXX** signifies the**KeyID**.
  * If you are using the web, then add the web URL in the **Sign In with Apple**. Configure this by following- 
    * Click **configure** then add Website URLs, in domain and Subdomains section add your website url without **https://** and **parrams**. And on Return URLs section, add your website url. Then click **Next > Continue> Save.**



**Step 4: Submit Data in the Admin Panel**

  * Go to the **Admin panel.**
  * Navigate to **Configurations > 3rd Party > Apple Login** setup your data.
  * Use the following information:
    * **Client ID for web:** Service ID’s identifier you previously specified.
    * **Client ID for App:** The Bundle ID you previously specified.
    * **Team ID:** Obtained from the Apple Developer page.
    * **Key ID:** KeyID from the AuthKey_example.p8 file name.
    * **Redirect url for flutter web** : Your flutter web app’s url link.
    * **Redirect url for react web** : Your react website url link.
    * **Service File:** Downloaded AuthKey_example.p8 file. [Must ensure your setup key id is similar with that file],
  * Save and enable Apple Login status.



By following these steps, you can successfully set up and implement Apple Sign-In in your Project.

## **Firebase OTP Login** #

For configuring OTP in the Firebase, you must create a Firebase project first. If you haven’t created any project for your application yet, please follow the instructions given [here]().

Now go the [Firebase console](https://console.firebase.google.com/) and follow the instructions below-

**Adding sign-in method**[**​**](https://docs.6amtech.com/docs-grofresh/third-party#adding-sign-in-method)

  * Go to your Firebase project.
  * Navigate to the **Build** menu from the left sidebar and select **Authentication**.
  * Get started on the project and go to the **Sign-in method** tab.
  * From the **Sign-in Providers** section, select the **Phone** option.
  * Ensure to enable the method **Phone** and press **save**



**Admin Panel Configuration**[**​**](https://docs.6amtech.com/docs-grofresh/third-party#admin-panel-configuration)

To configure the Admin panel for Firebase OTP verification, follow these steps:

  * Go to your Firebase project, In the Project settings, locate your **Web API Key** and make a copy of it.
  * Go to the Admin panel and navigate **Settings > 3rd Party > Firebase OTP Verification **.
  * Paste the **Web API Key** copied from your Firebase project.
  * Turn on the Firebase OTP Verification Status.
  * Turn on the Customer Verification option from **Settings > View all > Login setup > Verification.**



**Web Configuration**[**​**](https://docs.6amtech.com/docs-grofresh/third-party#web-configuration)

To configure your web domain for Firebase OTP verification:

  * Go to your Firebase project.
  * Navigate to the Build menu from the left sidebar and select **Authentication**.
  * Go to the Settings tab.
  * Under the Authorized Domains section, add your web domain without specifying “http” or “https.” **(for example: example.com)**.



**App Configuration**[​](https://docs.6amtech.com/docs-grofresh/third-party#app-configuration)

To configure the app, follow the steps below-

  * Go to the firebase console **Your Project > Project settings > General > Your apps.**
  * Download **google-services.json** file for android and **GoogleService-Info.plist** for IOS app.
  * Copy that file and paste it under **< project>/android/app/** folder for android and under **< project>/iOS/** for IOS.
  * Select your app at the bottom you will find an add fingerprint option then enter your **SHA1** and **SHA256** and Save. Visit this site here you will get the instruction on how you will get SHA1 and SHA256 [Link](https://developers.google.com/android/guides/client-auth)
  * Go to your downloaded **GoogleService-Info.plist** file, there you’ll find **REVERSED_CLIENT_ID** , copy this then go to **< project>/ios/Runner/Info.plist **and add your copied **REVERSED_CLIENT_ID**


    
    
     <dict>
       <key>CFBundleTypeRole</key>
       <string>Editor</string>
       <key>CFBundleURLSchemes</key>
       <array>
           <string>YOUR_REVERSED_CLIENT_ID</string>
       </array>
    </dict>
    
    
    <dict>
       <key>CFBundleTypeRole</key>
       <string>Editor</string>
       <key>CFBundleURLSchemes</key>
       <array>
           <string>YOUR_REVERSED_CLIENT_ID</string>
       </array>
    </dict>

**Note:**

Firebase billing must be enabled for using this feature. Need to use Blaze Plane for this

#### Share This Article :

  * [](https://www.facebook.com/sharer/sharer.php?u=)
  * [](https://twitter.com/intent/tweet?url=)
  * [](https://www.linkedin.com/shareArticle?mini=true&url=)
  * [](https://pinterest.com/pin/create/button/?url=)



[ App Build & Release]()[System Update ]()

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

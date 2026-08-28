Skip to content

6amMart Documentation

[ Installation ](/installation)

[ Customization ](/customization)

[ Any Question? ](https://wa.me/8801810494911?text=Hi%2C%20I%20want%20to%20chat%20about%206amMart.)

View Categories

Table of Contents

  * Map Configuration [SS]
  * Business Setup
  * Mail Configuration 
  * Firebase Configuration (for notification)
  * Payment Configuration 
  * SMS Module Configuration 
  * Configure Environment Variables 



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

## **Map Configuration [SS]** #

Client should buy Map API from Google for enabling the maps into the panels. Without buying those APIs clients cannot load Google maps into the panels for selecting zones. For generating map api key you can watch this video. Now go to your admin panel then “Third party APIs” menu, here you will find two inputs for map api key client and map api key server. You can restrict the client with admin panel domain and the server key with your server ip address. If you don’t want any restriction then you can use single api key for both field.

**TIP**

Recommended tutorial is below 👇

## **Business Setup** #

In the admin panel we have a menu called Business Setup where you can set your logo, timezone, country, time format, location, currency and many more things.

## **Mail Configuration** #

  * Mail Configurations part admin can set his Mailer name, host, driver, user name, Email ID and his own encryption method and password for this SMTP Mail setup. This configuration is used for sending password recovery mail for the store.



## **Firebase Configuration (for notification)** #

The Firebase Push Notification will send messages for general notifications, chatting notification, order place notification and every order status notification. To set up firebase notification go to admin panel 3rd Party & Configuration > Firebase Notification > Firebase Configuration.

  * Go to <https://console.firebase.google.com/>
  * If you don’t have a project, create one.
  * Click on the settings icon from left sidebar (beside Project Overview) & Go to Project Settings.
  * From the Project Settings, go to Service Accounts tab.
  * Click on Generate new private Key to generate the key. It will automatically download a .json file.
  * Open the file with any text editor, copy the contents in it, and add those to Service File Content in 3rd Party > Push Notification > Firebase Configuration in admin panel.



**Tip**

Recommended tutorial is below 👇

The Firebase Push Notification will send messages for every order status. If the admin turns on the status then with order status change customers, restaurant, delivery man will get status notification and if he turned off that then no one will get that message. To set up firebase notification go to the admin panel Notification Settings menu.

Before that download the JavaScript file firebase-messaging-sw.js from this following link: <https://drive.google.com/file/d/1C4TpwYD6P5kkd8FA7xC333lXv10pO3hz/view?usp=sharing>

In the JavaScript file “firebase-messaging-sw.js” replace your firebase credential ( apiKey, authDomain, projectId, storageBucket, messagingSenderId, appId ):
    
    
    firebase.initializeApp({
    
        apiKey: "YOUR_API_KEY",
    
        authDomain: "YOUR_AUTH_DOMAIN",
    
        projectId: "YOUR_PROJECT_ID",
    
        storageBucket: "YOUR_STORAGE_BUCKET",
    
        messagingSenderId: "YOUR_MESSAGING_SENDER_ID",
    
        appId: "YOUR_APP_ID",
    
        databaseURL: "...",
    
    });
    
    
    firebase.initializeApp({
    
        apiKey: "YOUR_API_KEY",
    
        authDomain: "YOUR_AUTH_DOMAIN",
    
        projectId: "YOUR_PROJECT_ID",
    
        storageBucket: "YOUR_STORAGE_BUCKET",
    
        messagingSenderId: "YOUR_MESSAGING_SENDER_ID",
    
        appId: "YOUR_APP_ID",
    
        databaseURL: "...",
    
    });

## **Payment Configuration** #

In this part Admin will introduced with the payment gateways. Cash on delivery, Digital Payment like SSLCOMMERZ, Razor pay, Paypal, Stripe, Paystack, Senang Pay, Flutterwave, MercadoPago, Payment accept are available for payment gateways. He can make the necessary setup of making the status active and inactive of those payment gateways as well.

## **SMS Module Configuration** #

SMS Module is used for SMS Gateways for OTP sending in the simplest way of user verification. Customer will get OTP when they create their own account and for password recovery.

## **Configure Environment Variables** #

Ensure the following environment variables are present in your project’s .env file. Add them if they do not already exist.
    
    
    APP_HOST_DOMAIN=admin.example.com
    
    APP_HOST_BASE_DOMAIN=example.com
    
    APP_PUBLIC_IP=127.0.0.1
    
    
    APP_HOST_DOMAIN=admin.example.com
    
    APP_HOST_BASE_DOMAIN=example.com
    
    APP_PUBLIC_IP=127.0.0.1
    
    
    APP_HOST_DOMAIN: The primary domain where your application is hosted.
    
    APP_HOST_BASE_DOMAIN: The base domain.
    
    APP_PUBLIC_IP: The public IP address of your server.
    
    
    APP_HOST_DOMAIN: The primary domain where your application is hosted.
    
    APP_HOST_BASE_DOMAIN: The base domain.
    
    APP_PUBLIC_IP: The public IP address of your server.

**Note**

Replace the example values with your actual production domain and public server IP.

#### Share This Article :

  * [](https://www.facebook.com/sharer/sharer.php?u=)
  * [](https://twitter.com/intent/tweet?url=)
  * [](https://www.linkedin.com/shareArticle?mini=true&url=)
  * [](https://pinterest.com/pin/create/button/?url=)



[ Installation]()[Customizations ]()

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

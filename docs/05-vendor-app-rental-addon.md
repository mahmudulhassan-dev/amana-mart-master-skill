# Vendor App Rental Module Integration

**Official Section Reference:** 6amMart Documentation

---

Skip to content

6amMart Documentation

[ ![6amMart Installation](https://6ammart.app/wp-content/uploads/2025/08/6ammart-installation.svg)Installation ](/installation)

[ ![6amMart Customization](https://6ammart.app/wp-content/uploads/2025/08/6ammart-customization.svg)Customization ](/customization)

[ ![6amMart Question](https://6ammart.app/wp-content/uploads/2025/08/6ammart-question.svg)Any Question? ](https://wa.me/8801810494911?text=Hi%2C%20I%20want%20to%20chat%20about%206amMart.)

View Categories

Table of Contents

  * Setting Up the Rental Module in the Vendor App
  * Version Update – Rental Module 



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

**Note**

For Rental Module , You need to use minimum code version 3.0

## **Setting Up the Rental Module in the Vendor App** #

  1. **Download the Required Files:**


  * Get the Vendor app (without the rental module) from CodeCanyon and open it in your IDE.
  * Download the rental module code from CodeCanyon.


  2. **Remove the Existing Taxi Module:**


  * Navigate to: lib/features/taxi_module
  * Delete the taxi_module folder (it contains no code).


  3. **Run the following commands in your terminal:**


    
    
     flutter pub cache clean
    
    flutter clean
    
    
    flutter pub cache clean
    
    flutter clean

  4. **Add the Rental Module:**


  * Extract the downloaded rental module ZIP file.
  * Place the extracted taxi_module folder inside the features directory.


  5. **Then Run the following commands in your terminal:**


    
    
     flutter pub get
    
    
    flutter pub get

  6. **Your rental module is now set up and ready to use!**



## **Version Update – Rental Module** #

**Note**

This update applies only to existing users of the Rental Module.

If you want to upgrade your **Rental Module** to the **latest version** , follow one of the two methods below:

  1. **Update by Changed Files**
     * Locate the update folder named like:****App changes from V1.0 to V1.1****
     * Inside this folder, you will find files **organized directory-wise**.
     * Simply **replace the old files** in your project with the corresponding updated files in those directories
  2. **Full Module Replacement**
     * **If you prefer, you can replace the entire Rental Module code with the latest version provided.**



**Warning**

You can not switch from very older version to newer version. You can switch from previous version to new version

#### Share This Article :

  * [![Facebook](https://6ammart.app/wp-content/plugins/betterdocs/assets/static/images/social/facebook.svg?v=4.8.1)](https://www.facebook.com/sharer/sharer.php?u=https://6ammart.app/documentation/vendor-application-configuration/vendor-app-rental-module-addon/)
  * [![X](https://6ammart.app/wp-content/plugins/betterdocs/assets/static/images/social/twitter.svg?v=4.8.1)](https://twitter.com/intent/tweet?url=https://6ammart.app/documentation/vendor-application-configuration/vendor-app-rental-module-addon/)
  * [![LinkedIn](https://6ammart.app/wp-content/plugins/betterdocs/assets/static/images/social/linkedin.svg?v=4.8.1)](https://www.linkedin.com/shareArticle?mini=true&url=https://6ammart.app/documentation/vendor-application-configuration/vendor-app-rental-module-addon/)
  * [![Pinterest](https://6ammart.app/wp-content/plugins/betterdocs/assets/static/images/social/pinterest.svg?v=4.8.1)](https://pinterest.com/pin/create/button/?url=https://6ammart.app/documentation/vendor-application-configuration/vendor-app-rental-module-addon/)



 System UpdatePrerequisites 

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

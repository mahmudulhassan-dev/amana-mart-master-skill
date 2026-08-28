# Customer App System & Version Update

**Official Section Reference:** 6amMart Documentation

---

Skip to content

6amMart Documentation

[ ![6amMart Installation](https://6ammart.app/wp-content/uploads/2025/08/6ammart-installation.svg)Installation ](/installation)

[ ![6amMart Customization](https://6ammart.app/wp-content/uploads/2025/08/6ammart-customization.svg)Customization ](/customization)

[ ![6amMart Question](https://6ammart.app/wp-content/uploads/2025/08/6ammart-question.svg)Any Question? ](https://wa.me/8801810494911?text=Hi%2C%20I%20want%20to%20chat%20about%206amMart.)

View Categories

Table of Contents

  * Safely Live system update



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

## **Safely Live system update** #

Suppose your system’s current version is V 2.0, now you want to update your system to V2.1 and also want to force users to update the system then you can follow this to update your system safely. 

  * Generate your appbundle for PlayStore and ipa for AppStore using your update version’s code, in this case V 2.1. And must add this version on your project’s 



**lib/util/app_constants.dart** file-
    
    
    static const double appVersion = 2.1';  

It’ll maintain your app force update.

  * Update your app on both AppStore and PlayStore.


  * After successfully updating on AppStore and PlayStore – go to your**Admin Panel > Configurations > Third Party > App Settings** and set app minimum version, in this case V 2.1.



**Note**

Only friction or double value will be added in the app version. So if your release version is 2.1.1, then add app version 2.2. Which is maintained for force update. In admin, there must be added the app version 2.2 .

#### Share This Article :

  * [![Facebook](https://6ammart.app/wp-content/plugins/betterdocs/assets/static/images/social/facebook.svg?v=4.8.1)](https://www.facebook.com/sharer/sharer.php?u=https://6ammart.app/documentation/user-application-configuration/system-update/)
  * [![X](https://6ammart.app/wp-content/plugins/betterdocs/assets/static/images/social/twitter.svg?v=4.8.1)](https://twitter.com/intent/tweet?url=https://6ammart.app/documentation/user-application-configuration/system-update/)
  * [![LinkedIn](https://6ammart.app/wp-content/plugins/betterdocs/assets/static/images/social/linkedin.svg?v=4.8.1)](https://www.linkedin.com/shareArticle?mini=true&url=https://6ammart.app/documentation/user-application-configuration/system-update/)
  * [![Pinterest](https://6ammart.app/wp-content/plugins/betterdocs/assets/static/images/social/pinterest.svg?v=4.8.1)](https://pinterest.com/pin/create/button/?url=https://6ammart.app/documentation/user-application-configuration/system-update/)



 3rd Party SetupRental Module addon 

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

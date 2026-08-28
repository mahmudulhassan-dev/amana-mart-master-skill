# Admin Panel 3rd Party Integrations

**Official Section Reference:** 6amMart Documentation

---

Skip to content

6amMart Documentation

[ ![6amMart Installation](https://6ammart.app/wp-content/uploads/2025/08/6ammart-installation.svg)Installation ](/installation)

[ ![6amMart Customization](https://6ammart.app/wp-content/uploads/2025/08/6ammart-customization.svg)Customization ](/customization)

[ ![6amMart Question](https://6ammart.app/wp-content/uploads/2025/08/6ammart-question.svg)Any Question? ](https://wa.me/8801810494911?text=Hi%2C%20I%20want%20to%20chat%20about%206amMart.)

View Categories

Table of Contents

  * Configure Laravel Reverb
    * 1\. Environment Configuration (.env)
    * 2\. Starting the Reverb Server
    * 3\. Deployment & Process Management
    * Configuration in Admin Panel​



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

## Configure Laravel Reverb #

This guide explains how to configure and deploy the Laravel Reverb server, which replaces the legacy laravel-websockets package for real-time event broadcasting.

### **1\. Environment Configuration (.env)** #

To enable Reverb as your broadcasting driver, update your .env file with the following variables:

Required Reverb Variables:
    
    
    BROADCAST_DRIVER = reverb – Enables Reverb broadcasting.
    REVERB_APP_ID = 6ammart – Your Reverb Application ID.
    REVERB_APP_KEY = 6ammart – Public App Key.
    REVERB_APP_SECRET = 6ammart – Private App Secret.
    REVERB_HOST = host_name – Host/IP for Reverb.
    REVERB_PORT = 6001 – Default WebSocket port.
    REVERB_SCHEME = http – Use https behind SSL proxy.
    Client-Side Pusher Compatibility:
    PUSHER_APP_ID = 6ammart
    PUSHER_APP_KEY = 6ammart
    PUSHER_HOST = host_name
    PUSHER_PORT = 6001
    PUSHER_SCHEME = http
    PUSHER_APP_CLUSTER = mt1
    
    
    BROADCAST_DRIVER = reverb – Enables Reverb broadcasting.
    REVERB_APP_ID = 6ammart – Your Reverb Application ID.
    REVERB_APP_KEY = 6ammart – Public App Key.
    REVERB_APP_SECRET = 6ammart – Private App Secret.
    REVERB_HOST = host_name – Host/IP for Reverb.
    REVERB_PORT = 6001 – Default WebSocket port.
    REVERB_SCHEME = http – Use https behind SSL proxy.
    Client-Side Pusher Compatibility:
    PUSHER_APP_ID = 6ammart
    PUSHER_APP_KEY = 6ammart
    PUSHER_HOST = host_name
    PUSHER_PORT = 6001
    PUSHER_SCHEME = http
    PUSHER_APP_CLUSTER = mt1

### **2\. Starting the Reverb Server** #
    
    
    php artisan reverb:start
    
    
    php artisan reverb:start

### **3\. Deployment & Process Management** #

Use Supervisor to keep Reverb and Queue Worker running.

Supervisor Installation:
    
    
    sudo apt install supervisor
    sudo yum install supervisor
    
    
    sudo apt install supervisor
    sudo yum install supervisor

Supervisor Configuration (reverb.conf):
    
    
    [program:reverb]
    command=/usr/bin/php /home/laravel-echo/laravel-websockets/artisan reverb:start
    autostart=true
    autorestart=true
    [program:queue-worker]
    command=/usr/bin/php /home/laravel-echo/laravel-websockets/artisan queue:work --tries=3 --daemon
    autostart=true
    autorestart=true
    
    
    [program:reverb]
    command=/usr/bin/php /home/laravel-echo/laravel-websockets/artisan reverb:start
    autostart=true
    autorestart=true
    [program:queue-worker]
    command=/usr/bin/php /home/laravel-echo/laravel-websockets/artisan queue:work --tries=3 --daemon
    autostart=true
    autorestart=true

Activate:
    
    
    sudo supervisorctl update
    sudo supervisorctl start reverb
    sudo supervisorctl start queue-worker
    Increase File Descriptors:
    minfds=10240
    
    
    sudo supervisorctl update
    sudo supervisorctl start reverb
    sudo supervisorctl start queue-worker
    Increase File Descriptors:
    minfds=10240

### **Configuration in Admin Panel**[**​**](https://docs.6amtech.com/docs-six-am-mart/third-party/#configuration-in-admin-panel) #

After configuring all the settings above, turn on the Websocket and update the Websocket URL and Websocket Port.

![6amMart Doc Admin 3rd-Party System Configuration SS](https://6ammart.app/wp-content/uploads/2024/06/6ammart-doc-admin-3rd-party-system-configuration-ss-1024x508.webp)

#### Share This Article :

  * [![Facebook](https://6ammart.app/wp-content/plugins/betterdocs/assets/static/images/social/facebook.svg?v=4.8.1)](https://www.facebook.com/sharer/sharer.php?u=https://6ammart.app/documentation/admin-application-configuration/3rd-party-setup/)
  * [![X](https://6ammart.app/wp-content/plugins/betterdocs/assets/static/images/social/twitter.svg?v=4.8.1)](https://twitter.com/intent/tweet?url=https://6ammart.app/documentation/admin-application-configuration/3rd-party-setup/)
  * [![LinkedIn](https://6ammart.app/wp-content/plugins/betterdocs/assets/static/images/social/linkedin.svg?v=4.8.1)](https://www.linkedin.com/shareArticle?mini=true&url=https://6ammart.app/documentation/admin-application-configuration/3rd-party-setup/)
  * [![Pinterest](https://6ammart.app/wp-content/plugins/betterdocs/assets/static/images/social/pinterest.svg?v=4.8.1)](https://pinterest.com/pin/create/button/?url=https://6ammart.app/documentation/admin-application-configuration/3rd-party-setup/)



 CustomizationsRental Module addon 

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

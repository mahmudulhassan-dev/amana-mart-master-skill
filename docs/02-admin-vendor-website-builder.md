Skip to content

6amMart Documentation

[ Installation ](/installation)

[ Customization ](/customization)

[ Any Question? ](https://wa.me/8801810494911?text=Hi%2C%20I%20want%20to%20chat%20about%206amMart.)

View Categories

Table of Contents

  * Download the Vendor Website Builder Add-on
  * Upload the Add-on
  * Activate the Add-on
  * Enable the Website Builder Feature
    * Admin Configuration
    * Vendor Configuration
  * Configure Wildcard Subdomain (Mandatory)
  * Configure Custom Domain



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

### **Download the Vendor Website Builder Add-on** #

Purchase and download the **Vendor Website Builder** add-on from the **6amTech Store**. After purchasing, you will receive a ZIP file containing the add-on files.

### **Upload the Add-on** #

  1. Log in to your **Admin Panel**.
  2. Navigate to **Business Settings**.
  3. Scroll down the sidebar and select **System Add-ons**.
  4. Upload the downloaded **Vendor Website Builder** ZIP file.



### **Activate the Add-on** #

After the upload is completed successfully, click **Activate** to enable the Vendor Website Builder features.

**Important**

After activating the add-on, the Website Builder feature is disabled by default. You must enable it from the admin panel before vendors can use it.

### **Enable the Website Builder Feature** #

#### **Admin Configuration** #

  1. Go to **Business Settings**.
  2. Locate the **Vendor Website Builder** option.
  3. Enable the **Website Builder** status.



#### **Vendor Configuration** #

After the admin enables the feature, each vendor who wants to use the Website Builder must also enable it:

  1. Log in to the **Vendor Panel**.
  2. Go to **Store Config**.
  3. Enable the **Website Builder** option.



Once both the **Admin** and the **Vendor** have enabled the feature, the Website Builder option will become available to the vendor.

### **Configure Wildcard Subdomain (Mandatory)** #

**This step is mandatory.** The Vendor Website Builder requires a wildcard subdomain configuration so vendors can create and access their websites using subdomains.

  1. Create a **Wildcard DNS A Record** for your base domain.
     * **Host:** *
     *  **Type:** A
     * **Value:** Your server’s public IP address
  2. Ensure your web server (Apache/Nginx) is configured to accept wildcard subdomains.



After the wildcard DNS is configured, vendors can use any available subdomain under your primary domain without requiring additional DNS records.

**Example**

  * Base Domain: example.com
  * Vendor Websites:
    * vendor1.example.com
    * restaurant.example.com
    * mystore.example.com



**Note**

Without the wildcard subdomain configuration, vendors will not be able to create or access their websites.

### **Configure Custom Domain** #

If vendors want to use their own custom domain instead of a subdomain:

  1. Share your **server’s public IP address** with the vendor.
  2. Ask the vendor to point their domain’s **A Record** to your server’s public IP address.
  3. Once DNS propagation is complete, the vendor can connect the custom domain from the Website Builder settings.



**Example**

  * Vendor Domain: www.myshop.com
  * DNS Record:
    * **Type:** A
    * **Host:** @
    * **Value:** Your server’s public IP address



**Note**

DNS propagation may take up to **24–48 hours** , although it is often completed much sooner.

#### Share This Article :

  * [](https://www.facebook.com/sharer/sharer.php?u=)
  * [](https://twitter.com/intent/tweet?url=)
  * [](https://www.linkedin.com/shareArticle?mini=true&url=)
  * [](https://pinterest.com/pin/create/button/?url=)



[ Rental Module addon]()[Prerequisite ]()

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

# Vendor App Environment Setup

**Official Section Reference:** 6amMart Documentation

---

Skip to content

6amMart Documentation

[ ![6amMart Installation](https://6ammart.app/wp-content/uploads/2025/08/6ammart-installation.svg)Installation ](/installation)

[ ![6amMart Customization](https://6ammart.app/wp-content/uploads/2025/08/6ammart-customization.svg)Customization ](/customization)

[ ![6amMart Question](https://6ammart.app/wp-content/uploads/2025/08/6ammart-question.svg)Any Question? ](https://wa.me/8801810494911?text=Hi%2C%20I%20want%20to%20chat%20about%206amMart.)

View Categories

Table of Contents

  * Windows 
    * Install Android Studio
    * Install Flutter SDK
  * Linux 
    * Install Android Studio
    * Install Flutter SDK:
  * Mac
    * Install Android Studio
    * Install Flutter SDK



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

## **Windows** #

### **Install Android Studio** #

  * Download Android Studio
    * Visit the [official Android Studio download page and download](https://developer.android.com/studio?gclid=CjwKCAiAiKuOBhBQEiwAId_sK4X0PLQrES_2pG_S8nPflALgWSOCUEqRRAFpbS4AmR5mXmU6hIhvHxoCfBgQAvD_BwE&gclsrc=aw.ds) the latest version for Windows.
  * Run the Installer
    * Run the downloaded installer executable **(e.g., android-studio-ide- <version>-windows.exe).**
  * Follow Installation Wizard
    * Follow the instructions in the installation wizard.
    * Choose a custom installation location if needed.
    * Select the components you want to install (Android Studio, Android Virtual Device, etc.).
  * Start Android Studio
    * Once the installation is complete, launch Android Studio.
  * Install SDK Components
    * Android Studio will prompt you to install additional SDK components and tools. Allow it to download and install them.
  * Set up Emulator (Optional)
    * If you plan to use an emulator, you can create one through the AVD (Android Virtual Device) Manager in Android Studio.



### **Install Flutter SDK** #

  * Download Flutter SDK
  * Visit the [official Flutter download page for the latest version](https://docs.flutter.dev/get-started/install/windows) for Windows.
  * Extract Flutter Archive
  * Extract the downloaded Flutter zip file to a location on your machine. For example, **‘C:\flutter’**.
  * Add Flutter to System Path:
    * Add the **flutter\bin** directory to your system’s PATH variable.
      * Right-click on “This PC” or “Computer” on your desktop or in File Explorer.
      * Select “Properties” -> “Advanced system settings” -> “Environment Variables.”
      * In the “System variables” section, find and select the “Path” variable, then click “Edit.”
      * Click “New” and add the path to the **bin** directory inside the Flutter directory.
  * Verify Flutter Installation
    * Open a new Command Prompt and run **`flutter doctor`** to check for any dependencies that need to be installed or configured.
  * Install Flutter Plugins for Android Studio
    * Open Android Studio.
    * Install the Flutter and Dart plugins through “File” -> “Settings” -> “Plugins” -> “Marketplace.”
  * Restart Android Studio
    * Restart Android Studio to apply the changes.



## **Linux** #

### **Install Android Studio** #

  * Download Android Studio
    * Visit the [official Android Studio download page and download](https://developer.android.com/studio?gclid=CjwKCAiAiKuOBhBQEiwAId_sK4X0PLQrES_2pG_S8nPflALgWSOCUEqRRAFpbS4AmR5mXmU6hIhvHxoCfBgQAvD_BwE&gclsrc=aw.ds) the latest version for Linux.
  * Extract the Archive
    * Open a terminal and navigate to the directory where the archive was downloaded.
    * Extract the archive using the following command `tar -xvzf android-studio-ide-<version>-linux.tar.gz `(replace **android-studio-ide- <version>-linux.tar.gz** with the actual filename)
  * Move to Installation Location
    * Move the extracted folder to a location of your choice. For example: `sudo mv android-studio /YOUR_DIRECTORY`
  * Run Android Studio Setup
    * Navigate to the bin directory inside the Android Studio folder: `cd /YOUR_DIRECTORY/android-studio/bin`
    * Run ‘**./studio.sh’** to start the Android Studio setup
  * Follow Installation Wizard
    * Follow the instructions in the setup wizard to complete the installation.
    * Choose a custom installation location if needed.



### **Install Flutter SDK:** #

  * Download Flutter SDK
    * Visit the [official Flutter download page and download](https://docs.flutter.dev/get-started/install/linux) the latest stable version for Linux.
  * Extract Flutter Archive
    * Open a terminal and navigate to the directory where the archive was downloaded.
    * Extract the archive using the following command `tar xf flutter_linux_<version>.tar.xz` (replace**flutter_linux_ <version>.tar.xz** with the actual filename)
  * Move to Installation Location
    * Move the extracted folder to a location of your choice. For example: `sudo mv flutter /YOUR_DIRECTORY`
  * Add Flutter to System Path
    * Add the **flutter/bin** directory to your system’s PATH variable.
  * Verify Flutter Installation
    * Open a new terminal and run: `flutter doctor`
  * Install Flutter Plugins for Android Studio
    * Open Android Studio.
    * Install the Flutter and Dart plugins through “File” -> “Settings” -> “Plugins” -> “Marketplace.”
  * Install Flutter Plugins for Android Studio
    * Open Android Studio.
    * Install the Flutter and Dart plugins through “File” -> “Settings” -> “Plugins” -> “Marketplace.”
  * Restart Android Studio
    * Restart Android Studio to apply the changes.



## **Mac** #

### **Install Android Studio** #

  * Download Android Studio
    * Visit the [official Android Studio download page and download](https://developer.android.com/studio?gclid=CjwKCAiAiKuOBhBQEiwAId_sK4X0PLQrES_2pG_S8nPflALgWSOCUEqRRAFpbS4AmR5mXmU6hIhvHxoCfBgQAvD_BwE&gclsrc=aw.ds) the latest version for macOS.
  * Open the DMG file
    * Open the downloaded DMG file.
    * Drag and drop Android Studio into the “Applications” folder.
  * Run Android Studio
    * Open the “Applications” folder and launch Android Studio.
  * Set up Android Studio
    * Complete the Android Studio Setup Wizard.
    * Android Studio may prompt you to install additional components and SDKs. Follow the instructions to install them.



### **Install Flutter SDK** #

  * Download Flutter SDK
    * Visit the [official Flutter download page and download](https://docs.flutter.dev/get-started/install/macos) the latest stable version for macOS.
  * Extract Flutter Archive
    * Open a terminal and navigate to the directory where the archive was downloaded.
    * Extract the archive using the following command `tar xf flutter_macos_<version>.tar.xz` (replace**flutter_macos_ <version>.tar.xz** with the actual filename)
  * Move to Installation Location
    * Move the extracted folder to a location of your choice. For example : `sudo mv flutter /YOUR_DIRECTORY`
  * Add Flutter to System Path
    * Add the flutter/bin directory to your system’s PATH variable.
  * Verify Flutter Installation
    * Open a new terminal and run: `flutter doctor`
  * Install Flutter Plugins for Android Studio
    * Open Android Studio.
    * Install the Flutter and Dart plugins through “Preferences” -> “Plugins” -> “Marketplace.”
  * Restart Android Studio
    * Restart Android Studio to apply the changes.



#### Share This Article :

  * [![Facebook](https://6ammart.app/wp-content/plugins/betterdocs/assets/static/images/social/facebook.svg?v=4.8.1)](https://www.facebook.com/sharer/sharer.php?u=https://6ammart.app/documentation/vendor-application-configuration/vendor-app-environment-setup/)
  * [![X](https://6ammart.app/wp-content/plugins/betterdocs/assets/static/images/social/twitter.svg?v=4.8.1)](https://twitter.com/intent/tweet?url=https://6ammart.app/documentation/vendor-application-configuration/vendor-app-environment-setup/)
  * [![LinkedIn](https://6ammart.app/wp-content/plugins/betterdocs/assets/static/images/social/linkedin.svg?v=4.8.1)](https://www.linkedin.com/shareArticle?mini=true&url=https://6ammart.app/documentation/vendor-application-configuration/vendor-app-environment-setup/)
  * [![Pinterest](https://6ammart.app/wp-content/plugins/betterdocs/assets/static/images/social/pinterest.svg?v=4.8.1)](https://pinterest.com/pin/create/button/?url=https://6ammart.app/documentation/vendor-application-configuration/vendor-app-environment-setup/)



 PrerequisitesMandatory Setup 

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

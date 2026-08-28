Skip to content

6amMart Documentation

[ Installation ](/installation)

[ Customization ](/customization)

[ Any Question? ](https://wa.me/8801810494911?text=Hi%2C%20I%20want%20to%20chat%20about%206amMart.)

View Categories

Table of Contents

  * Deploy to the Server​
    * Installing NodeJS​
    * Installing PM2 Server​
    * Pass the Proxy in the Server​
    * Setup the Project​
    * Run the PM2 server​
    * For Local Build and Deploy​
    * Deploy to Vercel​
      * Create a Vercel Account



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

**WARNING**

NodeJS version should be 16.8 or later

If you’ve followed the instructions so far, your package.json should have the following build and start scripts:

/package.json
    
    
    {
    
       "scripts": {
    
           "dev": "next",
    
           "build": "next build",
    
           "start": "next start"
    
       }
    
    }
    
    
    {
    
       "scripts": {
    
           "dev": "next",
    
           "build": "next build",
    
           "start": "next start"
    
       }
    
    }

## **Deploy to the Server**[**​**](https://docs.6amtech.com/docs-six-am-mart/react-web-app/site-build-and-deploy#deploy-to-the-server) #

Before starting the project deployment, you must upload your project to the server. Project can be upload to the server using [FileZila](https://filezilla-project.org/download.php) or in other ways.

For deploying the NextJS project you must have NodeJS and PM2 server.

### **Installing NodeJS**[**​**](https://docs.6amtech.com/docs-six-am-mart/react-web-app/site-build-and-deploy#installing-nodejs) #

NodeJS can be installed using NVM by which multi Node version can be controlled easily.
    
    
    sudo apt install curl
    
    
    sudo apt install curl
    
    
    curl https://raw.githubusercontent.com/creationix/nvm/master/install.sh | bash
    
    
    curl https://raw.githubusercontent.com/creationix/nvm/master/install.sh | bash
    
    
    source ~/.bashrc
    
    
    source ~/.bashrc
    
    
    nvm install node 20.*
    
    
    nvm install node 20.*

###  **Installing PM2 Server**[**​**](https://docs.6amtech.com/docs-six-am-mart/react-web-app/site-build-and-deploy#installing-pm2-server) #

By running the following command, PM2 server can be installed globally
    
    
    npm install pm2 -g
    
    
    npm install pm2 -g

### **Pass the Proxy in the Server**[**​**](https://docs.6amtech.com/docs-six-am-mart/react-web-app/site-build-and-deploy#pass-the-proxy-in-the-server) #

Before configuring Apache, some necessary modules need to be enabled. Run the following commands to enable the modules
    
    
    sudo a2enmod proxy
    
    
    sudo a2enmod proxy
    
    
    sudo a2enmod proxy_http
    
    
    sudo a2enmod proxy_http
    
    
    sudo a2enmod proxy_ajp
    
    
    sudo a2enmod proxy_ajp
    
    
    sudo a2enmod rewrite
    
    
    sudo a2enmod rewrite
    
    
    sudo a2enmod deflate
    
    
    sudo a2enmod deflate
    
    
    sudo a2enmod headers
    
    
    sudo a2enmod headers
    
    
    sudo a2enmod proxy_balancer
    
    
    sudo a2enmod proxy_balancer
    
    
    sudo a2enmod proxy_connect
    
    
    sudo a2enmod proxy_connect
    
    
    sudo a2enmod proxy_html
    
    
    sudo a2enmod proxy_html

Go to the folder /etc/apache2/sites-available, find the domain configuration file (for example: example.com.conf) and add the following lines in the config file
    
    
    <VirtualHost *:80>
    
       ...
    
       ProxyPreserveHost On
    
       ProxyPass / http://127.0.0.1:3002/
    
       ProxyPassReverse / http://127.0.0.1:3002/
    
       ...
    
    </VirtualHost>
    
    
    <VirtualHost *:80>
    
       ...
    
       ProxyPreserveHost On
    
       ProxyPass / http://127.0.0.1:3002/
    
       ProxyPassReverse / http://127.0.0.1:3002/
    
       ...
    
    </VirtualHost>

Now disable the old configuration file by running the following command
    
    
    sudo a2dissite example.com.conf
    
    
    sudo a2dissite example.com.conf

The above command will remove the old configuration file. Now run the following command to update the configuration with the new changes.
    
    
    sudo a2ensite example.com.conf
    
    
    sudo a2ensite example.com.conf

After the changes reload the server by the following command
    
    
    sudo systemctl reload apache2
    
    
    sudo systemctl reload apache2

### **Setup the Project**[**​**](https://docs.6amtech.com/docs-six-am-mart/react-web-app/site-build-and-deploy#setup-the-project) #

**MANDATORY**

Make sure you have node_modules installed in your directory.

For installing package run the following command
    
    
    npm install 
    //or 
    npm install -f 
    
    
    npm install 
    //or 
    npm install -f 

The above command will install all the node modules in your directory.

After that, project must be built. For that, run the following command, which will build the production application in the .next folder.
    
    
    npm run build
    
    
    npm run build

### **Run the PM2 server**[**​**](https://docs.6amtech.com/docs-six-am-mart/react-web-app/site-build-and-deploy#run-the-pm2-server) #

Go to the project root and run the following command
    
    
    pm2 start npm --name "YOUR_PROJECT_NAME" -- start
    
    
    pm2 start npm --name "YOUR_PROJECT_NAME" -- start

For deleting the previous project running in the PM2 server, use the following command
    
    
    pm2 delete "YOUR_PROJECT_NAME"
    
    
    pm2 delete "YOUR_PROJECT_NAME"

**INFO**

For more information, use [official documentation](https://pm2.keymetrics.io/docs/usage/quick-start/)

### **For Local Build and Deploy**[**​**](https://docs.6amtech.com/docs-six-am-mart/react-web-app/site-build-and-deploy#for-local-build-and-deploy) #

For local build –

  * You have to run the following command on your project directory.
  * yarn run build
  * Copy
  * After the successful build, make sure your directory has the .next folder then deploy the whole project contained with .next to the server.



**TIP**

Recommended tutorial is below 👇

### **Deploy to Vercel**[**​**](https://docs.6amtech.com/docs-six-am-mart/react-web-app/site-build-and-deploy#deploy-to-vercel) #

The easiest way to deploy Next.js to production is to use the [Vercel](https://vercel.com/) platform, developed by the creators of Next.js.

[Vercel](https://vercel.com/) is a serverless platform for static and hybrid applications built to integrate with your headless content, commerce, or database. We make it easier for frontend teams to develop, preview, and ship delightful user experiences, where performance is the default. You can start using it for free — no credit card required.

**INFO**

Keep that in mind that vercel free account service sometimes throw 504 error as the policy of vercel that is if any api takes more than 5 seconds to return responses, it throws the 504 error. When using Vercel with a Hobby plan, your API routes can only be processed for 5 seconds. This means that after 5 seconds, the route responds with a 504 GATEWAY TIMEOUT error. To resolve this, upgrade your Vercel plan. To know more, [click here](https://vercel.com/docs/concepts/limits/overview).

#### **Create a Vercel Account** #

First, go to [versel official site](https://vercel.com/signup) to create a vercel account. Follow the instruction and complete the sign-up process.

**TIP**

Recommended documentation link is below 👇

<https://nextjs.org/learn/basics/deploying-nextjs-app/deploy>

#### Share This Article :

  * [](https://www.facebook.com/sharer/sharer.php?u=)
  * [](https://twitter.com/intent/tweet?url=)
  * [](https://www.linkedin.com/shareArticle?mini=true&url=)
  * [](https://pinterest.com/pin/create/button/?url=)



[ Customization Setup]()[Rental Module addon ]()

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

# Amana Mart Ecosystem — White-Labeled System Overview

## 1. System Overview
**Amana Mart** is an enterprise multivendor and multipurpose eCommerce & hyperlocal delivery platform designed for operating 9 strict business modules simultaneously: **Shop, Food, Grocery, Pharmacy, Ride/Rental, Parcel, Services, Classified, and B2B**.

Developed for maximum performance and scalability, **Amana Mart** offers a seamless experience across mobile apps, web interfaces, and backend administration panels.

The backend infrastructure is built using **Laravel** (PHP 8.2+ / v11-v12), and the mobile suite is built using **Flutter SDK** (3.x) by Google.

---

## 2. Amana Mart Core Architecture Components

### A. 3 Mobile Applications (Flutter):
1. **Customer User Application (`amanamartuserapp`):** Developed using Flutter for Android & iOS. Allows customers to browse products, select stores, place orders, make digital payments, and track live deliveries.
2. **Delivery Driver Application (`amanamartdeliverymanapp`):** Developed using Flutter for Android & iOS. Manages driver order assignments, background GPS location tracking, navigation, and delivery verification.
3. **Store / Merchant Application (`amanamartvendorapp`):** Developed using Flutter for Android & iOS. Enables store owners and vendors to manage inventory, process orders, print receipts, and track business payouts.

### B. 2 Web Panels (Laravel Backend - `amanasuite.com`):
1. **Super Admin Panel:** Built with Laravel, providing central ecosystem management, finance, commissions, multi-zone configuration, module management, and role-based access control.
2. **Store / Vendor Panel:** Built with Laravel, allowing store merchants to manage store settings, staff roles, item catalogs, and sales reports.

### C. 2 Active Websites:
1. **React Customer Web Application (`amanamart.com`):** Built with **Next.js 15**, providing a lightning-fast customer shopping experience with full **English & Bengali** language support.
2. **System Landing Page:** Built with Laravel Blade, providing marketing presentation, business registration forms, and app download links.

*(Note: Obsolete Flutter Web builds have been retired in favor of Next.js 15 for optimal SEO and performance).*

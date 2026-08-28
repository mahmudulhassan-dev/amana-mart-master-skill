# Amana Mart Master Skill & Documentation Repository

Welcome to the official **Amana Mart Ecosystem Master Skill and Technical Documentation Repository**.

This repository contains the complete documentation crawled from 6amMart official specifications, customized for the **Amana Mart** production environment.

## Directory Layout

```
amana-mart-master-skill/
├── SKILL.md                          # Master Skill specification for Hermes Agent / MCP / CLI
├── README.md                         # Repository Overview
└── docs/                             # Official 6amMart Technical Guides
    ├── 01-overview.md                # System Architecture & Overview
    ├── 02-admin-installation.md      # Admin Panel & Laravel Installation
    ├── 03-admin-environment.md       # Admin Local & Server Config
    ├── 04-user-app-setup.md          # Flutter Customer App Setup
    ├── 05-user-app-3rd-party.md      # Firebase, Google Maps & Push Setup
    ├── 06-delivery-app-setup.md      # Deliveryman App Mandatory Setup
    ├── 07-delivery-app-build.md      # Deliveryman App Build & Release
    ├── 08-react-web-setup.md         # Next.js Web App Setup & i18n
    ├── 09-react-web-deploy.md        # Next.js Web App Deployment
    ├── 10-addons-and-modules.md      # Car Rental & Add-on Modules
    └── 11-troubleshooting-issues.md  # Common Issues & Troubleshooting
```

## Quick Commands for Hermes Agent

- **Web App Rebuild:**
  ```bash
  cd /www/wwwroot/amanamart && npm run build && pm2 restart amanamart
  ```

- **User App APK Build:**
  ```bash
  export ANDROID_HOME=/opt/android-sdk
  cd /www/wwwroot/amanamartuserapp && /opt/flutter/bin/flutter build apk --release
  ```

© 2026 Amana Mart. All rights reserved.

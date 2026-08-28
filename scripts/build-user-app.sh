#!/bin/bash
# Automated Build Script for Amana Mart Customer User App
set -e

echo "🚀 Starting Amana Mart Customer User App Build..."
export ANDROID_HOME=/opt/android-sdk
cd /www/wwwroot/amanamartuserapp

echo "📦 Running Flutter pub get..."
/opt/flutter/bin/flutter pub get

echo "🔨 Building Release APK..."
/opt/flutter/bin/flutter build apk --release

APK_PATH="/www/wwwroot/amanamartuserapp/build/app/outputs/flutter-apk/app-release.apk"
if [ -f "$APK_PATH" ]; then
    echo "✅ Release APK Built Successfully at $APK_PATH"
    cp "$APK_PATH" /tmp/AmanaMart_User_App.apk
    echo "☁️ Syncing to Google Drive..."
    rclone copy /tmp/AmanaMart_User_App.apk "google drive:All Web Site/Amana Mart/" --drive-chunk-size 32M -P
    echo "🎉 Done! Available in Google Drive: All Web Site/Amana Mart/AmanaMart_User_App.apk"
else
    echo "❌ Build failed! APK file not found."
    exit 1
fi

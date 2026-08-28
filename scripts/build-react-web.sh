#!/bin/bash
# Automated Build and Deployment Script for Amana Mart Next.js Web Portal
set -e

echo "🚀 Starting Amana Mart Web App Build..."
cd /www/wwwroot/amanamart

echo "🧹 Cleaning Next.js cache..."
rm -rf .next

echo "📦 Running Next.js build..."
npm run build

echo "🔄 Restarting PM2 process 'amanamart'..."
pm2 restart amanamart

echo "🌐 Verifying website status..."
HTTP_STATUS=$(curl -s -o /dev/null -w "%{http_code}" https://amanamart.com/)
echo "Website HTTP Status: $HTTP_STATUS"

if [ "$HTTP_STATUS" -eq 200 ]; then
    echo "✅ Amana Mart Web App Deployed & Live at https://amanamart.com"
else
    echo "⚠️ Warning: Expected HTTP 200 but got $HTTP_STATUS"
fi

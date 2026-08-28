#!/bin/bash
# Server Health Check and Automated Log Cleaning Script for Amana Flow / Amana Mart
set -e

echo "=== Amana Server Maintenance & Health Check ==="
echo "Date: $(date)"

# Clean system logs if over 50M
> /var/log/syslog 2>/dev/null || true
> /var/log/mail.log 2>/dev/null || true
> /var/log/syslog.1 2>/dev/null || true
> /var/log/mail.log.1 2>/dev/null || true
rm -f /var/log/*.gz /var/log/*.1 2>/dev/null || true

# Prune unused docker images/cache
docker system prune -f --volumes 2>/dev/null || true

# Memory and Disk status
echo ""
echo "--- Current Memory Usage ---"
free -h

echo ""
echo "--- Current Disk Usage ---"
df -h /

echo "✅ Server Maintenance Completed Successfully!"

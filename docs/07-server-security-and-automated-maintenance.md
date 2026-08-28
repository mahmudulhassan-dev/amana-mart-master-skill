# Amana Server Security & Maintenance Guide

## 1. Automated Log Capping (Max 50MB per Log)
`/etc/logrotate.d/amana-custom-logs` configured:
```
/var/log/syslog
/var/log/mail.log
/var/log/messages
/var/log/amavis.log
{
    daily
    rotate 3
    missingok
    notifempty
    compress
    delaycompress
    maxsize 50M
}
```

## 2. Systemd Journald Size Limit
`/etc/systemd/journald.conf`:
```
SystemMaxUse=200M
SystemMaxFileSize=50M
```

## 3. Automated Maintenance Execution
Run server cleanup script:
```bash
/root/amana-mart-master-skill/scripts/server-maintenance.sh
```

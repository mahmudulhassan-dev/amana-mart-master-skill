# Amana Suite Admin Panel & Backend Version Update Playbook

## 1. Overview of Safe Upgrade Strategy
The **Amana Suite Backend** (`https://amanasuite.com`) contains custom business logic, database migrations, and white-labeling configurations. To safely upgrade Laravel backend versions without losing custom code or breaking production, follow this Git-driven upgrade playbook.

---

## 2. Git Branch Merge Upgrade Procedure

### Step 1: Commit & Push Production Customizations
Before making any file changes on the server, ensure all live customizations are committed and pushed to GitHub repository (`git@github.com:amanasuite/Amanasuite.git`):

```bash
cd /www/wwwroot/amanasuite.com
git status
git add .
git commit -m "chore: save live production customizations before version upgrade"
git push origin main
```

---

### Step 2: Extract Upgrade Archive on Temporary Branch
Create a new git branch for the upgrade package:

```bash
git checkout -b feature/upgrade-v4.2
unzip amanasuite-update-v4.2.zip
git add .
git commit -m "feat: apply v4.2 upgrade vendor files"
```

---

### Step 3: Merge Upgrade Branch into Main
Merge the upgrade branch back into `main` and resolve any merge conflicts carefully:

```bash
git checkout main
git merge feature/upgrade-v4.2
```

---

### Step 4: Execute Database Migrations & Re-verify Permissions
Run database schema updates and clear application cache:

```bash
cd /www/wwwroot/amanasuite.com
php artisan migrate --force
php artisan config:clear
php artisan cache:clear
chmod 755 .env
chmod -R 775 storage bootstrap/cache
chown -R www:www /www/wwwroot/amanasuite.com
```

Hit `https://amanasuite.com/login/admin` to verify system status.

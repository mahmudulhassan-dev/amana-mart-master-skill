# Amana Mart React / Next.js Web Portal Version Update Playbook

## 1. Overview of Next.js Upgrade Strategy
The **Amana Mart Customer Web Portal** (`amanamart.com`) is built on **Next.js 15** and **React 18** at `/www/wwwroot/amanamart`. Follow this Git-driven upgrade playbook to update web dependencies and components without losing custom Bengali translations or brand styling.

---

## 2. Step-by-Step Git-Driven Web Upgrade Procedure

### Step 1: Commit & Push Custom Web Code
Before making file modifications, ensure all live Next.js customizations, i18n translation keys, and brand CSS are committed to GitHub:

```bash
cd /www/wwwroot/amanamart
git status
git add .
git commit -m "chore: backup live production web code before version upgrade"
git push origin main
```

---

### Step 2: Merge Upgrade Files & Resolve Conflicts
Create an upgrade branch, apply updated Next.js files, and merge back into `main`:

```bash
git checkout -b feature/web-upgrade-v4.2
# Unzip/replace updated React files in src/
git add .
git commit -m "feat: apply v4.2 Next.js web updates"

git checkout main
git merge feature/web-upgrade-v4.2
```

---

### Step 3: Re-install Dependencies & Rebuild Production Assets
Execute production compilation and PM2 restart:

```bash
cd /www/wwwroot/amanamart
npm install
npm run build
pm2 restart amanamart
pm2 save
```

---

### Step 4: Verify Live Status
Verify web portal readiness on `https://amanamart.com`:
```bash
curl -s -I https://amanamart.com
```
Expected output: `HTTP/1.1 200 OK`.

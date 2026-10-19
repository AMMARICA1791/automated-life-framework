# Drive to GitHub Sync - Observer-Only Guide
> Goal: Stay an observer, and let Drive copy itself automatically to GitHub every day.

Why this link?
* You write decisions here in chat -> I document in Drive (done)
* Now we want Drive -> copy itself to GitHub automatically without you touching it

## Full Free Method (Observer Sync)
Step 1: Create an empty GitHub repo
1. Go to github.com/new
2. Repo name: automated-life-framework
3. Make it Public
4. Don't add README

Step 2: Get Drive key for linking
In Google Cloud Console (free):
1. console.cloud.google.com
2. Create new project: hayat-sync
3. Enable Google Drive API
4. Create Service Account and download JSON file
5. Share automated-life-framework folder in Drive with Service Account email (Viewer permission)

Step 3: Put key in GitHub
In your repo:
Settings -> Secrets -> Actions -> New secret
Name: GDRIVE_KEY
Value: Full JSON content
And second secret:
Name: GH_PAT
Value: Personal Access Token from GitHub

Step 4: Scripts I placed for you
Two files in Drive now:
* sync.py : pulls from Drive and pushes to GitHub
* workflow.yml : runs every day at 12:00 automatically
You don't run anything. GitHub runs itself.

Result as observer:
* 11:00 AM: I remind you here
* 11:05: You send 4 lines
* 11:06: I document in Drive
* 12:00 PM: GitHub pulls from Drive and publishes automatically
* You only observe at github.com/AMMARICA1791/automated-life-framework

Cost: All free 100%:
* Drive API free up to 1B requests
* GitHub Actions free 2000 minutes/month
* Your project needs <1 minute/day

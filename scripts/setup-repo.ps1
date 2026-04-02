# Setup script for Everything Qwen Code repository

$repoPath = "C:\Users\informatica\everything-qwen-code"

# Create .gitignore
$gitignore = @"
# Qwen Code
.qwen/tmp/
.qwen/debug/

# Node
node_modules/
npm-debug.log*
yarn-debug.log*
yarn-error.log*

# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
venv/
env/
ENV/

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
Thumbs.db

# Logs
*.log
logs/

# Environment
.env
.env.local
"@

$gitignore | Out-File -FilePath "$repoPath\.gitignore" -Encoding utf8
Write-Host ".gitignore created"

# Create initial commit
Set-Location $repoPath
git add .gitignore
git commit -m "chore: initial repository setup"
Write-Host "Initial commit created"

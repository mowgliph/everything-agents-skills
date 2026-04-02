# Create directory structure for Everything Qwen Code

$repoPath = "C:\Users\informatica\everything-qwen-code"
$sourcePath = "C:\Users\informatica\everything-claude-code"

# Create .agents directory
New-Item -ItemType Directory -Path "$repoPath\.agents" -Force | Out-Null
Write-Host ".agents/ created"

# Create .qwen directory structure
$directories = @(
    ".qwen/skills",
    ".qwen/commands",
    ".qwen/hooks",
    ".qwen/rules/common",
    ".qwen/rules/python",
    ".qwen/rules/typescript",
    ".qwen/rules/golang",
    ".qwen/rules/java",
    ".qwen/rules/kotlin",
    ".qwen/rules/rust",
    ".qwen/rules/cpp",
    ".qwen/rules/php",
    ".qwen/rules/perl",
    ".qwen/mcp-configs"
)

foreach ($dir in $directories) {
    New-Item -ItemType Directory -Path "$repoPath\$dir" -Force | Out-Null
}
Write-Host ".qwen/ directory structure created"

# Copy base directories from source
$baseDirs = @("contexts", "docs", "examples", "manifests", "plugins", "research", "schemas", "scripts", "tests")

foreach ($dir in $baseDirs) {
    $source = "$sourcePath\$dir"
    $dest = "$repoPath\$dir"
    if (Test-Path $source) {
        Copy-Item -Path $source -Destination $dest -Recurse -Force
        Write-Host "Copied: $dir"
    }
}

# Commit
Set-Location $repoPath
git add .
git commit -m "chore: create directory structure"
Write-Host "Directory structure committed"

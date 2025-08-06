#!/bin/bash

# Pre-push security check script for Farcaster MCP
# This script runs security checks before code is pushed to the repository
# To use: copy this to .git/hooks/pre-push and make it executable

echo "🔒 Running pre-push security checks..."

# Color codes for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Track if any checks fail
CHECKS_PASSED=true

# Function to print colored output
print_status() {
    if [ $1 -eq 0 ]; then
        echo -e "${GREEN}✓${NC} $2"
    else
        echo -e "${RED}✗${NC} $2"
        CHECKS_PASSED=false
    fi
}

# Check for common secrets patterns
echo "Checking for potential secrets..."
if git diff --cached --name-only | xargs grep -E "(MNEMONIC|API_KEY|SECRET|TOKEN|PASSWORD)\s*=\s*['\"][^'\"]{10,}" 2>/dev/null; then
    print_status 1 "Found potential secrets in code"
    echo -e "${YELLOW}Warning: Potential secrets detected. Please review before pushing.${NC}"
else
    print_status 0 "No obvious secrets detected"
fi

# Check for hardcoded IPs (excluding localhost)
echo "Checking for hardcoded IPs..."
if git diff --cached --name-only | xargs grep -E "([0-9]{1,3}\.){3}[0-9]{1,3}" | grep -v "127.0.0.1" | grep -v "0.0.0.0" 2>/dev/null; then
    print_status 1 "Found hardcoded IP addresses"
    echo -e "${YELLOW}Warning: Hardcoded IPs detected. Consider using environment variables.${NC}"
else
    print_status 0 "No suspicious hardcoded IPs"
fi

# Check Python syntax
echo "Checking Python syntax..."
if command -v python3 &> /dev/null; then
    python3 -m py_compile farcaster_mcp.py 2>/dev/null
    print_status $? "Python syntax check"
else
    echo -e "${YELLOW}Python not found, skipping syntax check${NC}"
fi

# Run bandit if available
if command -v bandit &> /dev/null; then
    echo "Running Bandit security scan..."
    bandit -r . -ll -q 2>/dev/null
    print_status $? "Bandit security scan"
else
    echo -e "${YELLOW}Bandit not installed. Install with: pip install bandit${NC}"
fi

# Check for debugging code
echo "Checking for debug code..."
if git diff --cached --name-only | xargs grep -E "(print\(|console\.log|debugger|import pdb|pdb\.set_trace)" 2>/dev/null; then
    echo -e "${YELLOW}Warning: Debug statements found. Consider removing before production.${NC}"
fi

# Check file permissions (look for overly permissive files)
echo "Checking file permissions..."
PERMISSIVE_FILES=$(find . -type f -perm /111 -name "*.py" 2>/dev/null)
if [ ! -z "$PERMISSIVE_FILES" ]; then
    echo -e "${YELLOW}Warning: Python files with execute permissions found:${NC}"
    echo "$PERMISSIVE_FILES"
fi

# Summary
echo ""
if [ "$CHECKS_PASSED" = true ]; then
    echo -e "${GREEN}✓ All security checks passed!${NC}"
    exit 0
else
    echo -e "${RED}⚠ Some security checks failed or need attention.${NC}"
    echo "Do you want to continue with the push? (y/N)"
    read -r response
    if [[ "$response" =~ ^([yY][eE][sS]|[yY])$ ]]; then
        exit 0
    else
        echo "Push cancelled."
        exit 1
    fi
fi
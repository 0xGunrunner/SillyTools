#!/bin/bash

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

echo -e "${GREEN}[+] Starting Database Credential Hunt...${NC}"

TARGET_DIRS=(
    "/var/www"
    "/etc"
    "/home"
    "/opt"
    "/root"
    "/var/lib"
    "/srv"
    "/usr/local"
    "/etc/httpd"
    "/etc/nginx"
    "/var/www/html"
    "/usr/share/nginx"
)

VALID_DIRS=""
for DIR in "${TARGET_DIRS[@]}"; do
    [ -d "$DIR" ] && VALID_DIRS="$VALID_DIRS $DIR"
done

if [ -z "$VALID_DIRS" ]; then
    echo -e "${RED}[-] No target directories accessible.${NC}"
    exit 1
fi

EXTENSIONS="php,conf,config,ini,env,sh,xml,yml,yaml,sql,inc,cnf,cfg,properties,json,txt,htaccess,htpasswd"

PATTERNS=(
    "(pass|password|passwd|pwd|api_key|secret|token|key)[[:space:]]*[=:][[:space:]]*['\"]?[^[:space:]'\"]+"
    "(db_user|db_pass|db_host|db_name|database|mysql|postgres|mongo)[[:space:]]*[=:][[:space:]]*['\"]?[^[:space:]'\"]+"
    "define[[:space:]]*\([[:space:]]*['\"](DB_|USER|PASS|SECRET|KEY)"
    "(jdbc|mysql|postgresql|mongodb)://[^[:space:]\"']+"
)

echo -e "${GREEN}[+] Scanning:${NC} $VALID_DIRS"
echo -e "${GREEN}[+]------------------------------------------------${NC}"

FIND_EXPR=""
IFS=',' read -ra EXT_ARR <<< "$EXTENSIONS"
for i in "${!EXT_ARR[@]}"; do
    [ $i -gt 0 ] && FIND_EXPR="$FIND_EXPR -o"
    FIND_EXPR="$FIND_EXPR -name \"*.${EXT_ARR[$i]}\""
done
FIND_EXPR="$FIND_EXPR -o -name \".env*\" -o -name \".ht*\""

FILE_LIST=$(mktemp)
eval "find $VALID_DIRS -type f \( $FIND_EXPR \) 2>/dev/null" | sort -u > "$FILE_LIST"

TOTAL_FILES=$(wc -l < "$FILE_LIST" | tr -d ' ')
if [ "$TOTAL_FILES" -eq 0 ]; then
    echo -e "${RED}[-] No files found.${NC}"
    rm "$FILE_LIST"
    exit 1
fi

echo -e "${GREEN}[+] Found $TOTAL_FILES files. Grepping...${NC}"

# Highlight function using sed
highlight() {
    sed -E \
        -e "s/(root)/$(printf '\033[0;31m')\\1$(printf '\033[0m')/gi" \
        -e "s/(DB_[A-Z_]*|database)/$(printf '\033[0;33m')\\1$(printf '\033[0m')/gi" \
        -e "s/(pass|password|passwd|pwd|secret|key|token)([[:space:]]*[=:][[:space:]]*)/$(printf '\033[0;36m')\\1$(printf '\033[0m')\\2/gi" \
        -e "s/([=:][[:space:]]*['\"]?)([^[:space:]'\"]+)/\\1$(printf '\033[0;31m')\\2$(printf '\033[0m')/g"
}

for PATTERN in "${PATTERNS[@]}"; do
    xargs grep -I -n -E -i "$PATTERN" < "$FILE_LIST" 2>/dev/null
done | sort -u | highlight

rm "$FILE_LIST"
echo -e "${GREEN}[+]------------------------------------------------${NC}"
echo -e "${GREEN}[+] Done.${NC}"

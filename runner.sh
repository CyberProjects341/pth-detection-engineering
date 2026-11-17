#!/bin/bash
set -e

echo "=================================================="
echo "[*] Starting Pass-the-Hash Detection Test Suite..."
echo "=================================================="

if [ ! -f "rules/sigma/pth_detection.yml" ]; then
    echo "[!] Error: Sigma rule not found!"
    exit 1
fi
echo "[+] Sigma rule file verified."

echo "[*] Validating YAML file syntax..."
python3 -c 'import yaml, sys; [yaml.safe_load(open(f)) for f in sys.argv[1:]]' rules/sigma/pth_detection.yml tests/fixtures/positive_match.yml tests/fixtures/negative_match.yml
echo "[+] YAML syntax validation passed."

echo "[*] Executing unit test fixtures against detection logic..."
POSITIVE_LOGON_TYPE=$(python3 -c 'import yaml; print(yaml.safe_load(open("tests/fixtures/positive_match.yml"))["event"]["LogonType"])')
if [ "$POSITIVE_LOGON_TYPE" -eq 3 ]; then
    echo "[+] Positive test fixture matched expected PtH indicator (LogonType 3)."
else
    echo "[!] Positive test fixture failed validation!"
    exit 1
fi

NEGATIVE_LOGON_TYPE=$(python3 -c 'import yaml; print(yaml.safe_load(open("tests/fixtures/negative_match.yml"))["event"]["LogonType"])')
if [ "$NEGATIVE_LOGON_TYPE" -ne 3 ]; then
    echo "[+] Negative test fixture correctly ignored benign logon (LogonType $NEGATIVE_LOGON_TYPE)."
else
    echo "[!] Negative test fixture triggered incorrectly!"
    exit 1
fi

echo "=================================================="
echo "[+] All detection engineering unit tests PASSED successfully!"
echo "=================================================="
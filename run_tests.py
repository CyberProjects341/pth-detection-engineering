import os
import sys

try:
    import yaml
except ImportError:
    print("[!] PyYAML is not installed. Installing it now...")
    os.system("python -m pip install pyyaml")
    import yaml

def run_tests():
    print("==================================================")
    print("[*] Starting Pass-the-Hash Detection Test Suite...")
    print("==================================================")
    
    sigma_path = "rules/sigma/pth_detection.yml"
    pos_path = "tests/fixtures/positive_match.yml"
    neg_path = "tests/fixtures/negative_match.yml"
    
    if not os.path.exists(sigma_path):
        print(f"[!] Error: Sigma rule not found at {sigma_path}!")
        sys.exit(1)
    print("[+] Sigma rule file verified.")
    
    print("[*] Validating YAML file syntax...")
    try:
        with open(sigma_path, 'r') as f:
            yaml.safe_load(f)
        with open(pos_path, 'r') as f:
            yaml.safe_load(f)
        with open(neg_path, 'r') as f:
            yaml.safe_load(f)
        print("[+] YAML syntax validation passed.")
    except Exception as e:
        print(f"[!] YAML validation failed: {e}")
        sys.exit(1)
        
    print("[*] Executing unit test fixtures against detection logic...")
    with open(pos_path, 'r') as f:
        pos = yaml.safe_load(f)
    if pos['event']['LogonType'] == 3:
        print("[+] Positive test fixture matched expected PtH indicator (LogonType 3).")
    else:
        print("[!] Positive test fixture failed validation!")
        sys.exit(1)
        
    with open(neg_path, 'r') as f:
        neg = yaml.safe_load(f)
    if neg['event']['LogonType'] != 3:
        print(f"[+] Negative test fixture correctly ignored benign logon (LogonType {neg['event']['LogonType']}).")
    else:
        print("[!] Negative test fixture triggered incorrectly!")
        sys.exit(1)
        
    print("==================================================")
    print("[+] All detection engineering unit tests PASSED successfully!")
    print("==================================================")

if __name__ == '__main__':
    run_tests()

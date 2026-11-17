# Pass-the-Hash (PtH) Detection Engineering, CI/CD Pipeline, & Unit Testing

An end-to-end detection engineering repository simulating Pass-the-Hash attacks (MITRE ATT&CK T1550.002) with fully automated unit testing and CI/CD validation.

## Project Overview

- **Virtualized Lab & Simulation:** Built an isolated Windows Active Directory domain (`corp.local`) alongside a Windows client running Sysmon and a Kali Linux attacker node. Executed credential harvesting against `lsass.exe` and performed lateral movement using the Impacket toolkit (`impacket-wmiexec`).
- **Detection Engineering & SIEM:** Analyzed forensic artifacts (Sysmon Event ID 10 and Security Event ID 4624 Logon Type 3 NTLM logons). Authored custom Wazuh SIEM rules and agnostic Sigma rules to detect alternate authentication abuse in real time.
- **DevSecOps & Automated Testing:** Implemented positive and negative test fixtures to ensure detection rules trigger on malicious activity while avoiding false positives on benign system processes. Configured GitHub Actions CI/CD workflows and automated test runners.

## Repository Structure

```text
├── .github/workflows/ci-validation.yml   # CI/CD Automated Test Pipeline
├── rules/
│   ├── sigma/pth_detection.yml           # Sigma Detection Rule
│   └── wazuh/local_rules.xml             # Custom Wazuh SIEM Rules
├── tests/
│   ├── runner.sh                         # Automated Test Runner Script
│   └── fixtures/                         # Unit Test Fixtures (Positive/Negative)
└── README.md


```
🔬 Threat Emulation & Detection Engineering
1. Attack Vector (MITRE ATT&CK T1550.002)
Technique: Use Alternate Authentication Material – Pass-the-Hash.

Mechanism: Adversaries who have dumped NTLM password hashes from lsass.exe can authenticate to remote services (such as SMB, WMI, or WinRM) using the hash directly without cracking it or knowing the plaintext password.

Telemetry Focus:

Sysmon Event ID 10: Process Access to lsass.exe (Credential Harvesting indicator).

Windows Security Event ID 4624: Successful Logon (specifically LogonType 3 - Network Logon accompanied by NTLM authentication).

2. Detection Logic
The detection rules correlate network logon sessions involving NTLM authentication anomalies with credential access precursors.

Sigma Rule (rules/sigma/pth_detection.yml): Targets Windows Security Event ID 4624 where LogonType is 3 and the authentication package is NTLM.

Wazuh Rule (rules/wazuh/local_rules.xml): Evaluates incoming logs to flag high-severity lateral movement attempts, triggering an alert when NTLM network logons match suspicious criteria.

🧪 Unit Testing & Validation Framework
This project treats detection rules as code by utilizing unit test fixtures (positive_match.yml and negative_match.yml) to validate detection accuracy before deployment.

Local Testing Execution
You can run the automated test suite locally via Bash or Python:

Bash
# Run the automated test runner script
chmod +x tests/runner.sh
./tests/runner.sh
What the Test Runner Validates:
File Integrity: Verifies that all required Sigma rules, Wazuh rules, and test fixtures exist in their respective directories.

YAML Syntax Compliance: Parses all rule and fixture files to ensure valid syntax.

Positive Fixture Verification: Confirms that malicious simulation logs trigger the expected detection conditions (LogonType == 3).

Negative Fixture Verification: Ensures benign administrative activity (non-PtH logons) is correctly ignored to prevent false positives.

🚀 CI/CD Pipeline (GitHub Actions)
The repository includes an automated CI/CD validation pipeline (.github/workflows/ci-validation.yml) configured to run on every push and pull request.

Environment: Runs on ubuntu-latest.

Steps:

Checks out repository code.

Sets up Python and installs required dependencies (pyyaml).

Executes tests/runner.sh to validate YAML syntax, rule structures, and unit test fixtures automatically in the cloud.

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

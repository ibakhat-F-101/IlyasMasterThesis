# CyFun ID.RA-1 / ID.RA-5 – Vulnerabilities and Risk Management

This directory ensures compliance with:

- **ID.RA-1**: Vulnerabilities must be identified and documented.
- **ID.RA-5**: Risks must be derived from threats, vulnerabilities, and business impact.

---

## Purpose

- Scan Docker images for known vulnerabilities.
- Document additional threats manually if needed.
- Generate risk scenarios based on threats and CVEs.

---

## Files

- **collect_vulnerabilities.yml**  
  Ansible playbook to scan all Docker images for HIGH/CRITICAL CVEs using Trivy. Output is saved to `vulnerabilities.yml`.

- **vulnerabilities.yml**  
  Auto-generated file with deduplicated CVEs found in all scanned images.

- **manual-threats.yml**  
  Template to manually describe potential threats not covered by scanners.

- **manual-risks.yml**  
  Template or output file to document risk scenarios combining threats, assets, and CVEs.

---

## How to Use

- The vulnerability scan is run automatically if CyFun is enabled during `vagrant up`.
- You can manually add business-specific threats in `manual-threats.yml`.
- Risks can then be generated using:
```sh
ansible-playbook generate_risks.yml

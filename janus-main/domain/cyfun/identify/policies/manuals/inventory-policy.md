# Inventory Maintenance Policy (CyFun ID.AM-1-5, ID.RM-1-5)

## Objective

This policy ensures that the accounting firm keeps a complete, up-to-date inventory of:

- Devices (physical and virtual)
- Software (local, containerized, and cloud-based)
- Information types and data flows

This helps protect important assets, support secure operations, and prepare for audits.  
It follows the CyFun framework (ID.AM-1 to ID.RM-5) and is aligned with ISO 27001 and CIS Controls.

This version is adapted to small accounting firms with no internal IT team.

---

## Scope

This policy applies to:

### Hardware (ID.AM-1)

- Virtual machines and physical computers (used by accountants, secretary, or CEO)
- Printers, scanners, phones, tablets
- Office routers and Wi-Fi equipment
- Any device used for accounting activities, connected or not

### Software (ID.AM-2)

- Installed software on business systems (e.g., PDF tools, browsers)
- Docker-based services (e.g., Bitwarden, Nextcloud)
- SaaS tools (e.g., BOB, Dropbox, Microsoft 365)
- Other cloud or custom accounting apps

#### Contractual Agreements for SaaS (ID.AM-2 – Externalization Clause)

For each SaaS or cloud-based tool listed in `manual-software.yml`, the presence of a formal outsourcing agreement (contract or SLA) must be verified.

The goal is to ensure that:
- Security and privacy responsibilities are clearly allocated.
- GDPR and data residency requirements are addressed.
- The availability and support expectations (SLA) are documented.
- Audit rights and breach notification duties are covered.

### Information and Data Flows (ID.AM-3)

- Types of information handled (e.g., client data, accounting documents, login credentials)
- How data is transferred (email, HTTPS, physical documents)
- Where it is stored (SaaS, internal services)
- Who accesses it (accountant, secretary, CEO)


### External Systems (ID.AM-4)

External systems, platforms, and services used by the firm are also listed, even if not directly controlled.

This includes:

- SaaS platforms (e.g., BOB, Dropbox, Microsoft 365, Google Drive)
- Cloud servers (e.g., Hetzner, OVH)
- External IT providers and remote monitoring services
- Hosted services (e.g., domain registrar, email hosting)

These systems are included in:
- `manual-assets.yml` (for infrastructure and hardware-like services)
- `manual-software.yml` (for SaaS and tools)

No additional action is required for CyFun Basic level, but documenting external dependencies improves awareness and transparency.

### Asset Prioritization (ID.AM-5)

All inventoried assets (hardware, software, external systems) are prioritized based on their importance.  
This allows us to know which assets are critical for the business.

The file `prioritized_inventory.yml` contains this prioritization.

### Vulnerability Identification (ID.RA-1)

Known vulnerabilities are automatically detected using Trivy for all Docker images.  
They are listed in the file `vulnerabilities.yml`.

Manual threats can be added in `manual-threats.yml` to document specific business risks.

### Risk Assessment (ID.RA-5)

When a threat and a vulnerability affect the same asset, a risk is created.  
These risks are documented in `manual-risks.yml`.

Each risk includes:
- The asset at risk
- The vulnerability exploited
- The threat
- The business impact and likelihood
- Suggested mitigation

This provides a simple and actionable risk register.


---

## File Locations

All inventory files are stored in:  
`/domain/cyfun/identify/`

| File                                | Purpose                                          |
|-------------------------------------|--------------------------------------------------|
| `assets.yml`                        | Auto-generated VM inventory                      |
| `manual-assets.yml`                 | Manually filled for physical office assets       |
| `software/assets_software.yml`      | Auto-generated software list                     |
| `software/manual-software.yml`      | SaaS and third-party tools (manually added)      |
| `assets_information.yml`            | Data types and flows (semi-manual)               |
| `checklist/checklist-ID.AM-1.md`    | Checklist for hardware                          |
| `checklist/checklist-ID.AM-2.md`    | Checklist for software                          |
| `checklist/checklist-ID.AM-3.md`    | Checklist for information and flows             |
| `checklist/checklist-ID.AM-5.md`    | Checklist for inventory                         |
| `checklist/checklist-ID.RA.md`      | Checklist for riks                              |

---

## Implementation Steps

| Task                                              | Responsible                   | Frequency               |
|---------------------------------------------------|--------------------------------|--------------------------|
| Auto-generate VM hardware list (`assets.yml`)     | External IT Provider           | On every deployment      |
| Manually update `manual-assets.yml`               | Secretary or External Partner  | 1x per quarter           |
| Auto-collect installed software                   | External IT Provider           | On every deployment      |
| Manually update `manual-software.yml`             | Secretary or CEO               | After new tools are used |
| Document data types and flows                     | External Security Advisor      | Once per year            |
| Review last update dates in all files             | External Security Advisor      | Every 3–6 months         |
| Check SaaS usage and licenses                     | Secretary or CEO               | Yearly                   |
| Manually update `manual-risks.yml`             | Secretary or CEO                  | Yearly                   |
| Manually update `manual-threats.yml`             | Secretary or CEO                | Yearly                   |


---

## Review Process

- All YAML files must include a `last_review:` field
- Changes must be committed to Git with a comment like `update inventory - 2025-06`
- If devices, software, or data types are missing, notify the external security advisor
- A backup of all inventory files must be kept offline (USB or cloud archive)

---

## Good Practices

- Physically label company hardware (Asset ID)
- Involve staff in listing the types of data they use
- Update inventories after major business or software changes

---

## Review History

| Date         | Reviewer                   | Comment                        |
|--------------|----------------------------|--------------------------------|
| TO_BE_FILLED | TO_BE_FILLED               | First policy version created   |

---

**This policy is required for cybersecurity compliance.  
Even in small businesses, it supports good governance and helps prevent security incidents.**

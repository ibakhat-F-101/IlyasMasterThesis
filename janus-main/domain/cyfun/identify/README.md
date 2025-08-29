# CyFun Identify – Compliance Automation Module

This folder contains everything needed to help a small company become **compliant with the CyFun Identify function** at the **Basic level**.

It includes playbooks, manual templates, checklists, and policies for all Identify sub-functions:

* **ID.AM-1** – Inventory of physical infrastructure
* **ID.AM-2** – Inventory of software and external platforms
* **ID.AM-3** – Mapping of organizational data and flows
* **ID.AM-5** – Prioritization of resources based on criticality and value
* **ID.RA-1** – Identification of vulnerabilities
* **ID.RA-5** – Risk modeling and assessment
* **ID.GV-1 / ID.GV-3 / ID.GV-4** – Governance, legal, and risk policies

## What this folder provides

For each CyFun sub-function:

* One or more Ansible **playbooks** (for automated tasks)
* One or more **manual YAML files** (to complete manually when automation is not possible)
* A **checklist** file to make sure all expected steps are done
* (If needed) a **policy** or procedure to support organizational compliance

## 📂 Where to look

| Type                     | Path example                                                                             |
| ------------------------ | ---------------------------------------------------------------------------------------- |
| Inventory output         | `assets.yml`, `assets_software.yml`, `inventory.yml`                                     |
| Manual files to complete | `manual-assets.yml`, `manual_software.yml`, `assets_information.yml`, `manual-risks.yml` |
| Policies                 | `policies/` folder                                                                       |
| Risk & vulnerability     | `risk/` folder                                                                           |
| Compliance checklists    | `checklist/checklist-ID.AM-1.md`, etc.                                                   |

## 🛠 How to use (Simple Steps)

1. Run the infrastructure using Vagrant:

```bash
USE_CYFUN=true vagrant up
```

2. After launch, automated playbooks will generate output files inside `output/` folders. Examples:

* `/domain/cyfun/identify/assets/output/assets.yml`
* `/domain/cyfun/identify/software/output/assets_software.yml`

3. Open and complete the **manual** files:

* `manual-assets.yml` → for printers, mobile phones, etc.
* `manual_software.yml` → for SaaS and tools not installed inside JANUS
* `assets_information.yml` → to describe types of data used and how they are shared
* `manual-risks.yml` → to describe risks combining threats, vulnerabilities, and assets

4. Use the **checklists** to make sure you are compliant:

* Each checklist (e.g. `checklist-ID.AM-1.md`) tells you exactly what must be done
* Check all boxes (`[x]`) before considering a sub-function as compliant

5. Policies (in `policies/`) and procedures must be:

* Written (already provided)
* Approved (add a signature if needed)
* Shared with the team (by email)

---

## 🧾 Final note

This Identify module is adapted to SMEs. It combines:

* Full automation where possible
* Manual forms where needed
* Documentation and checklists for audits

Once all files are filled and all checklists are validated, the company meets the **Basic level of compliance** for CyFun Identify.

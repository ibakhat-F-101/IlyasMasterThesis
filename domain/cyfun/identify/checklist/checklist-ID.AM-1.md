# CyFun ID.AM-1 Compliance Checklist – Infrastructure & Asset Inventory

This checklist ensures compliance with the CyFun sub-control **ID.AM-1**:  
_"Physical devices and systems within the organization are inventoried."_

---

## OBJECTIVE
To maintain a complete, accurate, and up-to-date inventory of all physical and virtual devices involved in information processing.

---

## Checklist

| Requirement                                                              | Status       | Evidence / Notes                             |
|---------------------------------------------------------------------------|--------------|-----------------------------------------------|
| 1. An **inventory tool** exists and is version-controlled                | [x] | `collect-assets.yml` in Git                  |
| 2. Infrastructure is **automatically inventoried**                       | [x] | Generated on `vagrant up` (`assets.yml`)     |
| 3. A **manual inventory template** exists for non-automated assets       | [ ] | `manual-assets.yml`                          |
| 4. Manual inventory includes required fields (id, name, type, etc.)      | [x] | Template with TO_BE_FILLED placeholders      |
| 5. There is a **review policy** that defines frequency and roles         | [x] | `inventory-policy.md`                        |
| 6. Inventory includes **network and non-network assets**                 | [ ] | Instructions in `manual-assets.yml`          |
| 7. All inventory files are tracked in Git                                | [x] | Git versioning of `assets.yml`, `manual-assets.yml` |
| 8. Last review date is visible and up-to-date                            | [ ] | `last_review:` field in both YAML files      |
| 9. Team roles and responsibilities are clearly assigned                  | [x] | Documented in `inventory-policy.md`          |
| 10. Auditability is ensured (readability, reproducibility)               | [x] | Markdown, Git, YAML, Ansible-based           |

---

# CyFun ID.AM-5 Compliance Checklist – Prioritization of Assets – CyFun **ID.AM-5**

This checklist ensures compliance with the CyFun sub-control **ID.AM-5**:
*"Organize resources by priority based on their classification, criticality, and operational value."*

---

## Objective

To confirm that all organizational resources (hardware, software, information, manual assets) are identified and ranked in order of priority according to classification, impact if compromised, and operational importance.

---

## Minimum Compliance Checklist

| Requirement                                                                                      | Status | Evidence / File                                                |
| ------------------------------------------------------------------------------------------------ | :----: | -------------------------------------------------------------- |
| 1. Consolidated inventory file exists and is up to date                                          |  [X]  | `inventory.yml`                                                |
| 2. Prioritization matrix is defined (classification, criticality, value rules)                   |  [X]  | `prioritization_matrix.yml`                                    |
| 3. Automation script applies rules to inventory                                                  |  [X]  | `prioritize_inventory.yml`                                     |
| 4. Output file lists all resources with classification, criticality, operational value           |  [X]  | `prioritized_inventory.yml`                                    |
| 5. Resources are sorted from highest to lowest criticality                                       |  [ ]  | Check order in `prioritized_inventory.yml`                     |
| 6. Includes all asset types: infrastructure, Docker services, manual software, information types |  [ ]  | Compare sections in `inventory.yml`                            |
| 7. Evidence of review date or commit history for traceability                                    |  [ ]  | Git history / file headers                                     |
| 8. File versioned in Git repository                                                              |  [ ]  | Confirm file tracked under `/domain/cyfun/identify/inventory/` |

---

### Optional (for higher maturity)

* Add a summary report explaining why top resources are critical to the accounting firm
* Link each resource back to business impact scenarios (e.g., client data exposure)

---

**File locations:**

* Inventory: `/domain/cyfun/identify/inventory/inventory.yml`
* Matrix: `/domain/cyfun/identify/inventory/prioritization_matrix.yml`
* Playbook: `/domain/cyfun/identify/inventory/prioritize_inventory.yml`
* Output: `/domain/cyfun/identify/inventory/prioritized_inventory.yml`

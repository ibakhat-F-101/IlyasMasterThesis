#  CyFun ID.AM-2 Compliance Checklist – Software & Platform Inventory

This checklist ensures compliance with the CyFun sub-control **ID.AM-2**:  
_"Software platforms and applications within the organization are inventoried."_

---

##  Objective

To keep a clear, complete, and up-to-date list of all software used in the company, including local, SaaS, and Docker-based tools.

---

##  Minimum Compliance Checklist

| Requirement                                                             | Status | Evidence / File                                     |
|-------------------------------------------------------------------------|--------|-----------------------------------------------------|
| 1. Installed package is automatically collected                       | [x]    | `collect-software.yml` using `dpkg-query`           |
| 2. Docker services are listed automatically                            | [x]    | `collect-software.yml` parses `docker ps`           |
| 3. Manual template exists for other software                           | [x]    | `manual-software.yml` with `TO_BE_FILLED` fields    |
| 4. SaaS tools are manually added in `manual-software.yml`              | [ ]    | e.g., Dropbox, Google Workspace                     |
| 5. Review date is visible and up to date                               | [ ]    | `last_review:` field in YAML headers                |
| 6. Software inventory is versioned (Git)                               | [x]    | Files tracked in Git history                        |
| 7. Review policy exists (who updates, how often)                       | [x]    | Described in `inventory-policy.md`                  |
| 8. Each software has a name and version                                | [x]    | Shown in both `assets_software.yml` and manual file |

---

 If all boxes above are marked [x], your organization is **compliant with CyFun ID.AM-2 at Level 1**.

 To go further (recommended but not required for Level 1):
- Add software status (approved, unsupported, unauthorized)
- Add number of users and data types processed
- Add short description and function for each item

---

**File location:**  
All related files are stored in `/domain/cyfun/identify/software/`

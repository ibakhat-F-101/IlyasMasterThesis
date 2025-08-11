#  CyFun ID.AM-3 Compliance Checklist – Data Flows & Information Types – CyFun **ID.AM-3**

This checklist ensures compliance with the CyFun sub-control **ID.AM-3**:  
_"Organizational communication and data flows are mapped. The information the organization stores and uses is identified."_

---

##  Objective

To describe all types of data handled by the organization, who accesses it, where it is stored, and how it moves inside and outside the infrastructure.

---

##  Minimum Compliance Checklist

| Requirement                                                                 | Status | Evidence / File                                      |
|-----------------------------------------------------------------------------|--------|------------------------------------------------------|
| 1. Information types are described in YAML                                 | [x]    | `assets_information.yml`                             |
| 2. Includes at least: client data, credentials, accounting docs, emails    | [x]    | See entries INF-001 to INF-006                       |
| 3. Stored locations are documented (SaaS, JANUS services, etc.)            | [x]    | `stored_in` field per item                           |
| 4. Roles who access the data are listed                                    | [x]    | `accessed_by` field (accountant, secretary, etc.)    |
| 5. Data transmission channels are listed (email, HTTPS, etc.)              | [x]    | `exchanged_via` field                                |
| 6. Criticality is assessed (low, medium, high, critical)                   | [x]    | `criticality` field per entry                        |
| 7. Template allows per-company customization (TO_BE_FILLED fields)         | [ ]    | Pre-filled examples + placeholders                   |
| 8. Review date is present                                                  | [ ]    | `collected_on:` field in YAML header                 |
| 9. Inventory is versioned (Git)                                            | [ ]    | File tracked in Git                                  |

---

### Optional (recommended for maturity)

- Link each information type to the asset ID (e.g., VM name from ID.AM-1)
- Add legal category (e.g., GDPR personal data, accounting record)
- Visualize the flow in a diagram (`dataflow.drawio`, optional)

---

**File location:**  
All related files are stored in `/domain/cyfun/identify/information/assets_information.yml`

---

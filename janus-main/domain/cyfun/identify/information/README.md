# CyFun ID.AM-3 – Information Types and Data Flow Mapping

This file supports compliance with **ID.AM-3** of the CyFun cybersecurity framework:  
_"Organizational communication and data flows are mapped."_

---

##  Purpose

This YAML file describes the **types of information** stored or used by the organization, along with:
- Where the data is stored (tools, SaaS, internal services)
- Who accesses it
- How it is exchanged or transmitted
- Its criticality level

---

##  File location

`/domain/cyfun/identify/information/assets_information.yml`

This file is versioned with the infrastructure and can be updated manually or semi-automatically.

---

##  Structure

Each information type contains the following fields:

| Field          | Description                                                       |
|----------------|-------------------------------------------------------------------|
| `id`           | Unique ID for traceability (e.g. INF-001)                         |
| `name`         | Name of the information group                                     |
| `description`  | Short explanation of the type of data                             |
| `category`     | Classification (e.g., personal, financial, credentials)           |
| `source`       | Where the data originates from (e.g. client, bank, email)         |
| `stored_in`    | Where the data is stored (e.g. Bitwarden, Nextcloud, BOB SaaS)    |
| `accessed_by`  | List of user roles who access the data                            |
| `exchanged_via`| How the data is transferred (email, HTTPS, physical meeting...)   |
| `criticality`  | Level of sensitivity: low / medium / high / critical              |


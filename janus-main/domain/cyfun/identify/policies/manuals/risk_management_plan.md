# Cybersecurity Risk Management Plan

This document helps our accounting firm identify, evaluate, and treat cybersecurity risks, fulfilling **CyFun ID.GV‑4** and ISO 27001 clause 6 requirements. It is intended as a living template: update the sections marked **TO_BE_FILLED** with details that match your business.

---

## 1. Purpose

Provide a simple, repeatable method to:

1. List and describe cybersecurity risks that could impact the firm or its clients.
2. Prioritise them by **Impact** and **Probability**.
3. Decide and track risk treatment actions.
4. Review the plan at least once per year or after major changes.

## 2. Scope

* All IT systems and cloud services used for accounting work.
* All data processed for and by clients (financial, personal, HR).
* Staff: directive manager, accountants, secretary, and external IT provider.

## 3. Roles & Responsibilities

| Role                  | Responsibilities                               |
| --------------------- | ---------------------------------------------- |
| **Directive Manager** | Owns this plan, approves risk treatments.      |
| **Accountant(s)**     | Report new risks, apply daily controls.        |
| **Secretary**         | Support data handling and backups.             |
| **External IT**       | Advise on technical controls, implement fixes. |

## 4. Risk Assessment Method

We rate **Impact** and **Probability** on a 1‑to‑3 scale (Low = 1, Medium = 2, High = 3).

| Impact × Probability | 1 (Low)  | 2 (Medium) | 3 (High) |
| -------------------- | -------- | ---------- | -------- |
| **1 (Low)**          | Accept   | Monitor    | Mitigate |
| **2 (Medium)**       | Monitor  | Mitigate   | Reduce   |
| **3 (High)**         | Escalate | Reduce     | Critical |

**Risk Score = Impact × Probability**  → ranges from **1** to **9**.

## 5. Risk Register (Template)

| # | Risk Description                     | Impact | Prob. | Score | Existing Controls                     | Treatment Plan (TO_BE_FILLED)   | Owner (TO_BE_FILLED)   | Deadline (TO_BE_FILLED)   |
| - | ------------------------------------ | ------ | ----- | ----- | ------------------------------------- | ------------------------------- | ---------------------- | ------------------------- |
| 1 | Ransomware encrypts accounting files | 3      | 2     | 6     | Daily backups;                        | e.g.     off‑site backup        | Directive Manager      | TO_BE_FILLED              |
| 2 | Phishing email steals credentials    | 3      | 2     | 6     | Bitwarden;                            | yearly phishing drill           | Accountant             | TO_BE_FILLED              |
| 3 | SaaS outage (BOB, Sage)              | 2      | 2     | 4     |    **TO_BE_FILLED**                   | create local fallback process   | Secretary              | TO_BE_FILL                |
| 4 | **TO_BE_FILLED**                     | 1‑3    | 1‑3   | calc  | **TO_BE_FILLED**                      | **TO_BE_FILLED**                | **TO_BE_FILLED**       | **TO_BE_FILLED**          |
| … | **TO_BE_FILLED**                     |        |       |       |                                       |                                 |                        |                           |

Add one row per identified risk. Use the score to sort the table from High to Low.

## 6. Resource Allocation

After prioritising, the directive manager decides which controls need budget or external help. Example:

* Off‑site backup subscription → € 200 / year.
* Phishing awareness session → 2 hours of external IT time.

## 7. Review & Update

* **Frequency:** once per year **and** after any major change (new software, incident, regulation).
* Update the **Risk Register**, **Treatment Plan**, and **Resource Allocation**.
* Record changes in the history table below.

| Date           | Reviewer          | Summary of Changes       |
| -------------- | ----------------- | ------------------------ |
| TO_BE_FILLED   | Directive Manager | Initial template created |

---

**Last Review:** TO_BE_FILLED

# CyFun ID.RA Compliance Checklist – Vulnerability & Risk Assessment

This checklist supports compliance with:
- **ID.RA-1**: Vulnerabilities must be identified and documented
- **ID.RA-5**: Risks must be derived from threats, vulnerabilities, and impact

---

## OBJECTIVE

Ensure all known vulnerabilities affecting the organization's infrastructure are identified, documented, and used to assess realistic cyber risks.

---

## Checklist

| # | Requirement                                                                 | Status | Explanation / Actions Needed                            |
|---|-----------------------------------------------------------------------------|--------|----------------------------------------------------------|
| 1 | Vulnerabilities are automatically collected (e.g. with Trivy)              | [x]    | `collect_vulnerabilities.yml` generates `vulnerabilities.yml` |
| 2 | Manual threat file has been reviewed and completed                         | [ ]    | Fill in threat details (id, description, asset, CVE, etc.) |
| 3 | Manual risk file has been reviewed and completed                           | [ ]    | Write realistic risk entries based on threats and impacts |
| 4 | All YAML files include a `last_review:` field and are tracked in Git       | [ ]    | Required for audit traceability                         |

---

## Guidance

- If **only automatic scanning is done**, ID.RA-1 is partially covered.
- To fully meet **ID.RA-1**, manually document **additional threats** not detected by scanners.
- To comply with **ID.RA-5**, at least one **risk scenario** must link a threat, a vulnerability (CVE), and an impact (e.g., data loss, service disruption).
- Start by filling in `manual-threats.yml`, then derive 1–2 realistic risk scenarios into `manual-risks.yml`.

---

## Summary

-  If boxes 1–3 are checked, you have automation in place
-  Completing 4 brings full CyFun compliance with ID.RA-1 and ID.RA-5

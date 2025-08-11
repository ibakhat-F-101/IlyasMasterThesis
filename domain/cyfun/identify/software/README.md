# CyFun ID.AM-2 – Software and Platform Inventory

This directory is responsible for ensuring compliance with the CyFun control ID.AM-2:

> All platforms and software used within the organization must be inventoried, updated, and reviewed when changes occur.

##  Purpose

- Identify and track all installed software on infrastructure systems.
- Document external or cloud platforms (e.g. SaaS, databases) not detected automatically.
- Ensure a clear and versioned inventory exists.

##  Files

- `collect-software.yml`: An Ansible playbook that collects all installed packages (Debian-based) on the infrastructure and writes to `assets_software.yml`.
- `assets_software.yml`: Auto-generated file containing installed software inventory (one entry per host).
- `manual-software.yml`: Template to manually document external services or unmanaged software (SaaS, databases, mobile apps, etc.).

##  How to Use

The infrastructure is automatically inventoried each time `vagrant up` is performed.

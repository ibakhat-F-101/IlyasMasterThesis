# Service Overview

You will find different folders such as:
- backupScript
- packer
- templates

## BackupScript

This folder allows for the storage of import and export scripts for backing up existing services.

## Packer

It contains the configuration for Packer for provisioning and building the box, along with the script for basic virtual machine setup.

## Templates

These files enable the reuse of templates for service and backup usage, thereby avoiding code duplication.
Services in different domains will only need to modify IP addresses and necessary variables.


## InvoiceNinja
To use backup with this service, user must add the backup playbook to the main service template. The backup template is located in the service/template/invoiceninja folder. The following command can be used to link the backup template to the service
```
include_tasks: ../../../services/templates/invoiceninja/invoiceninjaBackup.yml
```
The variables required for the backup to work must be set in the ansible file that requires the backup:
```
backup_secure: invoiceninja_backup_secure_infra.sql
path_secure: backup(path_to_file)/{{ backup_secure }}
```
The backup is automated with cron job to run every midnight. The backup is saved on the virtual machine itself.
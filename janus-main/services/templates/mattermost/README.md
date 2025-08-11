# Mattermost

## Getting started

I followed the [official documentation](https://docs.mattermost.com/install/install-docker.html#deploy-mattermost-on-docker-for-production-use) to install Mattermost on docker.

## Configuration Files

### Focalboard 

Focalboard is already integrated in Mattermost. This is now called "Boards" in the top-right menu, next to the 'Start call' button.



# Import the backup "mattermost_backup_secure_infra.sql"

## For testing 
Add the variable :

    `path_backup_secure: backup/mattermost_backup_secure_infra.sql`

Add the tasks :

    `- include_tasks: ../../../services/templates/mattermost/mattermostBackup.yml`

And put the backup "mattermost_backup_secure_infra.sql from the old project" in the backup folder.

## To add your own backup
- Create your own backup.sql using the script : backup/export_db.sh/.j2
- Add the "path_backup_secure : {Name of you backup}" variable with the name of your backup 
- Add your backup.sql to the backup folder in the folder mattermost/backup in the user domain
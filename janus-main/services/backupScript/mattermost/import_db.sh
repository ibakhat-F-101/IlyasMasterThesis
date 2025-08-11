#!/bin/bash

# Import an inital db, use another backup file if it's more populated
docker exec -i mattermost_postgres_1 psql -U mmuser -d mattermost -c "DROP SCHEMA public CASCADE; CREATE SCHEMA public;" && cat /opt/mattermost_backup/backup.sql | docker exec -i mattermost_postgres_1 psql -U mmuser -d mattermost
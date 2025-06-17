pg_dump -U user 4forum > /backup/db_$(date +%Y%m%d).sql

tar -czf /backup/files_$(date +%Y%m%d).tar.gz /opt/4forum/uploads

find /backup -type f -mtime +30 -delete

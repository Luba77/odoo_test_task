# Odoo Project

## This project is a web application based on Odoo.

### Instalation

``` bash
git clone https://github.com/Luba77/odoo_test_task
```

### Run docker
``` bash
docker-compose up -d

```

### Init module with db settings
``` bash
docker-compose exec web usr/bin/odoo -i base -d newdb1 --db_host db -r odoo -w pass --stop-after-init
```

### Create odo user
``` bash
docker exec -it odoo_test_task-db-1 /bin/bash

psql -U odoo -d newdb1

UPDATE res_users SET password='new_password' WHERE login='admin';
```

## HOME PAGE:
http://localhost:9001/file_manager_view





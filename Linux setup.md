# 1. Install PostgreSQL
[Official docs](https://docs.djangoproject.com/en/5.0/ref/databases/#postgresql-notes)
Install necessary module, so Django can communicate with PostgreSQL:
```Bash
pip install psycopg2
```

if u have some problems (eg. Failed building wheel for psycopg2), you can try:
```Bash
pip install psycopg2-binary
```

Then install the PostgreSQL:
```Bash
sudo apt install postgresql
sudo apt install postgresql postgresql-contrib
```

Start postgresql process:
```Bash
sudo systemctl start postgresql.service
```
# 2. Configure PostgreSQL
Open **psql** CLI
```Bash
sudo -u postgres psql
```

Create DB:
```SQL
CREATE DATABASE nameDB;
```

Create user:
```SQL
CREATE USER username WITH PASSWORD 'pa$$word';
```

Give him all priveleges:
```SQL
GRANT ALL PRIVILEGES ON DATABASE nameDB TO username;
```

Modify a few settings to optimize DB and django:
```SQL
ALTER ROLE username SET client_encoding TO 'utf8';
ALTER ROLE username SET default_transaction_isolation TO 'read committed';
ALTER ROLE username SET timezone TO 'UTC';
```

Exit SQL prompt:
```SQL
\q
```
# 3. Django

In the [[Settings]].py file edit the DATABASES:
```Python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "OPTIONS": {
            "service": "my_service",
            "passfile": ".my_pgpass",
        },
    }
}
```
if you wish to use the [password file](https://www.postgresql.org/docs/current/libpq-pgpass.html) and the [connection service file](https://www.postgresql.org/docs/current/libpq-pgservice.html).
Passfile stores info in the following way: `hostname:port:database:username:password`

.pg_service.conf:
```
[my_service]
host=localhost
user=USER
dbname=NAME
port=5432
```

.my_pgpass:
```
localhost:5432:NAME:USER:PASSWORD
```
### OR
If you prefer to do it using the specified user
```Python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "nameDB",
        "USER": "username",
        "PASSWORD": 'pa$$word',
        "HOST": '127.0.0.1',
        "PORT": "5432"
    }
}
```






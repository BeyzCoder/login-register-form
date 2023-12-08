This project is a basic structure of how a registering a account get save into the database. This is
solely backend developer stuff have not implemented the frontend of login and register. But in the future
I will implement it.

Languages:
- Python
- SQL

Framework:
- Fastapi

Tools:
- Uvicorn
- Postgres
- Postman
- Docker

'How to use it?'

After cloning this repository, you can straightly go to terminal and do.

```bash
docker-compose up
```

The postgres container will automatically create the database for you.
Then to send a request just go to the Postman or your Browser.

```
localhost:8000/account/register
```

for the body parameter.

```json
{
    "first_name" : "__NAME__",
    "last_name" : "__LAST__",
    "email" : "__EMAIL__",
    "password" : "__PASSWORD__",
}
```
if you want to see if the query got added to the database. Just follow this command on the terminal.

```bash
docker exec -it user-account-db psql -U testdev -d UserAccounts
```

then just type the SQL command.

```sql
SELECT * FROM user_info;
```

These are the basic concept on how register works with database.
I haven't implemented for email validator check, password protection. I will do the if I have spare time.
## How to run the app?
First run the fast api scripts located in sql_api:
```
cd sql_api
pip install -r requirements.txt
cd ..
python3 -m uvicorn sql_api.main:app --reload
```

Next open a new terminal in the project and run the app by running:

```bash
npm install
npm run dev
```

Next run the sql script ```mysql_table_creation_scripts.sql``` then the script labeled ```populate_db.sql```


You can log in with this dummy user:
```
username === user
password === test
```


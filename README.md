## How to run the app?
First run the fast api scripts located in sql_api:
```
cd sql_api
pip install -r requirements.txt
cd ..
uvicorn sql_api.main:app --reload
```

Next open a new terminal in the project and run the app by running:

```bash
npm install
npm run dev
```

You can log in with this dummy user:

```
username === user
password === test
```


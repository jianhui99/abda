# Fund Management System
Directory Structure
```bash
/abda
    ├── .env                    # environment file
    ├── .env.example            # example environment file
    ├── app.py                  # Startup entry
    ├── controllers.py          # Controller logic
    ├── data_handler.py         # Data reading and writing logic
    ├── funds.json              # Store fund data
    ├── init.py                 # init database
    ├── investment_fund.py      # simple class for investment fund
    ├── investment_fund.db      # sqlite database for investment fund
    ├── json_db_to_sqlite3.py   # migrate json to sqlite3
    ├── lang.py                 # app language file
    ├── README_2.md             # Documentation for api and database structure
    ├── README.md               # Documentation for project and task
    ├── response.py             # Response encapsulation
    ├── routes.py               # Routing and interface logic
    ├── test_app.py             # Unit tests for api
    └── test_db.py              # Unit tests for database
```

**Task 1**: Data Model Design Create a Python class for representing an investment fund. The class should have the following attributes:
- Fund ID
- Fund Name
- Fund Manager Name
- Fund Description
- Fund Net Asset Value (NAV)
- Fund Date of Creation
- Fund Performance (as a percentage)
```bash
python3 investment_fund.py
```


**Task 2**: REST API Development Using Python and a web framework of your choice (e.g., Flask or Django), create a RESTful API to manage investment funds. The API should have the following endpoints:
- Endpoint to retrieve a list of all funds
- Endpoint to create a new fund
- Endpoint to retrieve details of a specific fund using its ID
- Endpoint to update the performance of a fund using its ID 
- Endpoint to delete a fund using its ID
```bash
python3 app.py
```

**Task 3**: Data Persistence Implement data persistence using a lightweight database system (e.g., SQLite or JSON file). When a new fund is created or the performance of an existing fund is updated, the data should be stored persistently.
```bash
we use sqlite3 to store the data
```


**Task 4**: SQL Database Schema Design an appropriate database schema to store investment fund data. Create SQL statements to create the necessary tables and relationships.
```bash
we use sqlite3 to create the table
python3 init.py 
```


**Task 5**: SQL Data Migration Write SQL scripts to migrate the data from the lightweight database system (used for Task 3) to the SQL database you designed in Task 4
```bash
task 3 & 4 use the same db, the following script is a simple to show how to migrate json data to sqlite
python3 json_db_to_sqlite3.py 
```


**Task 6**: Error Handling Implement appropriate error handling mechanisms for the API to handle scenarios like invalid input, missing resources, etc.
```bash
{
    "code": 0,
    "data": null,
    "message": "An internal server error occurred."
}

{
    "code": 0,
    "data": null,
    "message": "The request could not be understood or was missing required parameters."
}

{
    "code": 0,
    "data": null,
    "message": "Fund not found!"
}

{
    "code": 0,
    "data": null,
    "message": "Fund name already exists."
}

{
    "code": 0,
    "data": null,
    "message": "Fund performance must be a number."
}

{
    "code": 0,
    "data": null,
    "message": "Missing required field fund_performance."
}

```

**Task 7**: Testing Write test cases to ensure the proper functioning of both the API endpoints and the SQL database. The tests should cover various scenarios and edge cases, including testing the SQL queries and verifying data integrity in the database.
```bash
python3 -m unittest test_app.py
python3 -m unittest test_db.py
```


**Task 8**: Documentation Provide clear and concise documentation for the API and the SQL database, including how to interact with each endpoint, SQL schema, and sample requests and responses.

[README_2.md](README_2.md)
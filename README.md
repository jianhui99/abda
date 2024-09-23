# Fund Management System
Directory Structure
```bash
/abda
    ├── app.py              # Startup entry
    ├── controllers.py      # Controller logic
    ├── response.py         # Response encapsulation
    ├── routes.py           # Routing and interface logic
    ├── data_handler.py     # Data reading and writing logic
    └── funds.json          # Store fund data
```

Task 1: Data Model Design Create a Python class for representing an investment fund. The class should have the following attributes:
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


Task 2: REST API Development Using Python and a web framework of your choice (e.g., Flask or Django), create a RESTful API to manage investment funds. The API should have the following endpoints:
- Endpoint to retrieve a list of all funds
- Endpoint to create a new fund
- Endpoint to retrieve details of a specific fund using its ID
- Endpoint to update the performance of a fund using its ID 
- Endpoint to delete a fund using its ID
```bash
python3 app.py
```

Task 3: Data Persistence Implement data persistence using a lightweight database system (e.g., SQLite or JSON file). When a new fund is created or the performance of an existing fund is updated, the data should be stored persistently.
```bash
we use JSON files as the data persistence implementation of fund data
```


Task 4: SQL Database Schema Design an appropriate database schema to store investment fund data. Create SQL statements to create the necessary tables and relationships.
```bash
we use sqlite3 to create the table
python3 init_db.py 
```


Task 5: SQL Data Migration Write SQL scripts to migrate the data from the lightweight database system (used for Task 3) to the SQL database you designed in Task 4
```bash
python3 json_db_to_sqlite3.py 
```


Task 6: Error Handling Implement appropriate error handling mechanisms for the API to handle scenarios like invalid input, missing resources, etc.


Task 7: Testing Write test cases to ensure the proper functioning of both the API endpoints and the SQL database. The tests should cover various scenarios and edge cases, including testing the SQL queries and verifying data integrity in the database.
```bash
python3 -m unittest test_app.py
python3 -m unittest test_db.py
```


Task 8: Documentation Provide clear and concise documentation for the API and the SQL database, including how to interact with each endpoint, SQL schema, and sample requests and responses.
```bash
README_2.md
```
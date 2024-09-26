# Fund Management System API Reference
## Base URL
http://localhost:5000/api/v1


## Endpoints

### 1. Create Fund
- **Endpoint**: `/funds`
- **Method**: `POST`
- **Description**: Creates a new investment fund.
- **Request Body**:
    ```json
    {
        "fund_name": "string",              // required: the name of the fund
        "fund_manager_name": "string",      // required: the manager's name of the fund
        "fund_description": "string",       // required: the description of the fund
        "fund_nav": 1,                      // required: the net asset value of the fund
        "fund_performance": 1               // optional: the performance of the fund
        "fund_creation_date": "YYYY-MM-DD", // optional: the creation date of the fund
    }
    ```
- **Response**:
    - **Status Code**: `201 Created` on success.
    - **Body**:
    ```json
    {
        "code": 201,
        "data": {
            "fund_id": 1,
            "fund_name": "string",
            "fund_manager_name": "string",
            "fund_description": "string",
            "fund_nav": 1,
            "fund_creation_date": "YYYY-MM-DD",
            "fund_performance": 1,
            "created_at": "timestamp",
            "updated_at": "timestamp"
        },
        "message": "Fund created successfully!"
    }
    ```

### 2. Retrieve All Funds
- **Endpoint**: `/funds`
- **Method**: `GET`
- **Description**: Retrieves a list of all investment funds.
- **Response**:
    - **Status Code**: `200 OK`
    - **Body**:
    ```json
    {
        "code": 200,
        "data": [
            {
                "fund_id": 1,
                "fund_name": "string",
                "fund_manager_name": "string",
                "fund_description": "string",
                "fund_nav": 1,
                "fund_creation_date": "YYYY-MM-DD",
                "fund_performance": 1,
                "created_at": "timestamp",
                "updated_at": "timestamp"
            },
            ...
        ],
        "message": "Funds retrieved successfully!"
    }
    ```

### 3. Retrieve Fund by ID
- **Endpoint**: `/funds/{id}`
- **Method**: `GET`
- **Description**: Retrieves details of a specific fund using its ID.
- **Response**:
    - **Status Code**: `200 OK` on success, `404 Not Found` if not found.
    - **Body**:
    ```json
    {
        "code": 200,
        "data": {
            "fund_id": 1,
            "fund_name": "string",
            "fund_manager_name": "string",
            "fund_description": "string",
            "fund_nav": 1,
            "fund_creation_date": "YYYY-MM-DD",
            "fund_performance": 1,
            "created_at": "timestamp",
            "updated_at": "timestamp"
        },
        "message": "Fund retrieved successfully!"
    }
    ```

### 4. Update Fund Performance
- **Endpoint**: `/funds/{id}/performance`
- **Method**: `PUT`
- **Description**: Updates the performance of a fund using its ID.
- **Request Body**:
    ```json
    {
        "fund_performance": 1
    }
    ```
- **Response**:
    - **Status Code**: `200 OK` on success, `404 Not Found` if not found.
    - **Body**:
    ```json
    {
        "code": 200,
        "message": "Fund performance updated successfully!"
    }
    ```

### 5. Delete Fund
- **Endpoint**: `/funds/{id}`
- **Method**: `DELETE`
- **Description**: Deletes a fund using its ID.
- **Response**:
    - **Status Code**: `200 OK` on success, `404 Not Found` if not found.
    - **Body**:
    ```json
    {
        "code": 200,
        "message": "Fund deleted successfully!"
    }
    ```

## Error Responses
- Common error responses include:
    - **400 Bad Request**: Missing required fields or invalid input.
    - **404 Not Found**: Fund ID does not exist.
    - **500 Internal Server Error**: Server error occurred.

# SQL Database Documentation

## Database Schema

### Table: `investment_funds`
| Column Name          | Data Type         | Constraints                     |
|---------------------|-------------------|---------------------------------|
| `fund_id`           | INTEGER           | PRIMARY KEY AUTOINCREMENT       |
| `fund_name`         | TEXT              | NOT NULL                        |
| `fund_manager_name` | TEXT              | NOT NULL                        |
| `fund_description`  | TEXT              |                                 |
| `fund_nav`          | DECIMAL(15, 4)    | NOT NULL                        |
| `fund_creation_date`| DATE              | NOT NULL                        |
| `fund_performance`   | DECIMAL(10, 4)    | NOT NULL                        |
| `fund_status`     | INT                  | NOT NULL DEFAULT 1            |
| `created_at`        | TEXT              | DEFAULT (DATETIME('now'))      |
| `updated_at`        | TEXT              | DEFAULT (DATETIME('now'))      |

## SQL Commands

### Create Table
```sql
CREATE TABLE IF NOT EXISTS investment_funds (
    fund_id INTEGER PRIMARY KEY AUTOINCREMENT,
    fund_name TEXT NOT NULL,
    fund_manager_name TEXT NOT NULL,
    fund_description TEXT,
    fund_nav DECIMAL(15, 4) NOT NULL,
    fund_creation_date DATE NOT NULL,
    fund_performance DECIMAL(10, 4) NOT NULL,
    fund_status INT NOT NULL DEFAULT 1,
    created_at TEXT NOT NULL DEFAULT (DATETIME('now', 'localtime')),
    updated_at TEXT NOT NULL DEFAULT (DATETIME('now', 'localtime'))
);
```

## Sample Queries
### 1. Insert a Fund:
```sql
INSERT INTO investment_funds (fund_name, fund_manager_name, fund_desc, fund_nav, fund_creation_date, fund_performance)
VALUES ('Sample Fund', 'Manager X', 'Description of the fund', 1500.00, '2023-01-01', 5.0);
```

### 2. Select All Funds:
```sql
SELECT * FROM investment_funds;
```

### 3. Update Fund Performance:
```sql
UPDATE investment_funds SET fund_performance = 6.0 WHERE fund_id = 1;
```

### 4. Delete a Fund:
```sql
DELETE FROM investment_funds WHERE fund_id = 1;
```


## Conclusion
This documentation provides a clear guide on how to interact with the API and the SQL database. By following the examples and the schema, you can effectively use the endpoints and maintain data integrity in your database.

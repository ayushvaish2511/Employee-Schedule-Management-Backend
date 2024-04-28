# Employee Scheduling Backend

This project provides a backend system for managing employee schedules in a retail store chain. It is built using Python FastAPI and MongoDB.

## Features

### Employee Management
- Create new employees
- Update employee information

### Shift Management
- Create new shifts
- Retrieve shifts for a specific period

### Employee Scheduling
- Assign shifts to employees
- View employee schedules for a specific period

## Installation

1. Clone the repository:

```git clone https://github.com/ayushvaish2511/Employee-Schedule-Management-Backend.git```

2. Navigate to the project directory:

```cd employee-scheduling-backend```

3. Create Virtual Environment:

```python -m venv EmployeeScheduleManagementVENV```

4. Install the dependencies:

```pip install -r requirements.txt```


## Running the Application

1. Start the FastAPI server:

```uvicorn app.main:app --reload```

This will start the server at `http://localhost:8000` by default.

2. You can now access the API documentation using your browser or API client:

`http://localhost:8000/docs`


## Usage

1. Use the provided API endpoints to create employees, create shifts, assign shifts to employees, and view employee schedules.
2. Make requests to the API endpoints using tools like cURL, Postman, or your preferred HTTP client.



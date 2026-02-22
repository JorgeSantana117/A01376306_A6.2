# Hotel Management System

A robust, PEP8-compliant Python application for managing hotels, customers, and reservations. This system features persistent storage using JSON files and includes a comprehensive suite of unit tests with high code coverage.

## Features

- **Hotel Management**: Create, delete, modify, and display hotel information.
- **Customer Management**: Handle customer profiles and contact details.
- **Reservation System**: Book and cancel rooms with real-time occupancy updates.
- **Data Persistence**: All data is stored in the `/data` directory in JSON format.
- **Error Resilience**: Gracefully handles corrupted or missing data files without crashing.

## Project Structure

```text
A01376306_A6.2/
├── data/               # Persistent JSON storage
├── models.py           # Entity abstractions (Hotel, Customer, Reservation)
├── managers.py         # Business logic and file persistence
├── main.py             # CLI - User Interaction
└── test_system.py      # Unit tests (unittest framework)
```

## Getting Started

### Prerequisites
- Python 3.x
- `coverage` library (for testing reports)
- `pylint` (for code quality verification)

### Running the Application
To interact with the system via the Command Line Interface:
```bash
python main.py
```

## Testing & Quality Assurance

### Running Unit Tests
To run the automated test suite:
```bash
python test_system.py
```

### Code Coverage
To verify that the tests cover at least 85% of the logic:
```bash
pip install coverage
coverage run test_system.py
coverage report -m
```

### Code Quality (Pylint)
This project is optimized for PEP8 compliance. To check the code quality rating:
```bash
pylint models.py managers.py main.py test_system.py
```

## Error Handling
The system includes a BaseManager that implements a try-except mechanism. If a JSON file becomes corrupted or contains invalid data, the system will:
1. Print a specific error message to the console.
2. Continue execution with an empty dataset instead of crashing.

---
**Developer:** Jorge Santana (A01376306)
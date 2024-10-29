# Bank Account Example - Unit Testing with Coverage in Python

This Python project demonstrates unit testing and code coverage using a simple `BankAccount` class. The project includes methods for depositing, withdrawing, and transferring funds with basic validation rules. We will implement unit tests using [JUnit](https://junit.org/junit5/), and we will measure code coverage with [JaCoCo](https://www.jacoco.org/jacoco/trunk/doc/).

Note that the pom.xml file is already configured to run JaCoCo.

## Prerequisites

- **Python 3.6** or later
- **pip** (Python’s package installer)

## Getting Started

1. **Clone the Repository**: Clone the project to your local machine.
    ```bash
    git clone <repository-url>
    cd <your-project-directory>
    ```

2. **Create a virtual environment and install requirements**:

```
python3 -m venv .venv
source ./.venv/bin/activate
pip install -r requirements.txt
```

3. Run the unit tests

```bash
python -m unittest
```

4. Generate a coverage report

```
coverage run -m unittest
coverage html
```

The first command will generate the coverage report in your terminal. The second will generate an html file in `htmlcov/index.html` which you can view in your browser.

## Your Task

Add tests to `bank_account.py` to achieve 100% statement and branch coverage for the BankAccount class.

# Triangle Classification Testing

## Overview

This project implements a function to classify triangles based on the lengths of their sides. The program includes unit tests and static analysis to ensure code quality and coverage.

## Features

- Identifies **Right, Isosceles, Equilateral, and Scalene triangles**.
- Detects **invalid side lengths** and **non-triangle cases**.
- Uses **Pylint** for static code analysis.
- Uses **pytest & coverage.py** for unit testing and code coverage analysis.

## Installation

Ensure you have Python installed, then install the required dependencies:

```bash
pip install pylint pytest coverage
```

## Running Static Analysis (Pylint)

Run Pylint to analyze the code for style and errors:

```bash
pylint triangle_new.py
```

## Running Tests

To execute the test cases, use:

```bash
pytest test_triangle_new.py
```

## Checking Code Coverage

To measure test coverage, run:

```bash
coverage run -m pytest test_triangle_new.py
coverage report -m
```

For a detailed HTML report:

```bash
coverage html
start htmlcov/index.html  # Open in a browser (Windows)
open htmlcov/index.html    # (Mac/Linux)
```

## Project Structure

```
│── triangle_new.py          # Triangle classification function
│── test_triangle_new.py     # Unit tests for classification
│── README.md                # Project documentation
```

## Deliverables

1. **GitHub Repository**: [Insert Repo URL]
2. **Pylint Reports**:
   - Before and after fixing issues.
3. **Coverage Reports**:
   - Initial and final results (>80% coverage).
4. **List of additional test cases added** to improve coverage.

## Contributors

- [Your Name]

## License

This project is licensed under the MIT License.

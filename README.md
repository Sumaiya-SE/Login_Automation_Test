# 🔐 Login Automation Testing

This project demonstrates automation testing for web applications using Selenium and Pytest.
The main goal is to practice real-world QA workflows. The project focuses on the SauceDemo demo website, simulating a typical login flow that QA engineers encounter in industry.

## Tools Used
- Python 3.x
- Selenium WebDriver
- Pytest + pytest-html

## Test Cases
| Test | Expected Result |
|------|----------------|
| Valid login | Redirects to inventory page |
| Invalid password | Error message shown |
| Locked out user | Locked out error shown |
| Empty fields | Validation error shown |

## How to Run
```bash
pip install -r requirements.txt
pytest tests/ --html=reports/report.html
Open the report.html in a browser to view test results.
```

## Learning Outcomes
- Practiced automation script writing and locating web elements
- Learned test validation and assertion handling
- Gained experience in organizing tests using POM
- Generated test reports to simulate real QA documentation
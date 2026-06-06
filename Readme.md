# Library Management Playwright Automation

## Overview

This project contains automated end-to-end test scripts developed using **Python** and **Playwright** to validate critical workflows within the Library Management System's Student Portal.

The current automation covers the complete student journey from login to story submission in the **WorldSmith** module, reducing manual testing effort and ensuring application reliability.

---

## Features

* Automated student login workflow
* Browser launch in maximized mode
* Form interaction and validation
* Navigation across application modules
* WorldSmith story creation
* Multiline content submission
* Automated page scrolling
* Story submission workflow validation

---

## Technology Stack

* Python 3.x
* Playwright
* Chromium Browser

---

## Prerequisites

Install Playwright:

```bash
pip install playwright
```

Install browser binaries:

```bash
playwright install
```

---

## Automated Workflow

### Student Login

The automation performs the following actions:

* Opens the Student Login page
* Enters Admission Number
* Enters Username
* Enters Password
* Toggles password visibility
* Submits the login form

### WorldSmith Story Submission

After successful login, the automation:

* Navigates to the WorldSmith module
* Enters a story title
* Adds multiline story content
* Scrolls to access the submission section
* Submits the story successfully

---

## Test Objective

The objective of this automation is to verify that a student can:

1. Log in successfully.
2. Access the WorldSmith module.
3. Create a new story.
4. Submit story content without errors.
5. Complete the end-to-end workflow successfully.

---

## Project Structure

```text
project/
│
├── main.py
├── requirements.txt
├── README.md
└── playwright.config
```

---

## Future Enhancements

* Implement Page Object Model (POM)
* Add automated assertions
* Generate execution reports
* Capture screenshots on failure
* Integrate with CI/CD pipelines
* Add cross-browser testing support
* Add email OTP automation support

---

## Author

Hemanth HB

Playwright Automation | Python Automation Testing | QA

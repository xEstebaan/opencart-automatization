# 🟠 OrangeHRM Test Automation

> Automation framework built to practice and sharpen real-world QA engineering skills — structured, scalable, and containerized.

![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=flat-square&logo=python&logoColor=white)
![Selenium](https://img.shields.io/badge/Selenium-4.x-43B02A?style=flat-square&logo=selenium&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-7.x-0A9EDC?style=flat-square&logo=pytest&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?style=flat-square&logo=docker&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-Database-4479A1?style=flat-square&logo=mysql&logoColor=white)
![Status](https://img.shields.io/badge/Status-In%20Progress-orange?style=flat-square)

---

## 📌 About the Project

This project automates the main functional flows of **OrangeHRM** — an open-source Human Resources Management system. The primary goal is to practice and consolidate skills in test automation using industry-standard tools and patterns.

The entire environment runs **locally via Docker**, keeping the setup clean, reproducible, and independent from external dependencies.

---

## 🏗️ Tech Stack

| Layer            | Technology              |
| ---------------- | ----------------------- |
| Language         | Python 3.11             |
| Automation       | Selenium WebDriver      |
| Test Runner      | Pytest                  |
| Design Pattern   | Page Object Model (POM) |
| Containerization | Docker + Docker Compose |
| Database         | MySQL                   |
| Application      | OrangeHRM (self-hosted) |

---

## 🐳 Local Environment

The application runs fully containerized. A single `docker-compose up` spins up both the OrangeHRM instance and its MySQL database — no external services, no cloud dependencies.

```bash
docker-compose up -d
```

---

## 📁 Project Structure

```
orangeHRM-automatization/
│
├── pages/
│   ├── __init__.py
│   ├── base_page.py
│   └── login_page.py
│
├── tests/
│   ├── __init__.py
│   └── test_login.py
│
├── test_cases/
│   └── authentication/
│       ├── login.md
│       ├── logout.md
│       └── register.md
│
├── components/
│   └── .md
│
├── utils/
│   ├── __init__.py
│   └── config.py
│
├── conftest.py
├── docker-compose.yml
├── pytest.ini
├── README.md
└── requirements.txt
```

---

## 🧪 Automated Test Flows

| #   | Module            | Flow                               | Status         |
| --- | ----------------- | ---------------------------------- | -------------- |
| 01  | 🔐 Authentication | Login with valid credentials       | ✅ Done        |
| 02  | 🔐 Authentication | Login with invalid credentials     | ✅ Done        |
| 03  | 🔐 Authentication | Logout from dashboard              | 🔄 In Progress |
| 04  | 👤 My Info        | View and edit personal information | 🔄 In Progress |
| 05  | 👥 PIM            | Create new employee                | 🔄 In Progress |
| 06  | 👥 PIM            | Search employee by name/ID         | 🔄 In Progress |
| 07  | 👥 PIM            | Edit employee information          | 🔄 In Progress |
| 08  | 👥 PIM            | Delete employee                    | 🔄 In Progress |
| 09  | 🏖️ Leave          | Submit leave request               | 🔄 In Progress |
| 10  | 🏖️ Leave          | Approve / reject leave             | 🔄 In Progress |
| 11  | ⏱️ Time           | Add attendance record              | 🔄 In Progress |
| 12  | 📋 Recruitment    | Create job vacancy                 | 🔄 In Progress |
| 13  | 📋 Recruitment    | Add candidate                      | 🔄 In Progress |
| 14  | ⚙️ Admin          | Create system user                 | 🔄 In Progress |
| 15  | ⚙️ Admin          | Assign roles and permissions       | 🔄 In Progress |

## 🧠 Design Pattern — POM

The project follows a **Page Object Model** architecture with a `BasePage` that holds shared navigation components (top nav and side nav), inherited by all authenticated pages. This keeps selectors centralized and tests clean.

```python
# Every authenticated page inherits the navs automatically
class DashboardPage(BasePage):
    def __init__(self, page):
        super().__init__(page)  # topNav + sideNav included
        ...
```

---

## 🎯 Goals

- [x] Set up local environment with Docker
- [x] Implement POM structure with BasePage pattern
- [x] Automate login flow (positive & negative cases)
- [ ] Complete all functional flows
- [ ] Add HTML reporting
- [ ] Add CI/CD pipeline (GitHub Actions)

---

## 👨‍💻 Author

Built with purpose — to grow as a QA Automation Engineer.

> _"Good tests don't just find bugs — they prevent them."_

# WorkHub – Employee IT Helpdesk Management System

A full-stack web application built using **Python, Django, SQLite, HTML, and Tailwind CSS** to manage employee IT support requests efficiently.

## Project Overview

WorkHub is an employee IT helpdesk management system designed to simplify the process of reporting, tracking, and managing technical support issues within an organization.

Employees can submit support tickets, while administrators can manage departments, employees, ticket assignments, priorities, and resolution statuses.

## Features

- **Dashboard:** View total, open, in-progress, and resolved ticket counts, along with recent support requests.
- **Ticket Management:** Create and view support tickets with categories, priorities, and descriptions.
- **Ticket Details:** View individual tickets, including assigned support employees and timestamps.
- **Search and Filters:** Search tickets by subject and filter by status and priority.
- **Admin Management:** Manage departments, employees, ticket assignments, and ticket statuses through Django Admin.
- **Responsive UI:** Clean, responsive interface using Tailwind CSS.

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Django | Web framework |
| SQLite | Database |
| HTML | Template structure |
| Tailwind CSS | Frontend styling |
| Django ORM | Database operations |
| Git & GitHub | Version control |

## Project Structure

```text
workhub/
├── helpdesk/
│   ├── migrations/
│   ├── templates/
│   │   └── helpdesk/
│   │       ├── base.html
│   │       ├── dashboard.html
│   │       ├── ticket_create.html
│   │       ├── ticket_list.html
│   │       └── ticket_detail.html
│   ├── admin.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── workhub/
│   ├── settings.py
│   └── urls.py
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation and Setup

**1. Clone the repository**

```bash
git clone https://github.com/atiya234/workhub-django-helpdesk.git
cd workhub-django-helpdesk
```

**2. Create a virtual environment**

```bash
python -m venv venv
```

Activate it on Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

**3. Install dependencies**

```bash
python -m pip install -r requirements.txt
```

**4. Configure the Django secret key**

Set a `DJANGO_SECRET_KEY` environment variable before starting Django.

For example, in Windows PowerShell:

```powershell
$env:DJANGO_SECRET_KEY = Read-Host "Enter Django secret key"
```

Use a securely generated secret key. Do not commit it to GitHub.

**5. Apply migrations**

```bash
python manage.py migrate
```

**6. Create an admin account**

```bash
python manage.py createsuperuser
```

**7. Run the development server**

```bash
python manage.py runserver
```

Open `http://127.0.0.1:8000/` to access WorkHub.

## Main Pages

| Page | URL |
|---|---|
| Dashboard | `/` |
| Create Ticket | `/tickets/create/` |
| All Tickets | `/tickets/list/` |
| Ticket Details | `/tickets/1/` |
| Django Admin | `/admin/` |

The ticket detail URL uses the ID of an existing ticket.

## Future Enhancements

- Employee authentication and role-based access
- Dedicated support-agent dashboard
- Ticket pagination
- Email notifications
- Deployment to a production hosting platform

## Author

**Atiya Nishat**

Computer Science Graduate | Python Full Stack Developer

GitHub: https://github.com/atiya234

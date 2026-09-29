# Django Learning API

A Django REST API project for managing students, teachers and course-related data.

**Stack:** Python · Django · Django REST Framework · SQLite / PostgreSQL

## What is included

- Student and teacher CRUD endpoints.
- Models for courses, lessons, assignments, submissions and test results.
- Django admin for inspecting and managing records.
- Gunicorn, WhiteNoise and Render configuration files.

The assignment-related models describe the data structure; they do not by themselves provide a sandboxed code-execution service.

## Run locally

Use Python 3.11 or 3.12. Run the following from the repository root:

```bash
git clone https://github.com/NurmuhammaddAliyev/django_project.git
cd django_project
python -m venv .venv
```

Activate the environment:

```powershell
# Windows PowerShell
.venv\Scripts\Activate.ps1
```

```bash
# macOS / Linux
source .venv/bin/activate
```

Then install the root dependency file and start Django:

```bash
python -m pip install -r requirements.txt
python config/manage.py migrate
python config/manage.py createsuperuser
python config/manage.py runserver
```

Open [Django admin](http://127.0.0.1:8000/admin/) or [students API](http://127.0.0.1:8000/api/student/).
SQLite is used locally when `DATABASE_URL` is unset.

## API routes

| Route | Purpose |
| --- | --- |
| `/api/student/` | List students |
| `/api/student/<id>/` | Student detail |
| `/api/create_student/` | Create a student |
| `/api/update_student/<id>/` | Update a student |
| `/api/delete_student/<id>/` | Delete a student |
| `/api/teacher/` | List teachers |
| `/api/teacher/<id>/` | Teacher detail |

Teacher create, update and delete routes follow the same naming pattern. See [API routes](config/api/urls.py) and [views](config/api/views.py) for request methods and fields.

## Project structure

```text
config/
  all/          Domain models and application views
  api/          REST serializers, views and routes
  config/       Django settings and project URLs
  manage.py
requirements.txt
render.yaml
```

## Checks and deployment

```bash
python config/manage.py check
python config/manage.py test all
```

Automated test coverage is currently limited. The root `requirements.txt` is the runtime installation entry point; `config/requirements.txt` also contains development tooling.

Before deployment, configure `SECRET_KEY`, `DEBUG=False` and the database connection, restrict `ALLOWED_HOSTS`, and review API permissions. The Render configuration is a starting point and needs a matching database service.

## Author

[Nurmuhammad Aliyev](https://github.com/NurmuhammaddAliyev) · [Telegram](https://t.me/nurmuhammad252505)

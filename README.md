# 📚 AI Humanizer Tool (Backend)

AI Humanizer Tool transforms AI-generated text into natural, human-like content, bypassing AI detectors (like ZeroGPT, Turnitin, Originality.ai) while preserving quality and originality.  
It supports multilingual humanization, sentence-level editing, PDF/DOCX export, and secure API usage via API keys.

---

## ✨ Features

- User Registration and Login (with automatic API Key generation)
- Submit AI-generated text for humanization
- Detection evasion mode to bypass AI detectors
- Plagiarism check integration (dummy implementation, pluggable with real APIs)
- Asynchronous processing with Celery and Redis
- Save original and humanized content history
- Usage tracking with daily/monthly API rate limits
- Admin Panel for monitoring submissions, banned phrases, and flagged content
- Export humanized content as **PDF** or **DOCX**
- Support for **multiple languages** (via Google Translate)
- Sentence-by-sentence humanization editor API

---

## 🚀 Technology Stack

- **Backend Framework:** Django, Django REST Framework
- **Task Queue:** Celery
- **Message Broker & Backend:** Redis
- **Translation API:** Google Translate (via `googletrans`)
- **Database:** Default SQLite (can upgrade to PostgreSQL)
- **Document Export:** `python-docx`, `reportlab`

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd ai_humanizer
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate   # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file:

```env
SECRET_KEY=your-django-secret-key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
CELERY_BROKER_URL=redis://localhost:6379/0
CELERY_RESULT_BACKEND=redis://localhost:6379/0
```

### 5. Run Migrations

```bash
python manage.py migrate
```

### 6. Run Django and Celery

Start Django server:
```bash
python manage.py runserver
```

Start Celery worker:
```bash
celery -A config worker -l info
```

---

## 📬 API Endpoints

| Endpoint | Method | Description |
|:--------|:------|:------------|
| `/api/auth/register/` | POST | Register a new user and receive an API key |
| `/api/auth/login/` | POST | Log in and receive an API key |
| `/api/humanize-text/` | POST | Submit text for humanization |
| `/api/task-status/<task_id>/` | GET | Check the status of the humanization task |
| `/api/export/<submission_id>/?format=pdf` | GET | Export a submission as PDF |
| `/api/export/<submission_id>/?format=docx` | GET | Export a submission as DOCX |
| `/api/sentence-editor/` | POST | Humanize text sentence-by-sentence |

### Authentication
All endpoints (except register/login) require an `x-api-key` header.

Example:

```bash
x-api-key: your-generated-api-key
```

---

## 📂 Postman Collection

Download the ready-to-import Postman Collection:  
(**You already have** ➔ `AI_Humanizer_API.postman_collection.json`)

---

## 📦 Deployment (Optional)

Prepare for production by:
- Setting `DEBUG=False` in `.env`
- Using PostgreSQL instead of SQLite
- Adding a `Procfile` for deployment to Heroku, Railway, etc.
- Running `python manage.py collectstatic` for static files

---

## 👨‍💻 Contribution Guidelines

- Create feature branches from `main`
- Follow consistent commit message format (first word capitalized only)
- Ensure all API endpoints are documented and tested

---

## 📄 License

This project is licensed under the MIT License — feel free to use, modify, and distribute with proper attribution.
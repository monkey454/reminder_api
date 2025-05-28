# ⏰ Reminder API

A secure, modular, and RESTful Flask API to manage personal reminders. Users can register, log in, and perform full CRUD operations on their reminders. The app uses JWT for authentication and SQLAlchemy with SQLite as the default database.

---

## 🧰 Features

- 🔐 JWT Authentication
- 🔄 Full CRUD for Reminders
- 🧱 Modular Blueprint Architecture
- 🔧 Environment-Based Config
- 📅 ISO Format Due Dates

---

## 🧪 API Endpoints

### 🔐 Auth Routes

| Method | Endpoint        | Description         |
|--------|------------------|---------------------|
| POST   | `/auth/register` | Register new user   |
| POST   | `/auth/login`    | Login and get token |

---
### ⏰ Reminder Routes *(Protected with JWT)*

| Method | Endpoint                  | Description              |
|--------|---------------------------|--------------------------|
| GET    | `/reminders`          | Get all user reminders   |
| POST   | `/reminders`          | Create a new reminder    |
| GET    | `/reminders/<id>`     | Get specific reminder    |
| PATCH  | `/reminders/<id>`     | Update specific reminder |
| DELETE | `/reminders/<id>`     | Delete specific reminder |

---
## 📦 Requirements

1. **Clone the repository**  
   ```bash
   git clone https://github.com/your-username/reminder_api.git
   cd reminder_api
2. **Install virtual environment**
   ```bash
   python -m venv venv
   venv/bin/activate
1. **Inatall dependencies**  
   ```bash
    pip install -r requirements.txt

## 🛠️ Create a .env file


   




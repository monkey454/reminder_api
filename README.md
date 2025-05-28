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
| POST   | `/api/register` | Register new user   |
| POST   | `/api/login`    | Login and get token |

---
### ⏰ Reminder Routes *(Protected with JWT)*

| Method | Endpoint                  | Description              |
|--------|---------------------------|--------------------------|
| GET    | `/api/reminders`          | Get all user reminders   |
| POST   | `/api/reminders`          | Create a new reminder    |
| GET    | `/api/reminders/<id>`     | Get specific reminder    |
| PATCH  | `/api/reminders/<id>`     | Update specific reminder |
| DELETE | `/api/reminders/<id>`     | Delete specific reminder |

---
## 📦 Requirements

1. **Clone the repository**  
   ```bash
   git clone https://github.com/yourusername/flask-todo-app.git
   cd flask-todo-app
2. **Install virtual environment**
   ```bash
   python -m venv venv
   venv/bin/activate
1. **Inatall dependencies**  
   ```bash
    pip install -r requirements.txt

## 🛠️ Create a .env file


   




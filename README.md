# 📝 TODO LIST Web App

A simple and elegant To-Do List web application built using **Django**, **HTML**, and **CSS**. Users can add, view, and delete tasks with details and timestamps.

---

## 🚀 Features

- ✅ Add tasks with:
  - Title
  - Description
  - Timestamp
- 🗑️ Delete tasks
- 📋 View all tasks in a card-style layout
- 🎨 Clean and responsive UI using custom CSS

---

## 🛠️ Tech Stack

- **Backend:** Django (Python)
- **Frontend:** HTML, CSS
- **Database:** Default Django SQLite (can be switched)

---

todo_app/
│
├── todo/ # Django app
│ ├── migrations/
│ ├── templates/
│ │ └── todo/
│ │ └── index.html
│ ├── static/
│ │ └── todo/
│ │ └── styles.css
│ ├── models.py # Task model
│ ├── views.py # Logic for adding/removing tasks
│ ├── urls.py # App URL routing
│
├── todo_app/ # Project config
│ ├── settings.py
│ ├── urls.py
│
├── db.sqlite3 # Default database
└── manage.py


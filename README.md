# Blog CRUD Application

A modern Blog CRUD (Create, Read, Update, Delete) web application built using **Flask**, featuring image uploads and a clean pastel UI.

---

## ✨ Features

- Create blog posts with:
  - Title
  - Author
  - Content
  - Optional image upload
- View all blog posts on the home page
- View individual blog details
- Edit existing blog posts
- Delete blog posts
- Created & updated timestamps
- Modern pastel UI design

---

## 🛠️ Tech Stack

- Python
- Flask
- HTML, CSS
- Virtual Environment (venv)

---

## 📁 Project Structure

blog-crud-app/
│
├── app.py
├── manage.py
├── requirements.txt
├── .gitignore
├── .env.example
├── README.md
│
├── static/
│ ├── css/
│ │ └── style.css
│ └── assets/
│
├── templates/
│ ├── index.html
│ ├── add-edit.html
│ └── view.html
│
├── media/
│ └── uploads/
│
└── venv/ (ignored)


---

## 🚀 How to Run Locally

1. Clone the repository
```bash
git clone https://github.com/PiArch/blog-crud-app.git
cd blog-crud-app

2. Create and activate virtual environment

python -m venv venv
venv\Scripts\activate


3. Install dependencies

pip install -r requirements.txt


4. Run the application

python manage.py


5. Open your browser and visit:

http://127.0.0.1:5000
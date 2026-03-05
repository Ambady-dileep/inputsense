# InputSense – Django Form Validation Game

InputSense is a small Django web application that turns **form validation into a mini-game**.

Users must submit valid **name, email, and password** inputs while having a limited number of attempts. The application tracks **score and attempts using Django sessions**.

This project demonstrates practical usage of **Django Forms, custom validation logic, sessions, and Tailwind UI design**.

---

## Live Demo

Deployed on Render

https://inputsense.onrender.com

---

## Features

* Custom Django Form validation
* Field-level validation (`clean_<field>()`)
* Cross-field validation (`clean()`)
* Session-based scoring system
* Limited attempts system (**3 attempts per session**)
* Form lock when attempts are exhausted
* Reset session functionality
* Tailwind CSS glassmorphism UI
* Responsive design
* Django unit tests

---

## How the Game Works

1. User starts with **3 attempts**
2. If validation fails → **attempts decrease**
3. If validation succeeds:

   * **Score increases**
   * User is redirected to the success page
4. When attempts reach **0**, the form becomes locked
5. Clicking **Reset** clears the session and restarts the game

---

## Validation Rules

### Name

* Only alphabetical characters allowed
* Minimum **3 characters**
* Maximum **20 characters**
* Cannot contain **3 consecutive vowels**

Example invalid names:

```
Aei
John123
```

---

### Email

* Must follow valid email format
* Temporary domains like:

```
@tempmail.com
```

are rejected.

---

### Password

Must contain:

* Minimum **8 characters**
* At least **one uppercase letter**
* At least **one number**

Example valid password:

```
SecurePass1
```

---

### Cross-Field Validation

Additional security rules:

* Password **cannot contain the user's name**
* Email username **cannot be identical to the name**

Example:

```
Name: john
Email: john@gmail.com ❌
Password: john12345 ❌
```

---

## Tech Stack

### Backend

* Python
* Django

### Frontend

* HTML
* Tailwind CSS

### State Management

* Django Sessions

### Testing

* Django Test Framework

---

## Project Structure

```
inputsense/
│
├── inputsense/        # Django project settings
│
├── validator/         # Main application
│   ├── forms.py
│   ├── views.py
│   ├── urls.py
│   ├── tests.py
│
├── templates/
│   └── validator/
│       ├── form.html
│       └── success.html
│
├── static/
│
├── manage.py
│
├── requirements.txt
│
└── build.sh
```

---

## Installation

Clone the repository

```
git clone https://github.com/Ambady-dileep/inputsense.git
cd inputsense
```

Create virtual environment

```
python -m venv venv
```

Activate environment

Windows

```
venv\Scripts\activate
```

Mac/Linux

```
source venv/bin/activate
```

Install dependencies

```
pip install -r requirements.txt
```

Run migrations

```
python manage.py migrate
```

Run development server

```
python manage.py runserver
```

Open in browser

```
http://127.0.0.1:8000/
```

---

## Running Tests

```
python manage.py test validator
```

---

## Deployment

This project is deployed using:

* Render (cloud hosting)
* Gunicorn (WSGI server)
* WhiteNoise (static file serving)

Deployment includes:

* GitHub integration
* Automated build script (`build.sh`)
* Static file collection
* Database migrations
* Gunicorn production server

---

## Future Improvements

Possible upgrades:

* User authentication system
* Leaderboard scoring system
* Persistent database storage
* API version using Django REST Framework
* Password strength meter
* Rate limiting

---

## Learning Goals

This project was built to practice:

* Django Form validation
* Session management
* Backend logic design
* Deployment workflows
* Debugging production issues

---

## License

This project is open-source and available under the **MIT License**.

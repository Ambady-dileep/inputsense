# InputSense – Django Form Validation Game

InputSense is a small Django web application that turns form validation into a mini game.

Users must submit valid **name, email, and password** inputs while having a limited number of attempts. The application tracks score and attempts using Django sessions.

This project focuses on learning **Django Forms, validation logic, sessions, and UI design** using Tailwind.

---

## Features

- Custom Django Form validation
- Field-level validation (`clean_<field>()`)
- Cross-field validation (`clean()`)
- Score tracking
- Limited attempts system (3 tries per session)
- Session-based state management
- Lock system after attempts are exhausted
- Reset functionality
- Modern glassmorphism UI using Tailwind CSS
- Responsive layout
- Django test integration

---

## How the Game Works

1. User starts with **3 attempts**.
2. If form validation fails → attempts decrease.
3. If form validation succeeds:
   - Score increases
   - User is redirected to success page.
4. When attempts reach **0**, the form becomes locked.
5. Reset button clears the session and restarts the game.

---

## Validation Rules

### Name
- Only alphabetical characters allowed
- Minimum 3 characters
- Maximum 20 characters
- Cannot contain **3 consecutive vowels**

### Email
- Must be a valid email format
- Temporary email domains like `@tempmail.com` are rejected

### Password
- Minimum 8 characters
- Must contain:
  - At least one uppercase letter
  - At least one number

### Cross-field validation
- Password cannot contain the user's name
- Email username cannot be the same as the name

---

## Tech Stack

Backend:
- Python
- Django

Frontend:
- HTML
- Tailwind CSS

State Management:
- Django Sessions

Testing:
- Django Test Framework

---

## Project Structure
inputsense/
│
├── inputsense/ # Django project settings
│
├── validator/ # Main application
│ ├── forms.py
│ ├── views.py
│ ├── urls.py
│ ├── tests.py
│
├── templates/
│ └── validator/
│ ├── form.html
│ └── success.html
│
├── manage.py


---

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/inputsense.git
cd inputsense

Create virtual environment

python -m venv venv

Activate environment

Windows

venv\Scripts\activate

Mac/Linux

source venv/bin/activate

Install dependencies

pip install django

Run migrations

python manage.py migrate

Run server

python manage.py runserver

Open in browser

http://127.0.0.1:8000/
Running Tests
python manage.py test validator
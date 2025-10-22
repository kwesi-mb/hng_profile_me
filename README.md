🧠 Profile Endpoint API (Stage 0)

This is a simple RESTful API built with Django that returns profile information along with a random cat fact fetched from the Cat Facts API.

🚀 Features

/me endpoint that returns:

  . Your name, email, and backend stack

  . Current UTC timestamp (ISO 8601 format)

  . A random cat fact from an external API

Proper JSON response format with Content-Type: application/json

Handles errors gracefully (fallback response if Cat Facts API fails)

Ready for deployment on Heroku, PXXL, or similar platforms

📦 Tech Stack

Backend: Python (Django)

External API: Cat Facts API

Server: Gunicorn (for production)

Environment Variables: python-dotenv (optional)

Static File Handling: Whitenoise (optional)


Dependencies List 

Here are the dependencies used in this Task:

| Package           | Purpose                                          |
| ----------------- | ------------------------------------------------ |
| `Django`          | Web framework                                    |
| `requests`        | Fetches cat facts from external API              |
| `gunicorn`        | WSGI server for deployment                       |
| `python-dotenv`   | Loads environment variables                      |
| `whitenoise`      | Serves static files in production                |
| `dj-database-url` | Database configuration for deployment (optional) |


Installation Commands

1. Clone the Repository

git clone https://github.com/kwesi-mb/hng_profile_me.git

cd hng_profile_me

2. Create and Activate a Virtual Environment

Windows

python -m venv venv

venv\Scripts\activate

macOs/Linux

python3 -m venv venv

source venv/bin/activate

3. Install Dependencies

pip install -r requirements.txt

4. Run Migrations(if any)

python manage.py migrate

5. Start the Development Server

python manage.py runserver





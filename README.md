E-commerce Project
Overview
A simple e-commerce platform built with Django, HTML, CSS, JavaScript, and Bootstrap.

Features
User Registration and Authentication
Product Listing and Detailed Views
Shopping Cart Management
Admin Dashboard for Managing Products and Orders
Responsive Design
Technologies Used
Backend: Django
Frontend: HTML, CSS, JavaScript, Bootstrap
Database: SQLite (default)
Installation
1. Clone the Repository
bash
Copy code
git clone https://github.com/Bewajinis/PLP-Final-Project/new/main
cd ecommerce-django
2. Create a Virtual Environment
bash
Copy code
python3 -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
3. Install Dependencies
bash
Copy code
pip install -r requirements.txt
4. Apply Migrations
bash
Copy code
python manage.py migrate
5. Create a Superuser
bash
Copy code
python manage.py createsuperuser
6. Run the Development Server
bash
Copy code
python manage.py runserver
Access the site at http://127.0.0.1:8000.

License
This project is licensed under the MIT License.

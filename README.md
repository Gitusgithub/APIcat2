# E-Commerce Django Project

This project is a simple **E-Commerce application** built using the Django framework. It demonstrates how to define **one-to-many relationships** between models, manage database migrations, and set up a Django project for development and collaboration.

---

## **Features**

1. **Customer Model**
   - Stores customer details including:
     - `name`: Full name of the customer (string, up to 255 characters).
     - `email`: Unique email address (required, ensures no duplicates).

2. **Order Model**
   - Stores details of orders placed by customers:
     - `customer`: A foreign key linking the order to a specific customer.
     - `order_date`: The date and time when the order was placed (auto-filled).
     - `total_amount`: Total cost of the order, stored as a decimal value for accuracy.

3. **Data Relationships**
   - Each **Customer** can place multiple **Orders** (one-to-many relationship).
   - Orders are automatically deleted if the associated customer is removed (cascade behavior).

4. **Scalable Design**
   - The models are designed to be extended easily to include additional fields or features, such as customer addresses or order statuses.

---

## **Setup Instructions**

To get started with this project, follow the instructions below to set up the environment, run the project, and interact with the application.

### **Prerequisites**

- **Python 3.8+** (ensure you have the latest version of Python installed).
- **Django** (version 4.x or higher).

### **Installing Dependencies**

1. Clone the repository:
   ```bash
   git clone https://github.com/Gitusgithub/APIcat2
   cd e-commerce-django
Set up a virtual environment (recommended):



python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install the required dependencies:


pip install -r requirements.txt
Running the Project
Set up the database and migrations: Django uses migrations to set up your database schema. Run the following commands to create migrations for the models and apply them to your database:


python manage.py makemigrations
python manage.py migrate
Start the development server: To run the project locally, use the Django development server:


python manage.py runserver
This will start the server at http://127.0.0.1:8000/. You can visit this URL in your web browser to interact with the application.

Interacting with the Models
Admin Panel
To manage customers and orders through a graphical interface:

Create a superuser (admin account):


python manage.py createsuperuser
Login to the Admin Panel:

URL: http://127.0.0.1:8000/admin/
Use the superuser credentials to log in and manage the data (customers, orders).
Database
By default, Django uses an SQLite database. If you prefer to use a different database (e.g., PostgreSQL), you can configure the settings in settings.py.

Version Control
Initialize Git repository (if not done already):


git init
Commit changes:

Add changes to the staging area:

git add .
Commit the changes:

git commit -m "Initial commit for Django E-Commerce project"
Push to GitHub:

Create a new repository on GitHub and push your code:

git remote add origin https://github.com/Gitusgithub/APIcat2
git push -u origin master
Contributing
If you wish to contribute to this project, feel free to fork the repository, make changes, and submit a pull request. Ensure that any code added follows the existing style and is well-documented.
Eat Git And Fit - Web Application
===================
It's a web application that offers a collection of healthy recipes.
Inspired by model 80/20 which means healthy but no strict diet.
It's a place where you can find recipes according to meal type, occasion, region or ingredients.
For registered and logged-in users, there are additional features,
including the ability to add, save, and edit their own recipes.


Requirements
------------
* asgiref==3.6.0
* Django==4.2.1
* iniconfig==2.0.0
* packaging==23.1
* pluggy==1.0.0
* psycopg2-binary==2.9.6
* pytest==7.3.1
* sqlparse==0.4.4


How to Install and Run Eat_Git_And_Fit_80-20
--------------------------------------------
Prerequisites
Python 3.x should be installed on your system. PostgreSQL database should be installed and running.
Virtual environment (optional but recommended).
Installation
Clone the repository to your local machine (or download the .zip file and extract it):
```bash
git clone https://github.com/JankoLoL/Eat_Git_And_Fit_80-20.git
```
Navigate to the project directory:
```bash
cd Eat_Git_And_Fit_80-20
```
(Optional) Create and activate a virtual environment:
```bash
python -m venv venv
```
```bash
source venv/bin/activate    # On Windows: venv\Scripts\activate
```
Install the project dependencies using pip:
```bash
pip install -r requirements.txt
```

### Database Configuration

Create a PostgreSQL database for the project.
Update the database settings in the local_settings.py file located in the project's root directory.
Add your PostgreSQL database credentials and other configuration options.
Make sure not to include sensitive information like passwords in the repository.
Run Database Migrations. Apply database migrations to set up the necessary tables in the database:
```bash
python manage.py migrate
```
Run the Project. Start the development server:
```bash
python manage.py runserver
```
Open your web browser and go to http://localhost:8000 to access the Eat Git And Fit 80-20 application.

-------------------
Author: Adam Chrzanowski
Steps for running this project -
- make sure you have python installed on your system.
- create a virtual environment using "python -m venv virtual_environment_name".
- activate virtual environment using ".\virtual_environment_name\Scripts\activate".
- install all the required modules from requirements.txt using "pip install -r requirements.txt.
- change directory where the manage.py is, and migrate files
  - first run "python manage.py makemigrations".
  - then run "python manage.py migrate".
- finally run the server using "python manage.py runserver".


url for list reminders
methode get "http://127.0.0.1:8004/api/reminders/list/"

url for create reminder
methode post "http://127.0.0.1:8004/api/reminders/create/"

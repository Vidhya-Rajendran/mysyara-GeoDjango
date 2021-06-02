# Mysyara - Car Wash Order Creation Using GeoDjango
Create and manage car wash orders usage via simple app

## Scope
The application allows user to:
1. Create car washer profiles
2. Create car wash orders
3. List of car wash orders

## Tech Stack
1. Python
2. Django
3. GeoDjango
4. PostgreSQL

## Installation
1. Clone Repository
```
git clone https://github.com/Vidhya-Rajendran/mysyara-GeoDjango.git
```
2. To Create and activate virtual environment
```
virtualenv envname

source envname/bin/activate
```
3. Installing project requirements
```
pip install -r requirements.txt
```
4. To run the project
```
python manage.py runserver
```

## Project Description
### Create washer profile
Give the following details to **Create a washer profile**
```
Washer Name
Current Location
Is available
```
Washer profile will be create with washer name and washer location details. Is available field is readonly. By default is_available field is false. Once car wash order created by customer then is_available will be changed to True.

### Create car wash order
Give the following details to **Create a car wash order**
```
Customer Name
Customer Location
Car No
```
Customer requested for car wash order then car washer assigned based on nearest location of customer location. Once car wash order is created. Then the washer avalaiblity is changed to unavailable. 

### List of Car wash Orders
List of car wash orders displays corresponding customer and washer assigned.




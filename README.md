# Setup

## Requirements
* Python 3.7+

## Installation And Run
Copy .env.example into .env and fill up **SECRET_KEY**
```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py create_super_user # create super user with aktos/aktos
python manage.py generate_consumer_data # fill up consumer table from csv data
python manage.py runserver
```

# Implementation
1. **django-rest** library for REST API implementation
2. Strict **type definition** and **validation check** using **Serializer** and **typing** libraries
3. Filtering  
- Filtering based on these fields:  
**min_previous_jobs_count**, **max_previous_jobs_count**, **previous_jobs_count**, **status**  
http://localhost:8000/consumers/?previous_jobs_count=1  
http://localhost:8000/consumers/?min_previous_jobs_count=1  
http://localhost:8000/consumers/?status=1
- Multiple filtering conditions work at the same time with each other:  
http://localhost:8000/consumers/?previous_jobs_count=1&status=collected
4. Pagination
- Using **PageNumberPagination**  
https://www.django-rest-framework.org/api-guide/pagination/#pagenumberpagination
- Queries  
http://localhost:8000/consumers/?page=1  
http://localhost:8000/consumers/?page=1&page_size=50
5. Ordering
- Ordering based on these fields:  
**id**, **status**, **previous_jobs_count**, **street**, **amount_due**  
http://localhost:8000/consumers/?previous_jobs_count=1&status=collected&page_size=5&page=2&ordering=-amount_due


# Unit Testing
```bash
pytest
```

## Swagger API Docs
http://localhost:8000/docs/

## Heroku CLOUD URL
https://aktos.herokuapp.com/consumers/  
https://aktos.herokuapp.com/admin/  
https://aktos.herokuapp.com/docs/
# ✨ Lab 6 ✨
## __What did I leant so far__ ..
- Create a docker-compose file
- Manage the sessions within dockers
- API call with Django REST Framework
- Create a simple CRUD with API 

### Docker-compose File
I chose to use postgresql as the database. 
Then, I created docker-compose.yml file which it contains Django, PostgreSQL, and PGadmin as follows.

### REST API – Django REST framework
I used Django REST framework to create the API as follows.
 First, I created a folder as the API directory for this project.
 The files were consisted of ‘views.py’ where it brings all api data from the database to be displayed. ‘urls.py’ is a url pointed to this api. Lastly, ‘serializers.py’ contains CountSerializer class which it inherent functions from steriliser class. 
 
### API Call
I create a model within "api folder". use `@api_view` method from `rest_framework` to generate `[GET,POST,PUT,DELETE]`
Then, I used a simple Javascript to create a data using put method. Also, I created a Javascript to fetch new data from the database which renders all data from the postgreSQL as well. 
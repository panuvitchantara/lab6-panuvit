I chose to use postgresql as the database. 
Then, I created docker-compose.yml file which it contains Django, PostgreSQL, and PGadmin as follows.

I used Django REST framework to create the API as follows.
 First, I created a folder as the API directory for this project.
 The files were consisted of ‘views.py’ where it brings all api data from the database to be displayed. ‘urls.py’ is a url pointed to this api. Lastly, ‘serializers.py’ contains CountSerializer class which it inherent functions from steriliser class. 

I created a mock up data called ‘number_view’ and add some number, in this case ‘911’, to be numbers of view which it stored in the database.
The number was easily rendered with REST Framework and Serializer as follows.
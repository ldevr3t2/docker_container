# Music Suggestion API#

### To Run ###

* ./build.sh
* docker-compose up

### Included ###

* Main suggestion server container
* URLEncoder class in python-flask-server/swagger_server/url_encoder.py  
	URLEncoder helps to format strings in a very lenient way  
	ex. 'Pink Floyd' => 'pink+floyd'  
	even 'PiNk FlOyD' => 'pink+floyd'  
* Unittests for some classes (optional)
* Newman testing (optional)

### Usage ###

* GET to BASE_URL/artist_name
* ex. curl -X GET --header 'Accept: application/json' 'http://192.168.99.100:8081/v1/pink%20floyd'
* Feel free to copy json schemas and URLEncoder class for formatting

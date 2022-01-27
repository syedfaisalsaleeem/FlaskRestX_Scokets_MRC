# Flask Rest With Socket Application
This application serves the restful apis with sockets and role based authentication.
## Getting Started
To get started using this package follow the instructions below.

## Installation
 - git clone this repository
 - create a virtual environment
 - activate virtual environment
 - install requirement.txt using pip install -r requirements.txt
 - update the .env file
 - create a database in mysql and update that in .env file
 - then Go to “\venv\lib\site-packages\flask_script\__init__.py” and go to line number 15 and replace “from flask._compat import text_type” with “from flask_script._compat import text_type”.
  - python manage.py db init
  - python manage.py db migrate
  - python manage.py db upgrade
  - above commands will help us to setup and run the migrations
  - python main.py to start the server on local host

  ## APIS
  ### CREATE USER with validations
  - SEND POST REQUEST on this endpoint `http://localhost:5000/user` WITH JSON Payload
  `
  {
    "first_name":"faisal",
    "last_name":"saleem",
    "cnic":"1112233444551",
    "date_of_birth":"2001-11-11",
    "province":"Sindh"
}
`
- Get All the Users added with this endpoint with GET REQUEST `http://localhost:5000/user`

### CREATE A USER WITH ROLE
- SEND POST REQUEST on this endpoint `http://localhost:5000/user_roles/register` WITH JSON Payload
  `
{
    "email":"faisalsaleem@yahoo.com",
    "password":"demopassword",
    "roles": [{"name":"admin"}]
}
`
It will return the authorization bearer token
`{
    "status": true,
    "message": "User has been registered.",
    "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY0MzI4OTc3MywianRpIjoiMzhkYjM5NzAtN2ZiMS00OTMxLThlMjItYzc1ZTAxNmU4NTNmIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6MTQsIm5iZiI6MTY0MzI4OTc3MywiZXhwIjoxNjQzMjkwNjczfQ.9AJqKkWO96qn7fJ-zShfBI2xpcm-S_UKbro-UKCOWeI",
    "user": {
        "password": "demopassword",
        "roles": [
            {
                "name": "admin"
            }
        ],
        "email": "faisalsaleem@yahoo.com"
    }
}`

### check whether this user can access the url
 - Create a get request with authorization bearer token 
curl --location --request GET 'http://127.0.0.1:5000/test_roles/testadmin' \
--header 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY0MzI4NjI4MywianRpIjoiZjZmMmE2N2MtZWI3OC00Mzc3LThhZTAtODAxOGMxYTc3MTQ3IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6MTMsIm5iZiI6MTY0MzI4NjI4MywiZXhwIjoxNjQzMjg3MTgzfQ.8HE3Io1dEjM0m3mYiLKklayT1wwAu3t4kl1IAyK7q1U'

if the token is valid for the admin role request it will return successfull response

- Create a get request with authorization bearer token 
curl --location --request GET 'http://127.0.0.1:5000/test_roles/testemployees' \
--header 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY0MzI4NjI4MywianRpIjoiZjZmMmE2N2MtZWI3OC00Mzc3LThhZTAtODAxOGMxYTc3MTQ3IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6MTMsIm5iZiI6MTY0MzI4NjI4MywiZXhwIjoxNjQzMjg3MTgzfQ.8HE3Io1dEjM0m3mYiLKklayT1wwAu3t4kl1IAyK7q1U'

if the token is valid for the employees role request it will return successfull response

### Socket Connection
Use postman to test the socket connection
- http://localhost:5000 send a socket connection request
- `{"room":"1"}` send message to createrooms event to create room
-  `{"room":"1","username":"faisal"}` send message to join event to user join room which will be broadcasted
- `{"room":"1","username":"faisal"}` send message to leave event to leave room

### Google APIS
- update .env file to load api key
- use getaddress function to get the address from longitude and latitude
- getdistanceandtime function to get the distance and time from one position to second position

## Errors
if server is not starting go to this address to empty the port
for using only ip address at a time
https://stackoverflow.com/questions/12362542/python-server-only-one-usage-of-each-socket-address-is-normally-permitted
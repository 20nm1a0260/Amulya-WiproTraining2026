#! Question 1 – REST API Basics & Flask Server

#& Topics Covered:	API introduction, HTTP verbs, REST principles, Building a simple Flask web server	

'''
Create a simple RESTful API using Flask that manages a list of users.	
	
Requirements:	
	
1. Create a Flask application	
	
	
	
	
	
GET /users → Return all users	
	
GET /users/<id> → Return user details by ID	
	
POST /users → Create a new user	
	
3. Follow REST principles:	
	
	
	
Use proper HTTP status codes	
	
Return responses in JSON format	
	
4. Store data in an in-memory list or dictionary	

'''

from flask  import Flask,request,jsonify

app1=Flask(__name__)

users=[{"id":1,"name":"saiprakash"},
            {"id":2,"name":"reddy"}]

#GET METHOD

@app1.route("/",methods=["Get"])
def home():
    return "Welcome"

@app1.route("/users",methods=["Get"])
def get_users():
    return jsonify(users)

@app1.route("/users/<int:user_id>",methods=["Get"])
def get_user(user_id):
    
    for user in users:
        if user["id"]==user_id:
            return jsonify(user)
    
    return jsonify({"message":"User Not Found"}),404 


# POST METHOD 

@app1.route("/users/",methods=["POST"])
def add_user():
    data=request.json 
    newuser={
        "id":len(users)+1,
        "name":data.get("name")
    }
    users.append(newuser)
    return jsonify(newuser),201


if __name__=="__main__":
    app1.run(port=5000,debug=True)
    
    
#!Question 2 – Endpoint Testing Using Postman

#& Topics Covered:Create application endpoints, Test API using Postman

'''
Using the Flask API created in Question 1:

1. Test all endpoints using Postman

2. For each endpoint:



Set the correct HTTP method

Send request headers (Content-Type: application/json)

Pass request body for POST

3. Verify:



Correct status codes (200, 201, 404)

Correct JSON responses

4. Document your Postman tests with:



Screenshots (or steps)

Sample request and response payloads
'''
#Answer - refer pdf shared 
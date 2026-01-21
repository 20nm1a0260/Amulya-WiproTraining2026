
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


#PUT METHOD -- full update ,need to send whole data 

@app1.route("/users/<int:user_id>",methods=["PUT"])
def update_user(user_id):
    data=request.json
    for user in users:
        if user["id"]==user_id:
            user["name"]=data.get("name")
            return jsonify(user)
        
    return jsonify({"message":"user not found"}),404
        
        
#PATCH METHOD -- partial update, send only what you want to update


@app1.route("/users/<int:user_id>",methods=["PATCH"])

def update_user(user_id):
    pass 

if __name__=="__main__":
    app1.run(debug=True)
   

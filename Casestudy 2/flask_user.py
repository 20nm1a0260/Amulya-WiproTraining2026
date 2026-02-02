from flask import Flask,jsonify,request

app=Flask(__name__)

moviesdata= [ {
  "id": 101,
  "movie_name": "Interstellar",
  "language": "English",
  "duration": "2h 49m",
  "price": 250
}
]

#homepage

@app.route("/",methods=["GET"])
def home():
    return ''' <h1><center>Welcome to Online Movie Ticket Booking System</center></h1>
<h2>🍿 NOW SHOWING MOVIES</h2>

<h3>Hi Guys you can access these API Endpoints:</h3>

<ul>
    <li><b>GET</b> /api/movies  ---> To view all the running movies</li>
    <li><b>GET</b> /api/movies/&lt;id&gt;  ---> To know about one single show</li>
    <li><b>POST</b> /api/movies  ---> To add a new movie</li>
    <li><b>PUT</b> /api/movies/&lt;id&gt;  ---> To update movie details</li>
    <li><b>DELETE</b> /api/movies/&lt;id&gt;  ---> To delete a movie</li>
</ul>

<h2>🎟 BOOK TICKETS</h2>

<h3>To book tickets use the below endpoint:</h3>

<ul>
    <li><b>POST</b> /api/bookings  ---> To book movie tickets</li>
</ul>

<h4>⚠ Use Postman Application to test POST, PUT, DELETE & Booking APIs</h4>'''

#Retrieve all movies

@app.route("/api/movies/",methods=["GET"])
def retrieveallmovies():
    return jsonify(moviesdata),200


#Retrieve single movie details

@app.route("/api/movies/<int:movie_id>",methods=["GET"])
def getmoviebyid(movie_id):
    
    for movie in moviesdata:
        if movie["id"]==movie_id:
            return jsonify(movie)
    
    return jsonify({"message":"Movie Not Found"}),404

#POST METHOD

@app.route("/api/movies/",methods=["POST"])
def add_movie():
    data=request.json
    newmovie={
        "id":moviesdata[-1]["id"]+1,
        "movie_name":data.get("movie_name"),
        "language":data.get("language"),
        "duration":data.get("duration"),
        "price":data.get("price")
    }
    moviesdata.append(newmovie)
    return jsonify(newmovie),201

#PUT METHOD

@app.route("/api/movies/<int:movie_id>",methods=["PUT"])
def update_movie(movie_id):
    data=request.json
    for movie in moviesdata:
        if movie["id"]==movie_id:
            movie["movie_name"]=data.get("movie_name")
            movie["language"]=data.get("language")
            movie["duration"]=data.get("duration")
            movie["price"]=data.get("price")
            return jsonify(movie),200
    return jsonify({"message":"Movie Not Found"}),404


@app.route("/api/movies/<int:movie_id>",methods=["DELETE"])
def delete_movie(movie_id):
    for movie in moviesdata:
        if movie["id"]==movie_id:
            moviesdata.remove(movie)
            return jsonify({"message":"Movie Deleted Successfully"}),200
    return jsonify({"message":"Movie Not Found"}),404


#Tickets booking 

bookings=[]

@app.route("/api/bookings",methods=["POST"])
def book_ticket():
    data=request.json
    movie_id=data.get("movie_id")
    tickets=data.get("tickets")

    for movie in moviesdata:
        if movie["id"]==movie_id:
            booking={
                "movie_id":movie_id,
                "tickets":tickets
            }
            bookings.append(booking)
            return jsonify({"message":"Booking successfull",
                            "booking":booking}),201
    return jsonify({"message":"Movie Not found"}),404


if __name__=="__main__":
    app.run(debug=True)
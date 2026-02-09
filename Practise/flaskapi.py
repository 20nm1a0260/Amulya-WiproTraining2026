
from flask import Flask,jsonify,request

app=Flask(__name__)


moviesdata=[
    {
        "id":1,
        "movie_name":"Interstellar",
        "language":"English",
        "duration":"2h 49m",
        "price":323
    }
]
@app.route("/",methods=["GET"])
def homepage():
    return "hi welcome"

@app.route("/api/movies",methods=["GET"])
def getallmovies():
    return jsonify(moviesdata)

@app.route("/api/movies/<int:movie_id>",methods=["GET"])
def singlemovie(movie_id):
    for movie in moviesdata:
        if movie["id"]==movie_id:
            return jsonify(movie),200
    return jsonify({"message":"movie not found"}),404

@app.route("/api/movies",methods=["POST"])
def postmovies():
    data=request.json
    new_movie={
        "id":len(moviesdata)+1,
        "movie_name":data.get("movie_name"),
        "language":data.get("language"),
        "duration":data.get("duration"),
        "price":data.get("price")
    }
    moviesdata.append(new_movie)
    return jsonify(new_movie),201

@app.route("/api/movies/<int:movie_id>",methods=["PUT"])
def putmovie(movie_id):
    data=request.json 
    for movie in moviesdata:
        if movie["id"]==movie_id:
            movie["movie_name"]=data.get("movie_name")
            movie["language"]=data.get("language")
            movie["duration"]=data.get("duration")
            movie["price"]=data.get("price")
            return jsonify(movie)
    return jsonify({"message":"movie not found"}),404

@app.route("/api/movies/<int:movie_id>",methods=["DELETE"])
def deletemovie(movie_id):
    for movie in moviesdata:
        if movie["id"]==movie_id:
            moviesdata.remove(movie)
            return jsonify({"message":"movie deleted successfully"}),200
    return jsonify({"message":"movie not found"}),404

if __name__=="__main__":
    app.run(debug=True)

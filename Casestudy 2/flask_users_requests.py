
import requests

#getting all movies

getallmoviesurl="http://127.0.0.1:5000/api/movies"

response=requests.get(getallmoviesurl)

print(response.status_code)
print(response.json())


#getting single movie

getsinglemovieurl="http://127.0.0.1:5000/api/movies/102"

response=requests.get(getsinglemovieurl)

print(response.status_code)
print(response.json())

#post method to add movie

postmethodurl="http://127.0.0.1:5000/api/movies/"

body={
    "movie_name":"NUN",
    "language":"Spanish",
    "duration":"2h 5m",
    "price":300
}

response=requests.post(postmethodurl,json=body)

print(response.status_code)
print(response.json())

#put method to update the values

putmethodurl="http://127.0.0.1:5000/api/movies/102"

body={
    "movie_name":"Nun3 put method",
    "language":"English",
    "duration":"2h 45m",
    "price":342
}

response=requests.put(putmethodurl,json=body)

print(response.status_code)
print(response.json())

#Delete method to delete the movie

delelteurl="http://127.0.0.1:5000/api/movies/101"

response=requests.delete(delelteurl)

print(response.status_code)
print(response.json())

#post method for booking

bookingurl="http://127.0.0.1:5000/api/bookings"

body={
    "movie_id": 101,
    "tickets":5
}
response=requests.post(bookingurl,json=body)

print(response.status_code)

if response.headers.get("Content-Type") == "application/json":
    print(response.json())
else:
    print(response.text) 


import requests

getallurl="http://127.0.0.1:5000/api/movies"

response=requests.get(getallurl)
print(response.status_code)
print(response.json())

# getsingleurl="http://127.0.0.1:5000/api/movies/1"

# response=requests.get(getsingleurl)
# print(response.status_code)
# print(response.json())

# posturl="http://127.0.0.1:5000/api/movies"

# body={
#     "movie_name":"tenant",
#     "language":"Japanese",
#     "duration":"2h 2m",
#     "price":232
# }

# response=requests.post(posturl,json=body)
# print(response.status_code)
# print(response.json())

# puturl="http://127.0.0.1:5000/api/movies/2"

# body={
#     "movie_name":"Strangerthings",
#     "language":"English",
#     "duration":"2h 2m",
#     "price":232
# }

# response=requests.put(puturl,json=body)
# print(response.status_code)
# print(response.json())

# deleteurl="http://127.0.0.1:5000/api/movies/1"

# response=requests.delete(deleteurl)
# print(response.status_code)
# print(response.json())

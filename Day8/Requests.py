import requests

#! get url - list of all objects

# geturl1="https://api.restful-api.dev/objects"

# response=requests.get(geturl1)

# print(response.status_code)
# print(response.json())

#! get url - list of objects by id's

# geturl2="https://api.restful-api.dev/objects?id=3&id=5&id=10"

# response=requests.get(geturl2)

# print(response.status_code)
# print(response.json())

#! get url - single object 

# geturl3="https://api.restful-api.dev/objects/7"

# response=requests.get(geturl3)
# print(response.status_code)
# print(response.json())

#! post url 

# posturl="https://api.restful-api.dev/objects"

# body1={
#    "name": "Apple MacBook Pro 16",
#    "data": {
#       "year": 2019,
#       "price": 1849.99,
#       "CPU model": "Intel Core i9",
#       "Hard disk size": "1 TB"
#    }
# }

# response1=requests.post(posturl,json=body1)

# print(response1.status_code)
# print(response1.json())

#! put url - update object

# puturl="https://api.restful-api.dev/objects/ff8081819782e69e019be40466032e75"

# body={
#    "name": "Apple MacBook Pro 16",
#    "data": {
#       "year": 2019,
#       "price": 2049.99,
#       "CPU model": "Intel Core i9",
#       "Hard disk size": "1 TB",
#       "color": "silver"
#    }
# }

# response=requests.put(puturl,json=body)

# print(response.status_code)
# print(response.json())

#! patch - partially update object


# patchurl="https://api.restful-api.dev/objects/ff8081819782e69e019be40466032e75"

# body={
#    "name": "Apple MacBook Pro 16 (Updated Name)"
# }

# response=requests.patch(patchurl,json=body)

# print(response.status_code)
# print(response.json())

#! delete object 

# deleteurl="https://api.restful-api.dev/objects/ff8081819782e69e019be40d22702eb9"

# response=requests.delete(deleteurl)
# print(response.status_code)
# print(response.json())
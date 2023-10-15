phone = {
    "Adam Smith": "11-22-33",
    "Britney Spears": "44-55-66",
    "Bob Marley": "99-88-77"
}


for key in phone.keys():
    print(key)

for item in phone.items():
    print(item)


person = {
  "name": "John Doe",
  "age": 30,
  "city": "New York",
  "email": "johndoe@example.com",
  "parents": [
    {
      "name": "Sam Doe",
      "age": 60,
      "city": "New York",
      "email": "sam.doe@gmail.com",
    },
    {
      "name": "Barbara Doe",
      "age": 55,
      "city": "New York",
      "email": "basia.doe@gmail.com",
    }
  ]
}

for parent in person["parents"]:
    print(parent["name"], parent["age"])

print(person["dfghj"])
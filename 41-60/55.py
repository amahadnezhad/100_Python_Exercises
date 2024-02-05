"""
Exercise 55
Question: Please add a newemployee to the dictionary.


"""
d = {"employees":[{"firstName": "John", "lastName": "Doe"},
                {"firstName": "Anna", "lastName": "Smith"},
                {"firstName": "Peter", "lastName": "Jones"}],
"owners":[{"firstName": "Jack", "lastName": "Petter"},
          {"firstName": "Jessy", "lastName": "Petter"}]}
# Answer
d["employees"].append(dict(firstName = "Albert", lastName = "Bert"))
print(d)
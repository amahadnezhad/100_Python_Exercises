"""
Exercise 54
Question: Please update the dictionary by changing the last name of the second employee from
          Smith to Smooth or whatever takes your fancy.


"""
d = {"employees":[{"firstName": "John", "lastName": "Doe"},
                {"firstName": "Anna", "lastName": "Smith"},
                {"firstName": "Peter", "lastName": "Jones"}],
"owners":[{"firstName": "Jack", "lastName": "Petter"},
          {"firstName": "Jessy", "lastName": "Petter"}]}
# Answer
d['employees'][1]['lastName'] = "Smooth"
print(d)
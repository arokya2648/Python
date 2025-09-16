class india():
    def capital(slef):
        print('new Delhi is the capital of India')
    def language(self):
        print('Hindi is the most widely spoken language in India')
    def type(self):
        print('India is a developing country')
class usa():
    def capital(self):
        print("Washington DC is the capital of the USA")
    def language(self):
        print('english is the most widely spoken language in the USA')
    def type(self):
        print('USA is a developed country')
obj_ind=india()
obj_usa=usa()
for country in(obj_ind, obj_usa):
    country.capital()
    country.language()
    country.type()
# city= ['Jaipur','Kota','Mirzapur','UP','Assam','Gujarat']

# def length(city):
#     return len(city)


# sort=sorted(city,key=length)

# print("Sorted By Length=> ",sort)


city= ['Jaipur','Kota','Mirzapur','UP','Assam','Gujarat']


sort=sorted(city,key=lambda x: len(x))

print("Sorted Word By Length=> ",sort)

# The first ever program made by Shayan :)
print("Welcome to the Band Name Generator!\nI will help you with your band name")
city_name=input("What city you were born?:\n")
pet_name=input("What is your pet name?:\n")
band_name=city_name + " " + pet_name
length=str(len(band_name) - 1)
print("Your band name is: "+ band_name)
print("Your band name has "+length+" Characters")
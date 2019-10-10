my_name = 'Rishi Bhandari'
my_age = 27
my_height = "5'9''"
my_weight = 75
my_eyes = 'Brown'
my_hair = 'Black'

print("Let's talk about %s." % my_name)
print("He's %s tall." % my_height)
print("He's %d Kg heavy" % my_weight)
print("He's got %s eyes and %s hair." % (my_eyes, my_hair))
print("If I add %d and %d. I get %d" % (my_age, my_weight, my_age + my_weight))


# USING FORMAT() OPTION
print("Let's talk about {}".format(my_name))
print("He's {} tall".format(my_height))
print("He's {} KG heavy".format(my_weight))
print("He's got {} eyes and {} hair".format(my_eyes,my_hair))
print("If i add {} and {}. I get {}".format(my_age, my_weight, my_age + my_weight))


# USING F-String method

print(f'{my_age} + {my_weight} is equal to {my_age + my_weight}')
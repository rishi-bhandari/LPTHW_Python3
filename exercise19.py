def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print("You have {} cheese".format(cheese_count))
	print("You have {} boxes of crackers".format(boxes_of_crackers))
	print("Man thats enough for a party!")
	print("get a blanket.\n")

print("We can give the fucntion numbers directly.")
cheese_and_crackers(20,30)

print("We can just use the variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can even do math inside too:")
cheese_and_crackers(10+20, 5+6)

print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese+100, amount_of_crackers+1000)
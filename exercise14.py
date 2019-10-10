from sys import argv

script, user_name, education = argv
prompt = '..... '


print ("Hi {}, You're a {} graduate. I am the {} script".format(user_name, education, script))
print ("I would like to ask you a few questions")
print ("Do you like me {}?".format(user_name))
likes =  input(prompt)
print ("Where do you live {} ?".format(user_name))
live = input(prompt)

print ("What kind of computer do you have {} ?".format(user_name))
computer = input(prompt)

print ('''
Alright, so you said {} about liking me.
You're a {} graduate.
You live in {}. Not usre where it is.
And you have a {} computer. Nice.
'''.format(likes, education, live, computer))

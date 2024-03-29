from sys import argv

from os.path import exists

script, from_file, to_file = argv

print("Copying from {} to {}".format(from_file, to_file))

in_file = open(from_file)
in_data = in_file.read()

print("The input file is {} bytes long".format(len(in_data)))

print("Does the output file exists? {}".format(exists(to_file)))
print("Ready, hit the RETURN to continue, CTRL+C to abort.")
input()

out_file = open(to_file, 'w')
out_file.write(in_data)

print("Alright, done!!")

out_file.close()
in_file.close()
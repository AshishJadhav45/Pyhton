# Initialising string
ini_string = 'xbzefdgstb'

# initializing string
sstring = 'stb'

# printing initial string and substring
print ("initial_strings : ", ini_string, "\nsubstring : ", sstring)

# removing substring from end
# of string using replace Method
if ini_string.endswith(sstring):
	res = ini_string.replace(sstring, '')

# printing result
print ("resultant string", res)

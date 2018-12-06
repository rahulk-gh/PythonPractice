#rahul anagram
# lines read - 98218
#poultry outwits ants
#The MD5 hash of the secret phrase is "4624d200580677270a54ccff86b9610e"

gob = open('/home/rahulxlnx/Downloads/wordlist', 'r')
token = gob.readlines()
#woot = token[i]
print (token[1] + token[-1] )
gob.close()
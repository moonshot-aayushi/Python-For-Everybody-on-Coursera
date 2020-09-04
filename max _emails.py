name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
d = dict()
for line in handle:
    line.rstrip()
    words = line.split()
    #print(words)
    if line.startswith("From"): 
    	#for word in words:
        d[words[1]] = d.get(words[1], 0)+1
       
largest = None
email = None
for key in d:
    if largest is None : largest = d[key]
    if largest < d[key]:
        largest = d[key]
        email = key
print(email, largest)

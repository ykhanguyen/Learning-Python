print "family list"
family = ["dad", "mom", "sister"]
print family

print "birth list"
birth = []
birth.append("day")
birth.append("month")
birth.append("year")
print birth
print birth[2]
#print brith[3]

#slicing
for member in birth[1:2]:
    print member

print birth[1:3]

print type(birth)
print type(birth[0])
#<type 'list'>
#<type 'str'>


#short hand
print birth[0:]
print birth[:3]
print birth[:]

"""
Remember:
1. append
2. short hand
3. type()
4. slicing

"""

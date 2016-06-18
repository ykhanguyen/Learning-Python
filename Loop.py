print "try array:"
for number in [1,2,3,4]:
    print number

print "try range 2 elements:"
for number in range(1,5):
    print number

print "try short range 1 element"
for number in range(5):
    print number

print "try range 3 elements"
for number in range(1,5,2):
    print number

print "this is the while version -- choose a number different than 1"
a = int(raw_input())

while a == 1:
    print "you chose 1"
    a = int(raw_input())
print "you stop chosing 1"

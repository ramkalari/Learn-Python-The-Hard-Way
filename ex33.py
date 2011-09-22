i = 0
numbers = []

while i < 6:
    print "At the top i is %d" %i
    numbers.append(i)

    i = i + 1
    print "Numbers now:", numbers
    print "At the bottom i is %d" %i

print "The numbers: "

for num in numbers:
    print num


def my_range(limit, inc):
    i = 0;
    numbers = []

    while i < limit:
        numbers.append(i)
        i = i + inc
        
    for num in numbers:
        print num


my_range(6, 2)

def my_range_using_for(limit, inc):

    for i in range(0, limit, inc):
        print i

my_range_using_for(7, 2)

#   Reimplement the sum function that comes with python
#   That function takes a sequence of numbers and returns the
#   sum of those numbers.

def mysum(*args):
    total = 0
    for i in args:
        total += i
    return total

print(mysum(1,2,3))
print(mysum(1,2,3,4,5))
print(mysum(10,20,30,40,50,60,70,80,90,100))


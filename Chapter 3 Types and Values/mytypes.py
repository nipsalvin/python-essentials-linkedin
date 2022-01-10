a = 7
b = 7.1
c = "Alvin"
d = "nipsAlvin".capitalize()
"""
.capitalize - capitalizes first letter
.upper - makes it all upper case
.lower - makes it all lower case
"""
e= "seven {} {}".format(8, 9)
#place holders are filled with positional arguments 8 and 9 respectively
f = "seven {1} {0}".format(8, 9)
#positions are swapped since they are declared in the arguments
g = "seven {0:<9} {1:>9}".format(8, 9)
# :<9 and :>9 add 9 spaces to the left and right respectively
h = "seven {0:<09} {1:>09}".format(8, 123456789123456789)
#this adds 9 zeros to the spaces

print("a is {}".format(a))
#print(f"a is {a}")
print(type(a))

print("b is {}".format(b))
#print(f"b is {b})
print(type(b))

print("c is {}".format(c))
print(f"c is {c}")
print(f"c is {c} which is a", type(c))
print(f"This is {d}")
print (e)
print (f)
print (g)
print (h)
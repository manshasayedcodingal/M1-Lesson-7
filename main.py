#Identity operator

x = 5
if (type(x) is int):
    print("true")
else:
    print("false")

y = 5.0
if (type(y) is not float):
    print("true")
else:
    print("false")

a = 20
b = 20
if ( a is b ): 
	print("x & y  SAME identity")
     
b=30
if ( a is not b ):
	print("x & y have DIFFERENT identity")
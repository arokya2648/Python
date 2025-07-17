x=5
if(type(x)is int):
    print("true")
else:
    print("false")
y=5.0
if(type(y)is not float):
    print("true")
else:
    print("false")
z=20
w=20
if(z is w):
    print("z & w SAME identity")
w=30
if(w is not z):
    print("z & w have DIFFERENT identity")
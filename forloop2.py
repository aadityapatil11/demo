for i in range(5):
    print(end="*")

for i in range(5):
    if i==2:
        print(end="$")
    else:
        print(end="*")

for i in range(5):
    if i==0 or i==4:
        print(end="$")
    else:
        print(end="*")

for i in range(3):
    print(end="$*")

for i in range(1,6):
    print(i,end="")

for i in range(10,51,10):
    print(i,end="")

for i in range(2,11,2):
    print(i,end="")

for i in range(1,10,2):
    print(i,end="")

for i in range(1,7,2):
    print(i,end="*")

for i in range(1,6):
    if i==5:
        print(i,end="=")
    else:
        print(i,end="*")

for i in range(1,6):
    print(i,end="!+")

for i in range(1,6):
    if i==5:
        print(i,end="=")
    else:
        print(i,end="+")
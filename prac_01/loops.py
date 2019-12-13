for i in range(1, 21, 2):
    print(i, end=' ')
print()

for a in range(0, 11,):
    a = a * 10
    print(a, end=' ')
print()

for e in range(20, 0, -1):
    print(e, end=' ')
print()

row = int(input("enter number of the rows: "))
number = int(input("enter number of stars: "))
for o in range(1,row+1):
    print()
    for u in range(1, number+1):
        print ("*", end='')
print()

row = int(input("enter number of the rows: "))
for a in range(1,row+1):
    print()
    for b in range(1,a+1):
        print("*", end='')
print()

import random
number = 0
picks = int(input("How many picks? "))
for a in range(picks):
    quick_pick = []
    print()
    for e in range(6):
        number = random.randint(1, 45)
        while number in quick_pick:
            number = random.randint(1, 45)
        quick_pick.append(number)
    quick_pick.sort()
    print(quick_pick)
# print("{:2}".format(quick_pick), end=' ',)
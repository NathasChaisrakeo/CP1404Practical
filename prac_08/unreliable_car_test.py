from prac_08.unreliable_car import UnreliableCar


def main():

    good_car = UnreliableCar("Good Car", 100, 90)
    bad_car = UnreliableCar("Bad Car", 100, 10)

    for i in range(1, 30):
        print("Attempting to drive {}km: ".format(i))
        print("{:10} drove {:2}km".format(good_car.name, good_car.drive(i)))
        print("{:10} drove {:2}km".format(bad_car.name, bad_car.drive(i)))

    print(good_car)
    print(bad_car)

main()

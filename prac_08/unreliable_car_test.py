from prac_08.unreliable_car import UnreliableCar


def main():
    taxi = UnreliableCar("Prius 2", 100, 0)
    taxi.drive(40)
    print(taxi)


main()

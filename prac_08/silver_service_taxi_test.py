from prac_08.silver_service_taxi import SilverService


def main():
    taxi = SilverService("SilverServiceTaxi", 100)
    taxi.drive(18)
    print(taxi)
    print(taxi.get_fare())


main()

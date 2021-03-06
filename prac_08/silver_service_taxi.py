from prac_08.taxi import Taxi


class SilverService(Taxi):
    flagfall = 4.5

    def __int__(self, name, fuel, fanciness):
        super(SilverService).__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        return "{} plus flagfall of ${:2f}".format(super().__str__(), self.flagfall)

    def get_fare(self):
        return self.flagfall + super().get_fare()

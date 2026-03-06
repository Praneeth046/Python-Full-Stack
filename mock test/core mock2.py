
from datetime import datetime
class TimeTraveler:
    registry = []
    def __init__(self, codename, origin_year, destination_year):
        self.codename = codename
        self.origin_year = origin_year
        self.destination_year = destination_year
        TimeTraveler.registry.append(self)

    @classmethod
    def show_registry(cls):
        print("Total Travelers:", len(cls.registry))
        print(f"Codenames:")
        for traveler in cls.registry:
            print(traveler.codename)

    @staticmethod
    def year_status(year):
        current_year = datetime.now().year
        if year < current_year:
            return "Past"
        elif year == current_year:
            return "Present"
        else:
            return "Future"
t1 = TimeTraveler("praneeth", 2000, 2050)
t2 = TimeTraveler("varma", 2002, 2060)
t3 = TimeTraveler("gopi", 2003, 2070)
TimeTraveler.show_registry()
print()
print("1800:", TimeTraveler.year_status(1800))
print("2026:", TimeTraveler.year_status(2026))
print("2556:", TimeTraveler.year_status(2556))
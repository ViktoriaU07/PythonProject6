from datetime import datetime


class Date:
    def __init__(self, day: int, month: int, year: int):
        if not all(isinstance(x, int) for x in (day, month, year)):
            raise TypeError("day, month та year мають бути цілими числами")

        if year < 1:
            raise ValueError("Рік має бути додатним")

        if not (1 <= month <= 12):
            raise ValueError("Місяць має бути в діапазоні 1-12")

        if not (1 <= day <= self._days_in_month(month, year)):
            raise ValueError(f"День має бути в діапазоні 1-{self._days_in_month(month, year)}")

        self.__day = day
        self.__month = month
        self.__year = year

    def __str__(self):
        return f"{self.__day:02d}.{self.__month:02d}.{self.__year}"

    def __eq__(self, other):
        return (self.__day, self.__month, self.__year) == (other.__day, other.__month, other.__year)

    def __lt__(self, other):
        return self.to_ordinal() < other.to_ordinal()

    def __gt__(self, other):
        return self.to_ordinal() > other.to_ordinal()

    def is_leap_year(self):
        year = self.__year
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    def days_in_month(self):

        return self._days_in_month(self.__month, self.__year)

    def to_ordinal(self):
        return (datetime(self.__year, self.__month, self.__day) - datetime(1, 1, 1)).days

    @staticmethod
    def _days_in_month(month, year):
        if month == 2:
            return 29 if (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)) else 28
        if month in [4, 6, 9, 11]:
            return 30
        return 31


if __name__ == "__main__":
    try:
        date1 = Date(29, 2, 2024)
        date2 = Date(1, 1, 2025)
        print("Дата 1:", date1)
        print("Дата 2:", date2)
        print("Дата 1 > Дата 2:", date1 > date2)
        print("Дата 1 == Дата 2:", date1 == date2)
        print("Дата 1 - кількість днів у місяці:", date1.days_in_month())
        print("Дата 1 високосний рік?:", date1.is_leap_year())
        print("Дата 1 ordinal:", date1.to_ordinal())

        bad_date = Date(31, 2, 2023)
    except (ValueError, TypeError) as e:
        print("Помилка при створенні дати:", e)
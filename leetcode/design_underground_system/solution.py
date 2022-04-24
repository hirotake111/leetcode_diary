from typing import Dict, Tuple
from unittest import TestCase, main


class CheckInRecord:
    start_station_name: str
    start_time: int

    def __init__(self, stationName: str, time: int) -> None:
        self.start_station_name = stationName
        self.start_time = time


class TotalRecord:
    _amount: int
    _count: int

    def __init__(self, time: int) -> None:
        self._amount = time
        self._count = 1

    def add(self, time: int):
        self._amount += time
        self._count += 1

    def get_average(self) -> float:
        return self._amount / self._count


class UndergroundSystem:
    _checkin_db: Dict[int, Tuple[str, int]]
    _record_db: Dict[Tuple[str, str], Tuple[int, int]]

    def __init__(self):
        self._checkin_db = {}
        self._record_db = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self._checkin_db[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        checkin_record = self._checkin_db.pop(id)
        total_record = self._record_db.get((checkin_record[0], stationName))
        if total_record is None:
            # create a new record
            self._record_db[(checkin_record[0], stationName)] = (
                t - checkin_record[1],
                1,
            )
        else:
            # update an existing one
            self._record_db[(checkin_record[0], stationName)] = (
                total_record[0] + t - checkin_record[1],
                total_record[1] + 1,
            )

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        amount, count = self._record_db[(startStation, endStation)]
        return amount / count


class TestSolution(TestCase):
    def test_solution(self):
        s = UndergroundSystem()
        s.checkIn(45, "Leyton", 3)
        s.checkIn(32, "Paradise", 8)
        s.checkIn(27, "Leyton", 10)
        s.checkOut(
            45, "Waterloo", 15
        )  # Customer 45 "Leyton" -> "Waterloo" in 15-3 = 12
        s.checkOut(
            27, "Waterloo", 20
        )  # Customer 27 "Leyton" -> "Waterloo" in 20-10 = 10
        s.checkOut(
            32, "Cambridge", 22
        )  # Customer 32 "Paradise" -> "Cambridge" in 22-8 = 14
        self.assertEqual(
            s.getAverageTime("Paradise", "Cambridge"), 14
        )  # return 14.00000. One trip "Paradise" -> "Cambridge", (14) / 1 = 14
        self.assertEqual(
            s.getAverageTime("Leyton", "Waterloo"), 11
        )  # return 11.00000. Two trips "Leyton" -> "Waterloo", (10 + 12) / 2 = 11
        s.checkIn(10, "Leyton", 24)
        self.assertEqual(s.getAverageTime("Leyton", "Waterloo"), 11)  # return 11.00000
        s.checkOut(
            10, "Waterloo", 38
        )  # Customer 10 "Leyton" -> "Waterloo" in 38-24 = 14
        self.assertEqual(
            s.getAverageTime("Leyton", "Waterloo"), 12
        )  # return 12.00000. Three trips "Leyton" -> "Waterloo", (10 + 12 + 14) / 3 = 12

        s = UndergroundSystem()
        s.checkIn(10, "Leyton", 3)
        s.checkOut(10, "Paradise", 8)  # Customer 10 "Leyton" -> "Paradise" in 8-3 = 5
        s.getAverageTime("Leyton", "Paradise")  # return 5.00000, (5) / 1 = 5
        s.checkIn(5, "Leyton", 10)
        s.checkOut(5, "Paradise", 16)  # Customer 5 "Leyton" -> "Paradise" in 16-10 = 6
        s.getAverageTime("Leyton", "Paradise")  # return 5.50000, (5 + 6) / 2 = 5.5
        s.checkIn(2, "Leyton", 21)
        s.checkOut(2, "Paradise", 30)  # Customer 2 "Leyton" -> "Paradise" in 30-21 = 9
        s.getAverageTime(
            "Leyton", "Paradise"
        )  # return 6.66667, (5 + 6 + 9) / 3 = 6.66667


# Your s object will be instantiated and called as such:
# obj = s()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)

if __name__ == "__main__":
    main()

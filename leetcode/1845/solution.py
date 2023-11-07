"""
https://leetcode.com/problems/seat-reservation-manager/
1845. Seat Reservation Manager
"""

class SeatManager:

    def __init__(self, n: int):
        self.queue = list(i for i in range(1, n + 1)) 

    def reserve(self) -> int:
        return heappop(self.queue)

    def unreserve(self, seatNumber: int) -> None:
        heappush(self.queue, seatNumber) 

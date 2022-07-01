from typing import List, Tuple
from unittest import TestCase, main


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        # bucket sort approach
        bucket = [0] * 1001
        total_units = 0

        for boxes, units in boxTypes:
            bucket[units] += boxes

        for units in range(1000, -1, -1):
            boxes = bucket[units]
            if boxes == 0:
                continue
            if truckSize >= boxes:
                truckSize -= boxes
                total_units += boxes * units
                continue
            total_units += truckSize * units
            break

        return total_units
        # # intuitive approach
        # units = 0
        # sorted_box_types = sorted(boxTypes, key=lambda x: x[1], reverse=True)
        # for num_of_boxes, num_of_units in sorted_box_types:
        # if truckSize >= num_of_boxes:
        # truckSize -= num_of_boxes
        # units += num_of_boxes * num_of_units
        # continue
        # units += truckSize * num_of_units
        # break

        # return units


class Test(TestCase):
    s = Solution()
    data: List[Tuple[List[List[int]], int, int]] = [
        ([[1, 3], [2, 2], [3, 1]], 4, 8),
        ([[5, 10], [2, 5], [4, 7], [3, 9]], 10, 91),
    ]

    def test_solution(self):
        for box_types, truck_size, expected in self.data:
            self.assertEqual(self.s.maximumUnits(box_types, truck_size), expected)


if __name__ == "__main__":
    main()

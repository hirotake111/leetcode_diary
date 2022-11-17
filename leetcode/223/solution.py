class Solution:
    def calculateRectangle(self, x1: int, y1: int, x2: int, y2: int) -> int:
        x_axis = x2 - x1
        y_axis = y2 - y1
        return x_axis * y_axis

    def computeArea(
        self,
        ax1: int,
        ay1: int,
        ax2: int,
        ay2: int,
        bx1: int,
        by1: int,
        bx2: int,
        by2: int,
    ) -> int:
        area_a = self.calculateRectangle(ax1, ay1, ax2, ay2)
        area_b = self.calculateRectangle(bx1, by1, bx2, by2)

        # find the overlaps
        right = min(ax2, bx2)
        left = max(ax1, bx1)
        x_overlap = right - left
        top = min(ay2, by2)
        bottom = max(ay1, by1)
        y_overlap = top - bottom

        # if either of x and y is negative, the two rectangle does not overlap each other
        if min(x_overlap, y_overlap) <= 0:
            return area_a + area_b

        # now we can say those rectables are overlapped.
        return area_a + area_b - (x_overlap * y_overlap)

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        n = len(heights)

        stack = []

        max_area = 0

        for i in range(n) :

            while stack and heights[stack[-1]] > heights[i]:

                nse = i

                height = heights[stack.pop()]

                if stack:

                    pse = stack[-1]

                else:
                    pse = -1

                max_area = max(max_area , (nse - pse - 1)*height)

            stack.append(i)

        while stack :

            nse = n

            height = heights[stack.pop()]

            if stack:

                pse = stack[-1]
            else:
                pse = -1

            max_area = max(max_area , (nse-pse-1)*height)


        return max_area

        
def maxHistogramArea(heights):
    stack = []
    max_area = 0

    for i, h in enumerate(heights):

        # Pop smaller heights from stack
        while stack and heights[stack[-1]] >= h:
            height = heights[stack.pop()]

            if not stack:
                width = i
            else:
                width = i - stack[-1] - 1

            area = height * width
            max_area = max(max_area, area)

        stack.append(i)

    # Pop remaining heights
    while stack:
        height = heights[stack.pop()]

        if not stack:
            width = len(heights)
        else:
            width = len(heights) - stack[-1] - 1

        area = height * width
        max_area = max(max_area, area)

    return max_area


heights = [2, 1, 5, 6, 2, 3]
print(maxHistogramArea(heights))

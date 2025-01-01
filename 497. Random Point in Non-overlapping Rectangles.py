class Solution:
    def __init__(self, rects: list[list[int]]):
        self.rects = rects
        self.weights = []
        self.total_points = 0
        
        for rect in rects:
            a, b, x, y = rect
            area = (x - a + 1) * (y - b + 1)
            self.total_points += area
            self.weights.append(self.total_points)
    
    def pick(self) -> list[int]:
        rand_weight = random.randint(1, self.total_points)
        rect_index = next(i for i, w in enumerate(self.weights) if rand_weight <= w)
        
        a, b, x, y = self.rects[rect_index]
        rand_x = random.randint(a, x)
        rand_y = random.randint(b, y)
        
        return [rand_x, rand_y]
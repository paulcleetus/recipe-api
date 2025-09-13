import math

class Point:
    def __init__(self, x: float, y: float ):
        self.move(x, y)

    def move(self, x: float, y: float ) -> None:
        self.x = x
        self.y = y

    def reset(self) -> None:
        self.move(0,0)

    def calculate_distance(self, other: "Point") -> float:
        '''
        calculate Euclidean distance (Hypotenuse of right angle triangle)
        sqrt( sqr(x1 - x2) + sqr(y1 - y2) )
        '''
        return math.hypot(self.x - other.x, self.y - other.y)
    
p1 = Point(5,4)
p2 = Point(3,6)

p = Point(2,2)
p.reset()

print(p1.x, p1.y)
print(p2.x, p2.y)

print(p.x, p.y)

print(p.calculate_distance(p) )
print(p.calculate_distance(p1) )
print(p.calculate_distance(p2) )
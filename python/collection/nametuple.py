from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(11, y=22)
print(f'p[0]+p[1] = {p[0] + p[1]}')
print(f'p.x+p.y = {p.x + p.y}')


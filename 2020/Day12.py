dirs = ['N', 'E', 'S', 'W']

class Ferry:
  def __init__(self, east, north, dir):
    self.east = east
    self.north = north
    self.dir = dir

  def move(self, action, value):
    if action == 'N':
        self.north += value
    elif action == 'S':
        self.north -= value
    elif action == 'E':
        self.east += value
    elif action == 'W':
        self.east -= value
    elif action == 'L':
        idx = (dirs.index(self.dir) - value // 90) % 4
        self.dir = dirs[idx]
    elif action == 'R':
        idx = (dirs.index(self.dir) + value // 90) % 4
        self.dir = dirs[idx]
    elif action == 'F':
        self.move(self.dir, value)

class Waypoint:
    def __init__(self, east, north):
        self.east = east
        self.north = north

    def move(self, action, value):
        if action == 'N':
            self.north += value
        elif action == 'S':
            self.north -= value
        elif action == 'E':
            self.east += value
        elif action == 'W':
            self.east -= value
        elif action == 'L':
            turns = value // 90
            for _ in range(turns):
                tmp = self.east
                self.east = -self.north
                self.north = tmp
        elif action == 'R':
            turns = value // 90
            for _ in range(turns):
                tmp = self.north
                self.north = -self.east
                self.east = tmp

class Pair:
    def __init__(self):
        self.ferry = Ferry(0, 0, 'E')
        self.waypoint = Waypoint(10, 1)

    def move(self, action, value):
        if action in dirs + ['L', 'R']:
            self.waypoint.move(action, value)
        elif action == 'F':
            for _ in range(value):
                self.ferry.move('E', self.waypoint.east)
                self.ferry.move('N', self.waypoint.north)

ferry = Ferry(0, 0, 'E')
pair = Pair()

with open('Day12.txt') as file:
    instructions = file.read().splitlines() 

for i in instructions:
    action = i[0]
    value = int(i[1:])
    ferry.move(action, value)
    pair.move(action, value)

print(abs(ferry.east) + abs(ferry.north)) #p1
print(abs(pair.ferry.east) + abs(pair.ferry.north)) #p2


import sys

class Elevator:
    def __init__(self, start_floor):
        self.current_floor = start_floor
        self.destination_floors = []
        self.time = 0
        self.floors_visited = []
    
    def add_destination_floor(self, floor):
        if floor not in self.destination_floors:
            self.destination_floors.append(floor)
    
    def go_to_next_floor(self):
        next_floor = self.destination_floors[0]
        while next_floor != self.current_floor:
            if next_floor > self.current_floor:
                self.current_floor += 1
                self.time += 10
            elif next_floor < self.current_floor:
                self.current_floor -= 1
                self.time += 10
        self.destination_floors.pop(0)
        self.floors_visited.append(next_floor)
        return self

def simulate_elevator(start_floor, destination_floors):
    elevator = Elevator(start_floor)
    elevator.floors_visited.append(start_floor)
    for floor in destination_floors:
        elevator.add_destination_floor(floor)
    while len(elevator.destination_floors) > 0:
        result = elevator.go_to_next_floor()
    return result

start_floor = int(input('Starting floor: '))
destination_floors_input = input('Destination floors: ')
destination_floors = [int(s) for s in destination_floors_input.split(',')]
result = simulate_elevator(start_floor, destination_floors)
print(f"Floors Visited: {result.floors_visited}")
print(f"Time: {result.time}")


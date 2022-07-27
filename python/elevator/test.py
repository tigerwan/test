class Elevator:
    def __init__(self, id, busy=False, current_floor=1, destination_floor=None):
        self.id = id
        self.busy = busy
        self.current_floor = current_floor
        self.destination_floor = destination_floor

    def go(self, destination_floor):
        self.destination_floor = destination_floor
        self.busy = True


class Controller:
    def __init__(self):
        self.elevators = {}

    def add_elvevator(self, id, busy, current_floor, destination_floor=None):
        self.elevators[id] = Elevator(id, busy, current_floor, destination_floor)

    def choose_elevator(self, destination_floor):

        distances = [
            {
                "elevator": elevator,
                "distance": abs(destination_floor - elevator.current_floor),
            }
            for id, elevator in self.elevators.items()
            if elevator.busy is False
        ]
        sorted_distances = sorted(distances, key=lambda dist: dist["distance"])
        shortest_distance = sorted_distances[0] if len(sorted_distances) > 0 else []

        if shortest_distance:
            print(
                f"closest evevator from floor {destination_floor} is evelvator {shortest_distance['elevator'].id} which is {shortest_distance['distance']} awway"
            )
            return shortest_distance["elevator"]
        else:
            print(f"no free elevator is available to go to {destination_floor}")
            return None


    def allocate_elevators(self, destinations):
        for destination in destinations:
            elevator = self.choose_elevator(destination)
            if elevator is not None:
                elevator.go(destination)


if __name__ == "__main__":
    controller = Controller()
    controller.add_elvevator("l1", False, 0)
    controller.add_elvevator("l2", True, 10)
    controller.allocate_elevators([1, 5])

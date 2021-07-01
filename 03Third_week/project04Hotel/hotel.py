class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room):
        if room not in self.rooms:
            self.rooms.append(room)

    def take_room(self, room_number, people):
        filtered_rooms = [x for x in self.rooms if x.number == room_number]
        if filtered_rooms:
            room_to_take = filtered_rooms[0]
            if not room_to_take.is_taken and room_to_take.capacity >= people:
                self.guests += people
                room_to_take.is_taken = True
                return room_to_take.take_room(people)

    def free_room(self, room_number):
        filtered_rooms = [x for x in self.rooms if x.number == room_number]
        if filtered_rooms:
            room_to_free = filtered_rooms[0]
            room_to_free.is_taken = False
            self.guests = 0
            return room_to_free.free_room()

    def print_status(self):
        free_rooms = [str(room) for room in self.rooms if not room.is_taken]
        taken_rooms = [str(room) for room in self.rooms if room.is_taken]
        print(f'Hotel {self.name} has {self.guests} total guests')
        print(f'Free rooms: {", ".join(free_rooms)}')
        print(f'Taken rooms: {", ".join(taken_rooms)}')

from typing import List, Dict

from .parking_strategy import ParkingStrategy1, ParkingStrategy2


class ParkManager:
    def __init__(self, parking: List[List[List[int]]]) -> None:
        self.parking = parking
        self.current_parking_status = [
            [[0 for column in row] for row in floor] for floor in parking
        ]
        self.free_parking_spots: List[Dict] = self.calculate_initial_free_spaces()
        self.parking_mapping = {}
        self.search_parking_space = {}

    def print_parking(self):
        print("parking", self.parking)
        print("current_parking_status", self.current_parking_status)
        print("free_parking_Spots", self.free_parking_spots)

    def calculate_initial_free_spaces(self):
        free_spaces = []
        for floor in self.parking:
            two_wheeler_count = 0
            four_wheeler_count = 0
            for row in floor:
                for spot in row:
                    if spot == 4:
                        four_wheeler_count += 1
                    elif spot == 2:
                        two_wheeler_count += 1
            free_spaces.append({2: two_wheeler_count, 4: four_wheeler_count})
        return free_spaces

    def save_parking_details(self, spot_id, vehicle_number, ticket_id, vehicle_type):
        self.parking_mapping[spot_id] = {
            "vehicle_number": vehicle_number,
            "ticked_id": ticket_id,
            "vehicle_type": vehicle_type,
        }
        self.search_parking_space[vehicle_number] = spot_id
        self.search_parking_space[ticket_id] = spot_id 

    def search_vehicle(self, search_query: str):
        if search_query.lower() in self.search_parking_space:
            return self.search_parking_space[search_query.lower()]

    def delete_parking_details(self, spot_id):
        result = self.parking_mapping[spot_id]
        del self.parking_mapping[spot_id]
        del self.search_parking_space[result["ticket_id"]]
        del self.search_parking_space[result["vehicle_type"]]

    def update_free_space_counter(self, spot_id, vehicle_type=None, type="park"):
        floor, row, column = self.spot_id_decoder(spot_id)
        if type == "park":
            self.current_parking_status[floor][row][column] = 1
            self.free_parking_spots[floor][vehicle_type] -= 1
        else:
            vehicle_type = self.parking[floor][row][column]
            self.current_parking_status[floor][row][column] = 0
            self.free_parking_spots[floor][vehicle_type] += 1

    def park(
        self,
        vehicle_type: int,
        vehicle_number: str,
        ticket_id: str,
        parking_strategy: int,
    ) -> str:
        if parking_strategy == 1:
            parking_strategy_class = ParkingStrategy1()
        elif parking_strategy == 2:
            parking_strategy_class = ParkingStrategy2()
        else:
            raise ValueError("parking strategy not defined")
        
        vehicle_number = vehicle_number.lower()
        ticket_id = ticket_id.lower()

        result = parking_strategy_class.find_parking_spot(
            self.parking,
            self.current_parking_status,
            vehicle_type,
            self.free_parking_spots
        )
        spot_id = self.spot_id_generator(result[0], result[1], result[2])
        self.save_parking_details(spot_id, vehicle_number, ticket_id, vehicle_type)
        self.update_free_space_counter(spot_id, vehicle_type, "park")
        return spot_id

    def remove_vehicle(self, spot_id: str):
        self.delete_parking_details(spot_id)
        self.update_free_space_counter(spot_id, type="remove")

    def spot_id_generator(self, floor: int, row: int, column: int):
        return f"{floor}-{row}-{column}"

    def spot_id_decoder(self, spot_id: str):
        result = spot_id.split("-")
        return [int(x) for x in result]

    def get_free_spots_count(self, floor: int, vehicle_type: int):
        return self.free_parking_spots[floor][vehicle_type]

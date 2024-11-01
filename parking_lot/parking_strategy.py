from abc import ABC, abstractmethod
from typing import Union, List


class ParkingStrategy(ABC):
    @abstractmethod
    def find_parking_spot(
        self,
        parking_structure: List[List[List[int]]],
        current_status: List[List[List[int]]],
        vehicle_type: int,
        free_parking_spots: List
    ) -> Union[int, int, int]:
        pass


class ParkingStrategy1(ParkingStrategy):
    """
    Get the parking spot at lowest index i.e.
    lowest floor, row and column e.g. park()
    is called with vehicleType 4 and we have
    free 4-wheeler spots at parking[0][0][0],
    parking[0][0][1] and parking[1][0][2] here
    we will return parking[0][0][0] because its
    index (floor, row, column) comes before the other two.
    """

    def find_parking_spot(
        self,
        parking_structure: List[List[List[int]]],
        current_status: List[List[List[int]]],
        vehicle_type: int,
        free_parking_spots: List
    ) -> Union[int, int, int]:
        """
        This function takes in the parking structure, the current status of the parking, vehicle type.
        It returns the floor, row and column index of the parking spot.
        """
        for floor_index, floor in enumerate(parking_structure):
            for row_index, row in enumerate(floor):
                for column_index, spot in enumerate(row):
                    if (
                        spot == vehicle_type
                        and current_status[floor_index][row_index][column_index] == 0
                    ):
                        return floor_index, row_index, column_index


class ParkingStrategy2(ParkingStrategy):
    """
    Get the floor with maximum number of free spots for the given vehicle type.
    for tie breaker choose the lowest floor
    and first free parking spot for that floor
    """

    def find_parking_spot(
        self,
        parking_structure: List[List[List[int]]],
        current_status: List[List[List[int]]],
        vehicle_type: int,
        free_parking_spots,
    ) -> Union[int, int, int]:
        """
        This function takes in the parking structure, the current status of the parking, vehicle type and the free parking spots.
        It returns the floor, row and column index of the parking spot based on the following strategy:
        1. Get the floor with maximum number of free spots for the given vehicle type.
        2. for tie breaker choose the lowest floor and first free parking spot for that floor.
        """
        selected_floor = -1
        maximum_free_spaces_count = float("-inf")
        for floor in range(len(free_parking_spots)):
            if free_parking_spots[floor][vehicle_type] > maximum_free_spaces_count:
                maximum_free_spaces_count = free_parking_spots[floor][vehicle_type]
                selected_floor = floor
        for row_index, row in enumerate(parking_structure[selected_floor]):
            for column_index, spot in enumerate(row):
                if (
                    spot == vehicle_type
                    and current_status[selected_floor][row_index][column_index] == 0
                ):
                    return selected_floor, row_index, column_index

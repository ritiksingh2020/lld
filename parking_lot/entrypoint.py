
import pytest
from parking_lot import ParkManager



parking = ParkManager(
    [
        [[4, 4, 2, 2], [2, 4, 2, 0], [0, 2, 2, 2], [4, 4, 4, 0]],
        [[4, 4, 2, 2], [2, 4, 2, 0], [0, 2, 2, 2], [4, 4, 4, 2]],
    ]
)
# spot_id = parking.park(2, "Wb74am2445", "random101", 1)
# print(spot_id)
# spot_id = parking.park(2,"wb74sbds","sjdbcks",1)
# print(spot_id)

# parking.print_blueprint()
def test_free_spots():
    assert parking.get_free_spots_count(0,4) == 6
    assert parking.get_free_spots_count(0, 2) == 7
    assert parking.get_free_spots_count(1,2) == 8
    assert parking.get_free_spots_count(1,4) == 6


def test_park_two_wheeler_with_undefined_strategy():
    with pytest.raises(ValueError):
        parking.park(2, "GJ12MK1234", "123", 0)

def test_park_two_wheeler_with_strategy_one():
    spot_id = parking.park(2, "GJ12MK1234", "123", 1)

    assert spot_id, "❗️ Did not find parking"
    assert type(spot_id) is str, "❗️ Response is not of type string"
    assert spot_id == "0-0-2", "❗️ Vehicle parked at incorrect spot"

    # Search for the parked vehicle
    assert (
        parking.search_vehicle("GJ12MK1234") == "0-0-2"
    ), "❗️ Couldn't find vehicle from vehicle_number"
    assert (
        parking.search_vehicle("123") == "0-0-2"
    ), "❗️ Couldn't find vehicle from ticket_number"

    assert (
        parking.get_free_spots_count(0, 2) == 6
    ), "❗️ Number of spots not reduced for that vehicle type"

    

def test_park_two_wheeler_with_strategy_two():
    spot_id = parking.park(2, "GJ12MK1235", "124", 2)

    assert spot_id, "❗️ Did not find parking"
    assert type(spot_id) is str, "❗️ Response is not of type string"
    assert spot_id == "1-0-2", "❗️ Vehicle parked at incorrect spot"

    # Search for the parked vehicle
    assert (
        parking.search_vehicle("GJ12MK1235") == "1-0-2"
    ), "❗️ Couldn't find vehicle from vehicle_number"
    assert (
        parking.search_vehicle("124") == "1-0-2"
    ), "❗️ Couldn't find vehicle from ticket_number"
 
    assert (
        parking.get_free_spots_count(1, 2) == 7
    ), "❗️ Number of spots not reduced for that vehicle type"


# test_free_spots()
# test_park_two_wheeler_with_strategy_one()
# test_park_two_wheeler_with_undefined_strategy()
# test_park_two_wheeler_with_strategy_two()

print("All testcases passed")
"""
TESTING FOR MAIN
"""

from main import main_results


def test_func():
    """Test function for main"""
    test_dict = main_results()
    assert test_dict["extract"] == "covid-geography/mmsa-icu-beds.csv"
    assert test_dict["transform"] == "Upload Complete"
    assert test_dict["complex_query"] == "Join Successful"

    # # Extract the actual list of messages from the returned dictionary
    # actual_list = result["full_crudquery"]

    # # Assert that the actual list matches the expected list
    # assert actual_list == expected, f"Assertion failed: {actual_list} != {expected}"


if __name__ == "__main__":
    test_func()

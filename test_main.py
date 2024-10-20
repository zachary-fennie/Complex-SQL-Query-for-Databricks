"""
TESTING FOR MAIN
"""

from main import main_results


def test_func():
    """Test function for main"""
    test_dict = main_results()
    assert test_dict["extract"] is not None
    assert test_dict["transform"] is not None
    assert test_dict["complex_query"] is not None


if __name__ == "__main__":
    test_func()

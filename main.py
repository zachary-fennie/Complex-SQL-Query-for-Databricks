"""
MAIN
"""

from library.extract import extract
from library.transform_load import load
from library.query_join import complex_query


def main_results():
    """Results function for testing main"""
    results = {
        "extract": extract(),
        "transform": load(),
        "full_crudquery": complex_query(),
    }
    return results


def main():
    """Main function for the Complex SQL operations"""
    # extract
    extract()

    # transform and load
    load()

    # query
    complex_query()

    # call results function for testing
    main_results()


if __name__ == "__main__":
    main()

import json
import os
from dotenv import load_dotenv
from googleapiclient.discovery import build
from excel import excel_helper


def custom_search(search):
    """Creates a custom google search engine"""

    load_dotenv()
    service = build(
        "customsearch", "v1", developerKey=os.getenv("API_KEY")
    )

    # returns the result
    result = (
        service.cse()
        .list(
            q=search,
            cx=os.getenv("CX"),
        )
        .execute()
    )

    return result


def main():
    """main function"""
    search = input(str("What would you like to search today?: "))
    results = custom_search(search)

    with open("../data/results.json", 'w') as wf:
        json.dump(results, wf, indent=4)

    excel_helper(search)


if __name__ == "__main__":
    main()

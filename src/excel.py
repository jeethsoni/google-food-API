"""
funtion that parses the json dictionary
"""

import json
import re
import xlsxwriter


def excel_helper(search):
    """
    Parses 
    """

    # opens json file and loads json in data variable
    f = open("../data/results.json")
    data = json.load(f)

    # final list requirements
    selected_columns = ["title", "link", "article:published_time", "og:description", "author"]

    # item count
    item_count = 0

    special_char = '[-\+!~@#$%^&*()={}\[\]:;<.>?/\'"_]'

    filename = search.replace(" ", "_")
    file_path = f"../excel/{filename}"
    excel_file = f"{file_path}_search_results.xlsx"

    wb = xlsxwriter.Workbook(excel_file)
    ws = wb.add_worksheet()

    for col_num, key in enumerate(selected_columns):
        new_key = re.sub(rf'{special_char}', ' ', key)
        ws.write(0, col_num, new_key.title())

    while item_count < 1:

        items = data["items"]

        # locates items in the json file
        data_items = items[item_count]

        # loops through each item in dictionary and prints the specific items

        col_num = 0
        for key in selected_columns:
            value = data_items.get(key)  # Get the value for the key or an empty string if key not present
            ws.write(item_count + 1, col_num, value)
            col_num += 1

        col_num = 0
        metatags_items = items[item_count]["pagemap"]["metatags"][0]
        for key in selected_columns:
            value = metatags_items.get(key, "")  # Get the value for the key or an empty string if key not present
            ws.write(item_count + 1, col_num, value)
            col_num += 1
        item_count += 1

    wb.close()
    f.close()

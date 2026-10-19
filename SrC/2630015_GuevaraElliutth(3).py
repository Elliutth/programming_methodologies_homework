# ============================================================
# Cover
# Name: [Your Name]
# Student ID: [Your Student ID]
# Group: [Your Group]
# File: student_LastNameFirstName.py
#
# Executive Summary
# A list is an ordered, mutable collection that can be changed after creation.
# A tuple is an ordered, immutable collection that is useful for fixed data.
# Lists support operations such as adding, removing, searching, and sorting.
# Tuples allow indexed access to values that should remain unchanged.
# This assignment practices lists and tuples through practical examples.
# Each problem includes its description, inputs, outputs, validations, and
# three test cases: normal, border, and error.
#
# Good Practices
# - Use lists when elements need to be added or removed frequently.
# - Use tuples for fixed data such as coordinates or configurations.
# - Avoid changing a list while iterating over it unless necessary.
# - Use clear variable names and messages.
# - Validate inputs before processing them.
# ============================================================

import math


# ============================================================
# Problem 1: Shopping List Basics (List Operations)
#
# Description:
# Creates a list of products, adds a new product, displays the
# number of items, and checks whether a product is in the list.
#
# Inputs:
# - initial_items_text: comma-separated product names.
# - new_item: product to add.
# - search_item: product to search for.
#
# Outputs:
# - Items list
# - Total items
# - Found item (True/False)
#
# Validations:
# - The initial list, new item, and search item cannot be empty.
# - Extra spaces around product names are removed.
#
# Test cases:
# 1) Normal: "apple, banana", new item "orange", search "apple".
# 2) Border: "apple", new item "apple", search "apple".
# 3) Error: empty initial list or empty new/search item.
# ============================================================

def problem_1():
    print("\\n--- Problem 1: Shopping List Basics ---")
    initial_items_text = input("Enter products separated by commas: ").strip()
    if not initial_items_text:
        print("Error: invalid input")
        return

    items_list = [item.strip() for item in initial_items_text.split(",") if item.strip()]
    if not items_list:
        print("Error: invalid input")
        return

    new_item = input("Enter a product to add: ").strip()
    search_item = input("Enter a product to search for: ").strip()
    if not new_item or not search_item:
        print("Error: invalid input")
        return

    items_list.append(new_item)
    is_in_list = search_item in items_list

    print("Items list:", items_list)
    print("Total items:", len(items_list))
    print("Found item:", str(is_in_list).lower())


# ============================================================
# Problem 2: Points and Distances with Tuples
#
# Description:
# Stores two 2D points in tuples, calculates their Euclidean
# distance, and creates a tuple containing their midpoint.
#
# Inputs:
# - x1, y1, x2, y2: numeric coordinates.
#
# Outputs:
# - Point A, Point B, Distance, Midpoint.
#
# Validations:
# - All four coordinates must be convertible to float.
#
# Test cases:
# 1) Normal: (0, 0) and (3, 4), distance 5.
# 2) Border: identical points (2, 2) and (2, 2), distance 0.
# 3) Error: enter a non-numeric coordinate such as "hello".
# ============================================================

def problem_2():
    print("\\n--- Problem 2: Points and Distances ---")
    try:
        x1 = float(input("Enter x1: ").strip())
        y1 = float(input("Enter y1: ").strip())
        x2 = float(input("Enter x2: ").strip())
        y2 = float(input("Enter y2: ").strip())
    except ValueError:
        print("Error: invalid input")
        return

    point_a = (x1, y1)
    point_b = (x2, y2)
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    midpoint = ((x1 + x2) / 2, (y1 + y2) / 2)

    print("Point A:", point_a)
    print("Point B:", point_b)
    print("Distance:", round(distance, 4))
    print("Midpoint:", midpoint)


# ============================================================
# Problem 3: Product Catalog (Dictionary section omitted)
# This problem is intentionally omitted because the user requested
# a version excluding the dictionary part.
# ============================================================


# ============================================================
# Problem 4: Student Grades (Dictionary section omitted)
# This problem is intentionally omitted because the user requested
# a version excluding the dictionary part.
# ============================================================


# ============================================================
# Problem 5: Word Frequency Counter (Dictionary section omitted)
# This problem is intentionally omitted because the user requested
# a version excluding the dictionary part.
# ============================================================


# ============================================================
# Problem 6: Simple Contact Book (Dictionary CRUD section omitted)
# This problem is intentionally omitted because the user requested
# a version excluding the dictionary part.
# ============================================================


# ============================================================
# Main Menu
# ============================================================

def main():
    while True:
        print("\\n=== Python Collections Practice (Lists and Tuples Only) ===")
        print("1. Shopping list")
        print("2. Points and distances")
        print("0. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            problem_1()
        elif choice == "2":
            problem_2()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Error: invalid input")


if __name__ == "__main__":
    main()


# ============================================================
# Conclusions
# Lists are useful when a collection needs to change over time.
# They support adding, removing, searching, and sorting elements.
# Tuples are appropriate for fixed groups of related values.
# Tuple coordinates make point data easy to read and keep together.
# Both lists and tuples support indexing and the len() function.
# Choosing the right collection makes programs clearer and easier to maintain.
#
# References
# 1) Python Documentation - Built-in Types:
#    https://docs.python.org/3/library/stdtypes.html
# 2) Python Tutorial - Data Structures:
#    https://docs.python.org/3/tutorial/datastructures.html
# 3) Python Documentation - math module:
#    https://docs.python.org/3/library/math.html
# 4) Python Documentation - Built-in Functions:
#    https://docs.python.org/3/library/functions.html
# 5) Python Tutorial - Errors and Exceptions:
#    https://docs.python.org/3/tutorial/errors.html
#
# Note: Add your GitHub repository URL to your assignment submission.
# ============================================================
"""
A list of items and each item has its name, relevance and price.
After sorting the items by (name: 0, relevance: 1, price: 2),
find out a list of items displayed in a chosen page

Given a list of items, the sort column, the sort order (0: ascending, 1: descending), the number
of items to be displayed in each page and a page number, write an algorithm to determine the 
list of item names in the specified page while respecting the item's order (page num starts at 0)

Input:
    1. numOfItems, an integer representing the number of items
    2. items, a map of string as key representing the name and pair of integers as values
       representing the relevance, price
    3. sortParameter, an integer representing the value used for sorting (0 for name, 
       1 for relevance, 2 for price)
    4. sortOrder, an integer representing the order of sorting (0 for ascending order and 1 descending)

Output:
    return a list of string representing the item names on the requested page in the order they are
    displayed

Constraints:
    1 <= numOfItems < 10^5
    0 <= relevance, price < 10^8
    0 <= pageNumber < 10

Note:
    itemsPerpage is always greater than 0, and is always less than the minimum of numOfItems and 20

Example:
    Input:
        numOfItems = 3
        items = [["item1", 10, 15], ["item2", 3, 4], ["item3", 17, 8]]
        sortParameter = 1
        sortOrder = 0
        itemsPerpage = 2
        pageNumber = 1
    Output:
        ["item3"]
"""
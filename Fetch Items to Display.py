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
    5. itemsPerPage, an integer representing the number of items per page
    6. pageNumber, an integer representing the page number

Output:
    return a list of string representing the item names on the requested page in the order they are displayed

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
    Explanation:
        There are 3 items.
        Sort them by relevance(sortParameter = 1) in ascending order ( items = [["item2", 3, 4], ["item1", 10,15], ["item3", 17, 8]]).
        Display up to 2 items on each page.
        The page 0 contains 2 item names ["item2", "item1"] and page 1 contains only 1 item name ["item3"].
        So, the output is "item3".
    Signature:
        List<String> fetchItemsToDisplay(int numOfItems, HashMap<String, PairInt> items, int sortParameter, int sortOrder, int itemsPerPage, int pageNumber);
"""


"""
1. map to list then sort
2. PQ
3. 
"""

class Solution:
    # solution 1: 
    def fetchItemsToDisplay1(self, numOfItems, items, sortParameter, sortOrder, itemsPerPage, pageNumber):
        ans = []

        if not items or len(items) == 0:
            return ans
        
        currPage = 0
        currItems = 1
        sortKey = [lambda x : x, lambda x : items[x][0], lambda x : items[x][1]]
        for name in sorted(items, reverse = sortOrder, key = sortKey[sortParameter]):
            if currPage > pageNumber:
                break
            if currPage == pageNumber:
                ans.append(name)
            if currItems == itemsPerPage:
                currPage += 1
                currItems = 1
            currItems += 1
        return ans
        
            
if __name__ == "__main__":
    # test case : should return ["item3"]
    numOfItems = 3
    items = {'item1': (10,15), 'item2': (3,4), 'item3': (17,8)}
    sortParameter=1
    sortOrder = 0
    itemsPerPage=2
    pageNumber=1
    case = Solution()
    print(case.fetchItemsToDisplay1(numOfItems, items, sortParameter, sortOrder, itemsPerPage, pageNumber))
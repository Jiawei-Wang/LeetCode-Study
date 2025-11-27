class ProductOfNumbers:

    def __init__(self):
        self.prefix_product = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.prefix_product = [1] # if num is 0, reset prefix_product
        else:
            self.prefix_product.append(self.prefix_product[-1] * num)

    def getProduct(self, k):
        if k >= len(self.prefix_product): 
            return 0 # if 0 in last k elements, return 0
        return self.prefix_product[-1] // self.prefix_product[-k - 1]

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
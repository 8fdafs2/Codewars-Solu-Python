class Solution():
    def __init__(self):
        self.cakes = self.cakes_02

    def cakes_01(self, recipe, available):
        ret = 2147483647
        for ingredient in recipe:
            if ingredient not in available:
                return 0
            ret = min(ret, available[ingredient] // recipe[ingredient])
        return ret

    def cakes_02(self, recipe, available):
        return min([available.get(ingredient, 0) // recipe[ingredient] for ingredient in recipe])


if __name__ == '__main__':
    sol = Solution()

    print((sol.cakes({'flour': 500, 'sugar': 200, 'eggs': 1},
                    {'flour': 1200, 'sugar': 1200, 'eggs': 5, 'milk': 200})))

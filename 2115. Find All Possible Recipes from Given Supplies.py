class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        hashmap = dict()
        for i in range(len(recipes)):
            hashmap[recipes[i]] = ingredients[i]
        
        supplies = set(supplies)
        recipes_set = set(recipes)

        can_make = set()
        cannot_make = set()

        # we need to track recipes currently in the recursion stack
        # to avoid dependency cycles: a is b's ingredient, b is a's ingredient
        visiting = set() 

        def check(recipe):
            # Return early if we already solved this recipe
            if recipe in can_make:
                return True
            if recipe in cannot_make:
                return False
            
            # If we hit a recipe currently being visited, we found a cycle
            if recipe in visiting:
                return False
            
            visiting.add(recipe)
            
            ingredient = hashmap[recipe]
            for ing in ingredient:
                if ing not in recipes_set:
                    if ing not in supplies:
                        cannot_make.add(recipe)
                        visiting.remove(recipe)
                        return False
                else:
                    # Simply recursively check; the early returns at the top handle the rest
                    if not check(ing):
                        cannot_make.add(recipe)
                        visiting.remove(recipe)
                        return False
            
            visiting.remove(recipe)
            can_make.add(recipe)
            return True

        for recipe in recipes:
            check(recipe)

        return list(can_make)
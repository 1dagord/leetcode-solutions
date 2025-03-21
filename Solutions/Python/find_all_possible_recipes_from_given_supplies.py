"""
    [MEDIUM]
    2115. Find All Possible Recipes from Given Supplies

    Concepts:
    - hash table
    - topological sort

    Stats:
        Runtime | 47 ms     [Beats 81.60%]
        Memory  | 26.08 MB  [Beats 18.72%]
"""

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        possible = {s : True for s in supplies}
        kitchen = dict(zip(recipes, ingredients))

        def dfs(recipe: str) -> bool:
            nonlocal possible

            if recipe in possible:
                return possible[recipe]

            if recipe not in kitchen:
                return False

            # assume impossible until all
            # dependencies are possible
            possible[recipe] = False

            for ingr in kitchen[recipe]:
                # if any dependency impossible,
                # current recipe impossible
                if not dfs(ingr):
                    return False

            possible[recipe] = True
            return possible[recipe]

        return [r for r in recipes if dfs(r)]
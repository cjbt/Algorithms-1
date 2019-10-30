#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    # if ingredients does not match recipe properties
    batch = float("inf")
    results = {}
    # keep track of item's frequency, loop through dictionary and return lowest number
    for item in recipe:
        if item in ingredients:
            while ingredients[item] >= recipe[item]:
                if item not in results:
                    results[item] = 1
                else:
                    results[item] += 1
                ingredients[item] = ingredients[item] - recipe[item]
        else:
            return 0
    for item in results:
        if results[item] < batch:
            batch = results[item]
    return batch


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))

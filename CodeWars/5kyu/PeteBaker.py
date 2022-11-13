def cakes(recipe, available):
    for i in recipe:
        if i not in available:
            return 0
    else:
        for i in available.copy():
            if i not in recipe:
                available.pop(i)

        values = []
        for i in available:
            values.append(available[i] // recipe[i])
        return min(values)

recipe = {'apples': 69, 'pears': 80, 'milk': 41} 
available = {'sugar': 8153, 'crumbles': 149, 'flour': 3475, 'butter': 6022, 'chocolate': 4516, 'nuts': 3709, 'milk': 6927, 'cocoa': 5490, 'pears': 4351, 'eggs': 1170}
print(cakes(recipe, available))
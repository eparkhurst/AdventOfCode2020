f = open('input.txt', 'r')
raw_rows = f.read().strip().split('\n')
f.close()

def main():
    split_rows = []
    all_allergens = set()
    for row in raw_rows:
        row = row[:-1]
        split = row.split(' (contains ')
        split[0] = set(split[0].split(' '))
        allergens = split[1].split(', ')
        all_allergens.update(allergens)
        split[1] = allergens
        split_rows.append(split)
    remove_known(split_rows, all_allergens)

def sorter(e):
    return e[1]


def remove_known(rows, allergens):
    run = True
    all_ingredients = []
    while run:
        stuff = check_for_match(rows, allergens)
        all_ingredients.append(stuff)
        for row in rows:
            row[0].discard(stuff[0])
        allergens.remove(stuff[1])
        if len(allergens) < 1:
            run = False

    print(all_ingredients)

    all_ingredients.sort(key=sorter)

    print(all_ingredients)

    ingredients_string = ''
    for ingredient in all_ingredients:
        ingredients_string += ingredient[0] + ','
    print(ingredients_string)

def check_for_match(rows, allergens):
    for allergen in allergens:
        rows_containing = []
        ingredients = False
        for row in rows:
            if allergen in row[1]:
                rows_containing.append(row[0])
                if not ingredients:
                    ingredients = row[0]
                else:
                    ingredients = ingredients.intersection(row[0])
        if len(ingredients) == 1:
            return (ingredients.pop(), allergen)

if __name__ == "__main__":
    main()

    bktzrz,bvgm,gbtmdb,hxntcz,rdksxt,srzqtccv,vfvvnm,xknb
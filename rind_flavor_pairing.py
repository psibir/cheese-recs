import csv

cheeses_file = 'cheeses_tab.tsv'
food_file = 'foods.csv'

def rind_flavor_pairing(cheeses_file, food_file):
    cheese_data = []
    food_data = []

    # Read cheeses from cheeses_tab.tsv
    with open(cheeses_file, 'r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter='\t')
        for row in reader:
            cheese_data.append(row)

    # Read food from food.csv
    with open(food_file, 'r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            food_data.append(row)

    for cheese in cheese_data:
        rind = cheese['rind']

        matching_foods = {
            "Spread": None,
            "Platform": None,
            "Dried Fruit": None,
            "Fresh Fruit": None,
            "Pickled": None,
            "Nut": None,
            "Vegetable": None
        }

        for food in food_data:
            food_kind = food['kind']
            food_name = food['food']
            food_flavor = food['food_flavor']

            if rind == "washed" and any(word in food_flavor for word in ["Savory", "Smokey", "Aged", "Garlicky", "Tangy", "Nutty", "Briney", "Vegetal"]):
                if matching_foods["Spread"] is None and food_kind == "Spread":
                    matching_foods["Spread"] = food_name
                if matching_foods["Platform"] is None and food_kind == "Platform":
                    matching_foods["Platform"] = food_name
                if matching_foods["Dried Fruit"] is None and food_kind == "Dried Fruit":
                    matching_foods["Dried Fruit"] = food_name
                if matching_foods["Fresh Fruit"] is None and food_kind == "Fresh Fruit":
                    matching_foods["Fresh Fruit"] = food_name
                if matching_foods["Pickled"] is None and food_kind == "Pickled":
                    matching_foods["Pickled"] = food_name
                if matching_foods["Nut"] is None and food_kind == "Nut":
                    matching_foods["Nut"] = food_name
                if matching_foods["Vegetable"] is None and food_kind == "Vegetable":
                    matching_foods["Vegetable"] = food_name

            elif rind == "bloomy" and food_flavor in ["Tangy", "Briney", "Savory"]:
                if matching_foods["Spread"] is None and food_kind == "Spread":
                    matching_foods["Spread"] = food_name
                if matching_foods["Platform"] is None and food_kind == "Platform":
                    matching_foods["Platform"] = food_name
                if matching_foods["Dried Fruit"] is None and food_kind == "Dried Fruit":
                    matching_foods["Dried Fruit"] = food_name
                if matching_foods["Fresh Fruit"] is None and food_kind == "Fresh Fruit":
                    matching_foods["Fresh Fruit"] = food_name
                if matching_foods["Pickled"] is None and food_kind == "Pickled":
                    matching_foods["Pickled"] = food_name
                if matching_foods["Nut"] is None and food_kind == "Nut":
                    matching_foods["Nut"] = food_name
                if matching_foods["Vegetable"] is None and food_kind == "Vegetable":
                    matching_foods["Vegetable"] = food_name

            elif rind == "natural" and any(word in food_flavor for word in ["Savory", "Smokey", "Aged", "Garlicky", "Tangy", "Nutty", "Briney", "Vegetal"]):
                if matching_foods["Spread"] is None and food_kind == "Spread":
                    matching_foods["Spread"] = food_name
                if matching_foods["Platform"] is None and food_kind == "Platform":
                    matching_foods["Platform"] = food_name
                if matching_foods["Dried Fruit"] is None and food_kind == "Dried Fruit":
                    matching_foods["Dried Fruit"] = food_name
                if matching_foods["Fresh Fruit"] is None and food_kind == "Fresh Fruit":
                    matching_foods["Fresh Fruit"] = food_name
                if matching_foods["Pickled"] is None and food_kind == "Pickled":
                    matching_foods["Pickled"] = food_name
                if matching_foods["Nut"] is None and food_kind == "Nut":
                    matching_foods["Nut"] = food_name
                if matching_foods["Vegetable"] is None and food_kind == "Vegetable":
                    matching_foods["Vegetable"] = food_name

        # Print the best matching foods for each category
        print(f"Best food pairings for {cheese['cheese']} (Rind: {rind}):")
        for category, food in matching_foods.items():
            if food is not None:
                print(f"{category}: {food}")
        print()

rind_flavor_pairing(cheeses_file, food_file)



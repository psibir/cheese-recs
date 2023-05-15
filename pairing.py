import csv
import food_pairing_ruleset as ruleset

class Cheese:
    def __init__(self, cheese, milk, origin, region, family, kind, fat, calcium, rind, texture, color, flavor, aroma, producer, synonyms, alternative_spellings, vegetarian, description):
        self.cheese = cheese
        self.milk = milk
        self.origin = origin
        self.region = region
        self.family = family
        self.kind = kind
        self.fat = fat
        self.calcium = calcium
        self.rind = rind
        self.texture = texture
        self.color = color
        self.flavor = flavor
        self.aroma = aroma

class Food:
    def __init__(self, food, kind, food_texture, food_flavor, compliment_flavor, bridge_flavor, contrastive_flavor, cleaving_flavor):
        self.food = food
        self.kind = kind
        self.food_texture = food_texture
        self.food_flavor = food_flavor
        self.compliment_flavor = compliment_flavor
        self.bridge_flavor = bridge_flavor
        self.contrastive_flavor = contrastive_flavor
        self.cleaving_flavor = cleaving_flavor

class CheesePairing:
    def __init__(self, cheese_name):
        self.cheese_name = cheese_name
        self.cheeses = self.read_cheeses('cheeses_tab.tsv')
        self.foods = self.read_foods('foods.csv')
        self.pairings = self.get_cheese_pairings()

    def read_cheeses(self, file):
        cheeses = []
        with open(file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f, delimiter='\t')
            for row in reader:
                cheese = Cheese(**row)
                cheeses.append(cheese)
        return cheeses

    def read_foods(self, file):
        foods = []
        with open(file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                food = Food(**row)
                foods.append(food)
        return foods

    def pair_cheese_with_food(self, cheese_name):
        pairings = []
        for cheese_item in self.cheeses:
            if cheese_item.cheese == cheese_name:
                for food in self.foods:
                    # Congruent FlavorRuleSet
                    ruleset.congruent
                    if (
                        food.kind in ["Spread", "Platform", "Dried Fruit", "Fresh Fruit", "Pickled", "Nut", "Vegetable"]
                        and food.complement_flavor in cheese_item.flavor
                        and cheese_item.texture == food.food_texture
                        and cheese_item.aroma in food.compliment_flavor
                    ):
                        pairings.append({food.food: food.kind})
        return pairings

# Usage example
cheese_pairing = CheesePairing('cheeses_tab.tsv', 'foods.csv')
user_input = input("What cheese would you like to pair with food? ")
pairings = cheese_pairing.pair_cheese_with_food(user_input)
for pairing in pairings:
    for food, kind in pairing.items():
        print(f"Pairing {user_input} with {food} ({kind})")

# FOOD PAIRING RULESETS

def init():
    self.congruent_flavor_ruleset = congruent
    
    }

def pairing_objective(pairing):
    


# MILK-FLAVOR RULES -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# cow's milk - 
# goat's milk -
# sheep's milk -
# buffalo's milk -


# KIND-FLAVOR RULES -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# soft - Sweet, Salty, Neutral, Savory, Tart, Acidic, Herbaceous, 
# semi-soft - Sweet, Vegetal, Briney, Savory, Bitter, 
# semi-hard - Nutty, Sweet, Chocolate, Briney, Tangy, Peppery, Sharp, Aged,
# hard - Nutty, Sweet, Tangy, Tart, Spicy, Garlicky, Smokey, Vegetal
# blue - Nutty, Tangy, Smokey, Aged, Briney, Chocolate, Savory


# RIND-FLAVOR RULES -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# Washed - Savory, Smokey, Aged, Garlicky, Tangy, Nutty, Briney, Vegetal
# Bloomy - Tangy, Briney, Savory
# soft-ripened - Savory, Smokey, Aged, Garlicky, Tangy, Nutty, Briney, Vegetal

def __init__(self, cheese, rind, food, food_flavor):
    self.cheese.rind = rind
    self.food.food_flavor = food_flavor
    


if rind == "Washed":
    if ["Savory", "Smokey", "Aged", "Garlicky", "Tangy", "Nutty", "Briney", "Vegetal"] in food_flavor:
        # Pair the cheese with the food
        print("Pair the Washed rind cheese with the food.")

elif cheese_rind == "Bloomy":
    if food_flavor in ["Tangy", "Briney", "Savory"]:
        # Pair the cheese with the food
        print("Pair the Bloomy rind cheese with the food.")

elif cheese_rind == "soft-ripened":
    if food_flavor in ["Savory", "Smokey", "Aged", "Garlicky", "Tangy", "Nutty", "Briney", "Vegetal"]:
        # Pair the cheese with the food
        print("Pair the soft-ripened cheese with the food.")

else:
    # No specific pairing recommendation for the given cheese rind
    print("No specific pairing recommendation for this cheese rind.")



# CONGRUENT FLAVOR HEURISTICS -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

if cheese.flavor == food.flavor and cheese.texture != food.texture:
    return food.food


# COMPLIMENTARY FLAVOR RULES  -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
if food.complement_flavor in food.cheese.flavor and (food.bridge_flavor in (cheese.flavor or cheese.aroma or cheese.texture)):
    return food.food



# CONTRASTIVE FLAVOR RULES-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

food_match = next((food.food for food in foods if cheese_item.flavor in food.compliment_flavor), None)
contrastive_flavor_food = next((food.food for food in foods if food_match and food.food_flavor == food_match), None)





# Complementary pairings: Fresh goat cheese with honey and almonds; Brie with fig jam and crackers; Gouda with apple slices and pecans; Blue cheese with walnuts and dried cranberries.
# Contrasting pairings: Sharp cheddar with dark chocolate; Blue cheese with spicy sausage and olives; Feta with watermelon and mint; Parmesan with lemon and arugula.



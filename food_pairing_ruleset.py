# FOOD PAIRING RULESETS

# MILK-FLAVOR RULES

cow's milk - 
goat's milk -
sheep's milk -
buffalo's milk -


# KIND-FLAVOR RULES

soft - Sweet, Salty, Neutral, Savory, Tart, Acidic, Herbaceous, 
semi-soft - Sweet, Vegetal, Briney, Savory, Bitter, 
semi-hard - Nutty, Sweet, Chocolate, Briney, Tangy, Peppery, Sharp, Aged,
hard - Nutty, Sweet, Tangy, Tart, Spicy, Garlicky, Smokey, Vegetal
blue - Nutty, Tangy, Smokey, Aged, Briney, Chocolate, Savory


# RIND-FLAVOR RULES

Washed - Savory, Smokey, Aged, Garlicky, Tangy, Nutty, Briney, Vegetal
Bloomy - Tangy, Briney, Savory
soft-ripened - Savory, Smokey, Aged, Garlicky, Tangy, Nutty, Briney, Vegetal



# COMMON CHEESE HEURISTICS

if cheese.flavor == food.flavor and cheese.texture != food.texture:
    return food.food


# COMPLIMENTARY FLAVOR RULES  
food.complement_flavor in food.cheese.clavor



# CONTRASTIVE FLAVOR RULES
food_match = next((food.food for food in foods if cheese_item.flavor in food.compliment_flavor), None)
contrastive_flavor_food = next((food.food for food in foods if food_match and food.food_flavor == food_match), None)





# Complementary pairings: Fresh goat cheese with honey and almonds; Brie with fig jam and crackers; Gouda with apple slices and pecans; Blue cheese with walnuts and dried cranberries.
# Contrasting pairings: Sharp cheddar with dark chocolate; Blue cheese with spicy sausage and olives; Feta with watermelon and mint; Parmesan with lemon and arugula.



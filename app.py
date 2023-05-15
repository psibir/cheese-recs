from flask import Flask, render_template, request
from cheese_recommender import CheeseRecommender

app = Flask(__name__)

cheese_file = 'cheeses_tab.tsv'
recommender = CheeseRecommender(cheese_file)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(error):
    return render_template('500.html'), 500

@app.errorhandler(501)
def not_implemented_error(error):
    return render_template('501.html'), 501

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form.get('user_input')
        exclude_words = request.form.get('exclude_words')
        if exclude_words:
            exclude_words = exclude_words.strip().split()
        num_recommendations = 50
        start_index = 0
        
        if not user_input and not exclude_words:
            recommendations = recommender.get_recommendations()
            cheese_details = None
        else:
            recommendations = recommender.get_recommendations(user_input=user_input, num_recommendations=num_recommendations, start_index=start_index, exclude_words=exclude_words)
            cheese_details = None  # Placeholder for selected cheese details
        
        if recommendations.empty:
            return render_template('no_results.html')
        else:
            return render_template('results.html', recommendations=recommendations, cheese_details=cheese_details)
    else:
        return render_template('form.html')


@app.route('/cheese/<int:index>')
def cheese_details(index):
    # Retrieve the cheese details based on the index
    cheese = recommender.df.iloc[index]
    cheese_details = {
        'cheese': cheese['cheese'],
        'milk': cheese['milk'],
        'origin': cheese['origin'],
        'region': cheese['region'],
        'family': cheese['family'],
        'kind': cheese['kind'],
        'fat': cheese['fat'],
        'calcium': cheese['calcium'],
        'rind': cheese['rind'],
        'texture': cheese['texture'],
        'color': cheese['color'],
        'flavor': cheese['flavor'],
        'aroma': cheese['aroma'],
        'producer': cheese['producer'],
        'synonyms': cheese['synonyms'],
        'alternative_spellings': cheese['alternative_spellings'],
        'vegetarian': cheese['vegetarian'],
        'description': cheese['description']
    }

    # Render the cheese details template
    return render_template('cheese_details.html', cheese_details=cheese_details)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/FAQ')
def faq():
    return render_template('FAQ.html')

@app.route('/cheese_library')
def cheese_library():
    cheeses = recommender.get_all_cheeses(cheese_file)
    return render_template('cheese_library.html', cheeses=cheeses)

@app.route('/pairing_form', methods=['GET', 'POST'])
def pairing():
    if request.method == 'POST':
        pairing_type = request.form.get('pairing_type')
        
        if pairing_type == 'food_cheese':
            food = request.form.get('food')
            accentuate_flavor = request.form.get('accentuate_flavor')
            
            cheese_pairing = CheesePairing(food)
            pairings = cheese_pairing.pair_cheese_with_food(food)
            
            return render_template('pairing_results.html', pairing_type=pairing_type, food=food, accentuate_flavor=accentuate_flavor, pairings=pairings)
        
        elif pairing_type == 'cheese_food':
            cheese = request.form.get('cheese')
            flavor = request.form.get('flavor')
            
            # Perform pairing logic for cheese and food accentuation
            # ...
            
            return render_template('pairing_results.html', pairing_type=pairing_type, cheese=cheese, flavor=flavor)
    
    return render_template('pairing_form.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)

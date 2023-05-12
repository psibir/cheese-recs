from flask import Flask, render_template, request
from cheese_recommender import CheeseRecommender
import search

app = Flask(__name__)

cheese_file = 'cheeses_tab.tsv'
recommender = CheeseRecommender(cheese_file)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form.get('user_input')
        exclude_words = request.form.get('exclude_words')
        if exclude_words:
            exclude_words = exclude_words.strip().split()
        num_recommendations = 15
        start_index = 0
        
        if not user_input and not exclude_words:
            recommendations = recommender.get_recommendations()
            cheese_details = None
        else:
            recommendations = recommender.get_recommendations(user_input=user_input, num_recommendations=num_recommendations, start_index=start_index, exclude_words=exclude_words)
            cheese_details = None  # Placeholder for selected cheese details
        
        return render_template('results.html', recommendations=recommendations, cheese_details=cheese_details)
    else:
        return render_template('form.html')


@app.route('/cheese/<int:index>')
def cheese_details(index):
    # Retrieve the cheese details based on the index
    cheese = recommender.df.iloc[index]
    cheese_details = {
        'cheese': cheese['cheese'],
        'country': cheese['origin'],
        'region': cheese['region'],
        'family': cheese['family'],
        'rind': cheese['rind'],
        'milk': cheese['milk'],
        'fat': cheese['fat'],
        'kind': cheese['kind'],
        'description': cheese['description'],
        'producer': cheese['producer'],
        'synonyms': cheese['synonyms']
    }

    # Render the cheese details template
    return render_template('cheese_details.html', cheese_details=cheese_details)


# @app.route('/search', methods=['GET', 'POST'])
# def search():
#     if request.method == 'POST':
#         query = request.form.get('query')
#         results = search(query)
#         return render_template('search_results.html', results=results)
    
#     return render_template('search_form.html')


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/faq')
def faq():
    return render_template('FAQ.html')

# @app.errorhandler('/404')
# def page_not_found(error):
#     return render_template('404.html'),


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)

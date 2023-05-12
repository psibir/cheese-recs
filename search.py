from cheese_recommender import CheeseRecommender

cheese_file = 'cheeses_tab.tsv'
recommender = CheeseRecommender(cheese_file)


# Function to perform the search operation
def search(query):
    results = []

    # Perform the search based on the query
    if query:
        # In this example, we assume 'recommender.df' is a DataFrame containing cheese data
        # You can customize the search logic based on your specific requirements

        # Convert the query to lowercase for case-insensitive search
        query = query.lower()

        for index, cheese in recommender.df.iterrows():
            # Search for the query in different cheese attributes
            if (
                query in cheese['cheese'].lower() or
                query in cheese['origin'].lower() or
                query in cheese['region'].lower() or
                query in cheese['family'].lower() or
                query in cheese['rind'].lower() or
                query in cheese['milk'].lower() or
                query in cheese['kind'].lower() or
                query in cheese['description'].lower() or
                query in cheese['producer'].lower() or
                query in cheese['synonyms'].lower()
            ):
                # Add the matching cheese to the results
                results.append({
                    'index': index,
                    'cheese': cheese['cheese']
                })

    return results


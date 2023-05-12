import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import random



class CheeseRecommender:
    def __init__(self, cheese_file):
        self.df = pd.read_csv(cheese_file, sep='\t')
        self.vectorizer = TfidfVectorizer()

    def get_recommendations(self, user_input=None, num_recommendations=5, start_index=0, exclude_words=None):
        self.df.fillna('', inplace=True)
        cheese_desc = self.df.apply(lambda x: ' '.join(x), axis=1)
        cheese_matrix = self.vectorizer.fit_transform(cheese_desc)

        if user_input is None:
            sim_indices = random.sample(range(len(self.df)), num_recommendations)
        else:
            user_vector = self.vectorizer.transform([user_input])
            sim_scores = cosine_similarity(user_vector, cheese_matrix).flatten()
            sim_indices = sim_scores.argsort()[::-1][start_index:num_recommendations + start_index]

        recommendations = self.df.iloc[sim_indices][
            ['cheese', 'milk', 'origin', 'region', 'kind', 'color', 'texture', 'flavor', 'aroma', 'description',
             'producer']]
        recommendations['origin'] = recommendations['origin'].str.split(',').str[0]

        if exclude_words:
            exclude_words_lower = [word.lower() for word in exclude_words]
            filtered_recommendations = []
            for index, row in recommendations.iterrows():
                should_exclude = False
                for field in ['cheese', 'milk', 'origin', 'region', 'kind', 'color', 'texture', 'flavor', 'aroma', 'description']:
                    if any(word in str(row[field]).lower() for word in exclude_words_lower):
                        should_exclude = True
                        break
                if not should_exclude:
                    filtered_recommendations.append(row)
            recommendations = pd.DataFrame(filtered_recommendations)

        return recommendations

    @classmethod
    def get_all_cheeses(cls, cheese_file):
        df = pd.read_csv(cheese_file, sep='\t')
        return df['cheese'].tolist()
    
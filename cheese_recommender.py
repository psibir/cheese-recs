import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class CheeseRecommender:
    def __init__(self, cheese_file):
        self.df = pd.read_csv(cheese_file, sep='\t')
        self.vectorizer = TfidfVectorizer()

    def get_recommendations(self, user_input=None, num_recommendations=5, start_index=0, exclude_words=None):
        if not user_input:
            return pd.DataFrame(columns=['cheese', 'milk', 'origin', 'region', 'kind', 'color', 'texture', 'flavor', 'aroma', 'description', 'producer'])

        words = user_input.split()
        cheese_columns = ['cheese', 'milk', 'origin', 'region', 'kind', 'color', 'texture', 'flavor', 'aroma', 'producer']
        if not any(any(word in str(val).lower() for val in self.df[col]) for word in words for col in cheese_columns):
            return pd.DataFrame(columns=cheese_columns)

        self.df.fillna('', inplace=True)
        cheese_desc = self.df.apply(lambda x: ' '.join(x), axis=1)
        cheese_matrix = self.vectorizer.fit_transform(cheese_desc)

        user_vector = self.vectorizer.transform([user_input])
        sim_scores = cosine_similarity(user_vector, cheese_matrix).flatten()
        sim_indices = sim_scores.argsort()[::-1]

        # filter out recommendations that do not include the user input if there are less than num_recommendations that contain the user input
        filtered_indices = []
        for i in sim_indices:
            row = self.df.iloc[i][cheese_columns]
            if any(word in str(val).lower() for val in row.values for word in words):
                filtered_indices.append(i)
                if len(filtered_indices) == num_recommendations:
                    break
        sim_indices = filtered_indices[start_index:start_index+num_recommendations]

        recommendations = self.df.iloc[sim_indices][cheese_columns]
        recommendations['origin'] = recommendations['origin'].str.split(',').str[0]

        if exclude_words:
            exclude_words_lower = [word.lower() for word in exclude_words]
            filtered_recommendations = []
            for index, row in recommendations.iterrows():
                should_exclude = False
                for field in cheese_columns:
                    if any(word in str(row[field]).lower() for word in exclude_words_lower):
                        should_exclude = True
                        break
                if not should_exclude:
                    filtered_recommendations.append(row)
            recommendations = pd.DataFrame(filtered_recommendations)

        if recommendations.empty:
            return pd.DataFrame(columns=cheese_columns)

        return recommendations

    @classmethod
    def get_all_cheeses(cls, cheese_file):
        df = pd.read_csv(cheese_file, sep='\t')
        return df['cheese'].tolist()

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from fuzzywuzzy import fuzz

class CheeseRecommender:
    def __init__(self, cheese_file):
        self.df = pd.read_csv(cheese_file, sep='\t')
        self.vectorizer = TfidfVectorizer()

    def get_recommendations(self, user_input=None, num_recommendations=5, start_index=0, exclude_words=None):
        self.df.fillna('', inplace=True)
        cheese_desc = self.df.apply(lambda x: ' '.join(x), axis=1)
        cheese_matrix = self.vectorizer.fit_transform(cheese_desc)

        if user_input is None or not self._is_significant_match(user_input, self.df['cheese']):
            return pd.DataFrame(columns=['cheese', 'milk', 'origin', 'region', 'kind', 'color', 'texture', 'flavor', 'aroma', 'description', 'producer'])

        user_words = user_input.split()
        total_scores = []
        for word in user_words:
            user_vector = self.vectorizer.transform([word])
            sim_scores = cosine_similarity(user_vector, cheese_matrix).flatten()
            total_scores.append(sim_scores)

        averaged_scores = sum(total_scores) / len(user_words)
        sim_indices = averaged_scores.argsort()[::-1][start_index:num_recommendations + start_index]

        recommendations = self.df.iloc[sim_indices][
            ['cheese', 'milk', 'origin', 'region', 'kind', 'color', 'texture', 'flavor', 'aroma', 'description', 'producer']]
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

        if recommendations.empty:
            return pd.DataFrame(columns=['cheese', 'milk', 'origin', 'region', 'kind', 'color', 'texture', 'flavor', 'aroma', 'description', 'producer'])

        return recommendations

    def _is_significant_match(self, user_input, choices, threshold=70):
        words = user_input.split()
        for choice in choices:
            match_scores = [fuzz.token_set_ratio(word, choice) for word in words]
            avg_score = sum(match_scores) / len(words)
            if avg_score >= threshold:
                return True
        return False

    @classmethod
    def get_all_cheeses(cls, cheese_file):
        df = pd.read_csv(cheese_file, sep='\t')
        return df['cheese'].tolist()

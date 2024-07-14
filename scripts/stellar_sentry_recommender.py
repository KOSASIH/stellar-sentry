import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

class StellarSentryRecommender:
    def __init__(self, data):
        self.data = data
        self.vectorizer = TfidfVectorizer()
        self.item_vectors = self.vectorizer.fit_transform(data['description'])

    def get_recommendations(self, user_id, num_recommendations):
        user_vector = self.vectorizer.transform([self.data.loc[user_id, 'description']])
        similarities = cosine_similarity(user_vector, self.item_vectors).flatten()
        indices = np.argsort(-similarities)[:num_recommendations]
        return self.data.iloc[indices]['name'].tolist()

def main():
    # Load data
    data = pd.read_csv('data/recommender_data.csv')

    # Create recommender system
    recommender = StellarSentryRecommender(data)

    # Get recommendations
    user_id = 123
    num_recommendations = 5
    recommendations = recommender.get_recommendations(user_id, num_recommendations)
    print(f'Recommendations for user {user_id}: {recommendations}')

if __name__ == '__main__':
    main()

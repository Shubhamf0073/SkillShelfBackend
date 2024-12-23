from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from scipy.sparse import hstack
import pandas as pd
import os

# Load the dataset
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
df = pd.read_csv(os.path.join(BASE_DIR, 'data', 'PreprocessedDataset.csv'))

# Vectorize the course names and descriptions
vectorizerName = TfidfVectorizer(stop_words="english", max_features=5000)
nameVectors = vectorizerName.fit_transform(df["course_name"].fillna(""))

vectorizerDesc = TfidfVectorizer(stop_words="english", max_features=5000)
descVectors = vectorizerDesc.fit_transform(df["course_description"].fillna(""))

# Combine the vectors
combinedVectors = hstack([nameVectors, descVectors])
cosineSim = cosine_similarity(combinedVectors, combinedVectors)

def recommendCourse(query, topN=5):
    if not query or len(query.strip()) == 0:
        return [], []

    # Vectorize the query
    queryNameVector = vectorizerName.transform([query])
    queryDescVector = vectorizerDesc.transform([query])

    queryCombinedVector = hstack([queryNameVector, queryDescVector])

    # Compute the cosine similarity
    querySim = cosine_similarity(queryCombinedVector, combinedVectors)

    # Get the top N similar courses
    simScore = list(enumerate(querySim[0]))
    simScore = sorted(simScore, key=lambda x: x[1], reverse=True)

    topCourses = []
    topScores = []

    for i in range(topN):
        courseIndex = simScore[i][0]
        courseInfo = {
            "course_name": df.iloc[courseIndex]["course_name"],
            "university": df.iloc[courseIndex]["university"],
            "rating": df.iloc[courseIndex]["course_rating"],
            "level": df.iloc[courseIndex]["difficulty_level"],
            "link": df.iloc[courseIndex]["course_url"]
        }
        topCourses.append(courseInfo)
        topScores.append(simScore[i][1])

    return topCourses, topScores
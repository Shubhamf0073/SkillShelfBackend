from flask import Flask, request, jsonify
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'models')))

from vectorising import recommendCourse

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to SkillShelf API"

@app.route('/search', methods=['POST'])
def search():
    if request.content_type != 'application/json':
        return jsonify({'error': 'Unsupported Media Type'}), 415
    data = request.json
    query = data.get('query', '')
    if query:
        print(f"Received query: {query}")
        recommendedCourses, scores = recommendCourse(query, topN=5)
        print(f"Recommended courses: {recommendedCourses}")
        response = jsonify({
            'courses': recommendedCourses,  # Already a list
            'scores': scores  # Already a list
        })
        return response
    else:
        return jsonify({'error': 'Please enter a search query'}), 400

if __name__ == "__main__":
    app.run(debug=True)
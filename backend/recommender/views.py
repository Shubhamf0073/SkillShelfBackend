from django.shortcuts import render
from django.http import JsonResponse
from .models import Course
import pandas as pd

def recommend_courses(request):
    # Load the dataset
    dataset_path = 'dataset/PreprocessedDataset.csv'
    data = pd.read_csv(dataset_path)

    # Example logic for course recommendation
    recommended_courses = data.sample(n=5)  # Randomly select 5 courses for demonstration

    # Prepare the response data
    response_data = recommended_courses.to_dict(orient='records')

    return JsonResponse(response_data, safe=False)
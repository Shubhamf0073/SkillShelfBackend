from django.http import JsonResponse, HttpResponse
from .vectorising import recommendCourse

def recommend_view(request):
    query = request.GET.get('query', '')
    topN = int(request.GET.get('topN', 5))
    courses, scores = recommendCourse(query, topN)
    return JsonResponse({'courses': courses, 'scores': scores})

def home_view(request):
    return HttpResponse("Welcome to the SkillShelf Recommender System API")
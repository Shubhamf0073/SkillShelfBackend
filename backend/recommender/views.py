from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Course
from .serializers import CourseSerializer
import numpy as np
from neural_network.model import NeuralNetwork

class CourseList(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class RecommendCourse(APIView):
    def post(self, request, *args, **kwargs):
        answers = request.data.get('answers')
        # Convert answers to numpy array and preprocess as needed
        X = np.array(answers).reshape(1, -1)
        # Load the trained neural network model
        nn = NeuralNetwork.load_model('neural_network_model.pkl')
        # Predict the recommended course
        prediction = nn.predict(X)
        recommended_course_index = int(prediction[0])
        recommended_course_name = Course.objects.values_list('course_name', flat=True).distinct()[recommended_course_index]
        recommended_course = Course.objects.get(course_name=recommended_course_name)
        serializer = CourseSerializer(recommended_course)
        return Response({'recommended_course': serializer.data}, status=status.HTTP_200_OK)
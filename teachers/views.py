from rest_framework import generics

from .models import Teacher
from .serializers import TeacherSerializer


class TeacherListCreateView(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

    # Filtering
    filterset_fields = ["subject", "is_active"]

    # Search
    search_fields = [
        "first_name",
        "last_name",
        "email",
        "subject",
    ]

    # Sorting
    ordering_fields = [
        "first_name",
        "last_name",
        "experience_years",
        "joining_date",
        "created_at",
    ]


class TeacherDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

from rest_framework.viewsets import ModelViewSet

from oiproblems.models import Problem
from oiproblems.serializer import ProblemSerializer


class ProblemViewSet(ModelViewSet):
    queryset = Problem.objects.all()
    serializer_class = ProblemSerializer

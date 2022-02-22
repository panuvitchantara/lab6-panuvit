from rest_framework.response import Response
from rest_framework.decorators import api_view
from counter.models import Count
from .serializers import CountSerializer
from rest_framework.renderers import JSONRenderer

@api_view(['GET'])
def getData(request):
    counts = Count.objects.all()
    serialiser = CountSerializer(counts, many=True)
    return Response(serialiser.data)

from rest_framework.response import Response
# from rest_framework import status
from rest_framework.decorators import api_view
from .models import Count
from .serializers import CountSerializer
# from django.http import JsonResponse


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'Total View' : '/counter-list/',
        # 'Detail View' : '/counter-detail/<str:pk>/',
        'Create' : '/counter-create/',
        # 'Update' : '/counter-update/<str:pk>/',
        # 'Delete' : '/counter-delete/<str:pk>/',
    }
    return Response(api_urls)


@api_view(['GET'])
def countList(request):
    counts = Count.objects.all()
    serialiser = CountSerializer(counts, many=True)
    return Response(serialiser.data)

# @api_view(['GET'])
# def countDetail(request, pk):
#     counts = Count.objects.get(id=pk)
#     serialiser = CountSerializer(counts, many=False)
#     return Response(serialiser.data)

@api_view(['POST'])
def countCreate(request):
    serialiser = CountSerializer(data=request.data)

    if serialiser.is_valid():
        serialiser.save()

    return Response(serialiser.data)

# @api_view(['POST'])
# def countUpdate(request, pk):
#     count = Count.objects.get(id=pk)
#     serialiser = CountSerializer(instance=count, data=request.data)

#     if serialiser.is_valid():
#         serialiser.save()

#     return Response(serialiser.data)

# @api_view(['DELETE'])
# def countDelete(request, pk):
#     count = Count.objects.get(id=pk)
#     count.delete()
#     return Response('Item was deteted.')

    
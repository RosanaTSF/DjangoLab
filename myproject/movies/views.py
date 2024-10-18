from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET', 'POST'])
def hello_word(request):
    if request.method == 'POST':
        name = request.data.get('name', '')
        return Response({'message': f'Hello {name}!'})
    return Response({'message': 'Hello API!'})
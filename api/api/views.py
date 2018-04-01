# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


@api_view(['GET'])
def get_notifications(request):
    if request.method == "POST":
        return Response({"message":"Bad Request"}, status = status.HTTP_400_BAD_REQUEST)
    else:
        request_data  = request.data
        return Response({"message": request_data})


@api_view(['POST'])
def set_notifications(request):
    if request.method == "GET":
        return Response({"message":"Bad Request"}, status = status.HTTP_400_BAD_REQUEST)
    else:
	request_data = request.data
	return Response({"message":request_data})


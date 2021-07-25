from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.http import JsonResponse
from .serializers import CalculateSumSerializer
from .models import CalculateSum
import time
import string
import random


# Simple get api which gives string as response
@api_view(['GET'])
def api_overview(request):
    data = {
        "Status_Code": status.HTTP_200_OK,
        "Response": "Hi from test API"
    }
    return JsonResponse(data, safe=False)


# Get api which take 2 number from the url and create entry in databases
@api_view(['GET'])
def calculate(request, number1, number2):
    # generating the unique Identifier
    id = unique_identifier_generator()
    # Creating data in json format to store data in db
    data = {
        "number1": number1,
        "number2": number2,
        "answer": 0,
        "uniqueIdentifier": id
    }
    serializer = CalculateSumSerializer(data=data)
    # checking that our serializer is valid or not if valid the save it
    if serializer.is_valid():
        serializer.save()
    # return unique identifier as response
    data = {
        "Status_Code": status.HTTP_200_OK,
        "Unique_Identifier": serializer.data['uniqueIdentifier']
    }

    return JsonResponse(data, safe=False)


# get api which takes the unique identifier from the url and calculate the sum of 2 number and update into the DB
@api_view(['GET'])
def get_answer(request, unique_identifier):
    try:
        # fetch data from database corresponding to unique identifier
        db_record = CalculateSum.objects.get(uniqueIdentifier=unique_identifier)
    except:
        # if data not found in db return the error message.
        data = {
            "Status_Code": status.HTTP_404_NOT_FOUND,
            "Response": "Identifier Does not exist in database"
        }
        return JsonResponse(data, safe=False)

    serializer = CalculateSumSerializer(db_record, many=False)
    # sleep for 10 second
    time.sleep(10)
    # calculate the sum of 2 number 
    answer = serializer.data['number1'] + serializer.data['number2']
    data = {'answer': answer}
    # Update the answer into DB corresponding to their unique identifier
    serializer_sum_queue = CalculateSumSerializer(instance=db_record, data=data, partial=True)
    if serializer_sum_queue.is_valid():
        serializer_sum_queue.save()
    # return the response
    # result = "Sum of " + str(serializer.data['number1']) + " and " + str(serializer.data['number2']) + " is: " + str(
    #     answer)
    data = {
        "Status_Code": status.HTTP_200_OK,
        "Calculated_Sum": answer
    }
    return JsonResponse(data, safe=False)


def unique_identifier_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

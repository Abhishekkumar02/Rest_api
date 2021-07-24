from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import CalculateSumSerializer
from .models import CalculateSum
from rest_framework.exceptions import NotFound
import time
import string
import random


# Simple get api which gives string as response
@api_view(['GET'])
def api_overview(request):
    api_urls = "Hi from test API"
    return Response(api_urls)


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
    return Response(serializer.data['uniqueIdentifier'])


# get api which takes the unique identifier from the url and calculate the sum of 2 number and update into the DB
@api_view(['GET'])
def get_answer(request, unique_identifier):
    try:
        # fetch data from database corresponding to unique identifier
        db_record = CalculateSum.objects.get(uniqueIdentifier=unique_identifier)
    except:
        # if data not found in db return the error message.
        raise NotFound("Does not exist in databases")

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
    res = "Sum of " + str(serializer.data['number1']) + " and " + str(serializer.data['number2']) + " is: " + str(
        answer)
    return Response(res)


def unique_identifier_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

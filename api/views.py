from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from api.models import Campaign, Update, Donation
from api.serializers import CampaignSerializer, UpdateSerializer, DonationSerializer
import json
import requests
import numpy as np
# import stripe

# CLASS NAMES HAVE BEEN UPDATED, BUT THE LOGIC NEEDS UPDATING

class CampaignList(APIView):
    '''Get all campaigns or create a campaign'''
    @csrf_exempt
    def get(self, request, format=None):
        camp = Campaign.objects.all()
        #UPDATE TITLE AFTER CREATING MODELS
        if request.query_params.get('title'):
            camp = camp.filter(title__contains=request.query_params.get('title'))
        serializer = CampaignSerializer(camp, many=True)
        return Response(serializer.data)

    @csrf_exempt
    def post(self, request, format=None):
        serializer = CampaignSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CampaignDetail(APIView):
    '''Work with an individual Campaign object'''
    @csrf_exempt
    def get(self, request, pk, format=None):
        camp = Campaign.objects.get(id=pk)
        serializer = CampaignSerializer(camp)
        return Response(serializer.data)

    @csrf_exempt
    def put(self, request, pk, format=None):
        camp = Campaign.objects.get(id=pk)
        serializer = CampaginSerializer(cat, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @csrf_exempt
    def delete(self, request, pk, format=None):
        camp = Campaign.objects.get(id=pk)
        camp.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UpdateList(APIView):
    '''Get all Update or create a Update'''
    @csrf_exempt
    def get(self, request, format=None):
        upd = Update.objects.all()
        #update category after making the models
        if request.query_params.get('update_id'):
            upd = upd.filter(title__contains=request.query_params.get('update_id'))
        serializer = UpdateSerializer(upd, many=True)
        return Response(serializer.data)

    @csrf_exempt
    def post(self, request, format=None):
        serializer = UpdateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateDetail(APIView):
    '''Work with an individual Update object'''
    @csrf_exempt
    def get(self, request, pk, format=None):
        upd = Update.objects.get(id=pk)
        serializer = UpdateSerializer(upd)
        return Response(serializer.data)

    @csrf_exempt
    def put(self, request, pk, format=None):
        upd = Update.objects.get(id=pk)
        serializer = UpdateSerializer(upd, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @csrf_exempt
    def delete(self, request, pk, format=None):
        upd = Update.objects.get(id=pk)
        upd.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class DonationList(APIView):
    '''Get all donations or create a Donation'''
    @csrf_exempt
    def get(self, request, format=None):
        don = Donation.objects.all()
        #update after doing the models
        if request.query_params.get('id'):
            don = don.filter(title__contains=request.query_params.get('id'))
        serializer = DonationSerializer(don, many=True)
        return Response(serializer.data)

    @csrf_exempt
    def post(self, request, format=None):
        serializer = DonationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DonationDetail(APIView):
    '''Work with an individual Donation object'''
    @csrf_exempt
    def get(self, request, pk, format=None):
        don = Donation.objects.get(id=pk)
        serializer = DonationSerializer(don)
        return Response(serializer.data)

    @csrf_exempt
    def put(self, request, pk, format=None):
        don = Donation.objects.get(id=pk)
        serializer = DonationSerializer(cat, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @csrf_exempt
    def delete(self, request, pk, format=None):
        don = Donation.objects.get(id=pk)
        don.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class Predict(APIView):
    '''predicts success score off of given inputs'''
    @csrf_exempt
    def post(self, request, format=None):
        body = json.loads(request.body) # import this library at top..dont need to install tho
        body = body['values']

        #log + 1 goal
        body['goal_lnplus'] = np.log(body['goal_lnplus'] + 1)
        body['goal_lnplus'] = str(body['goal_lnplus'])

        body['description'] = body['description'].replace('"','').replace("'",'')
        body['title'] = body['title'].replace('"','').replace("'",'')
        
        url = "https://ussouthcentral.services.azureml.net/workspaces/8c36dc3d420b40ca9c6de09a792a4651/services/a76e767c502d4a82a3d4990b137f66fd/execute?api-version=2.0&details=true"

        payload = "{\r\n  \"Inputs\": {\r\n    \"input1\": {\r\n      \"ColumnNames\": [\r\n        \"title\",\r\n        \"description\",\r\n        \"has_beneficiary\",\r\n        \"location_country\",\r\n        \"is_charity\",\r\n        \"location_state\",\r\n        \"goal_lnplus\",\r\n        \"success_score\"\r\n      ],\r\n      \"Values\": [\r\n        [\r\n          \"" + body['title'] + "\",\r\n          \"" + body['description'] + "\",\r\n          \"" + body['has_beneficiary'] + "\",\r\n          \"" + body['location_country'] + "\",\r\n          \"" + body['is_charity'] + "\",\r\n          \"" + body['location_state'] + "\",\r\n          \"" + body['goal_lnplus'] + "\",\r\n          \"0\"\r\n        ]\r\n      ]\r\n    }\r\n  },\r\n  \"GlobalParameters\": {}\r\n}"
        #payload.encode('utf-8', errors='ignore')
        headers = {
            'Authorization': 'Bearer kEg9TYo1c6jNUXUt7eS7FMIUzIm1Z7Tp4vs68vUFdHpcjF1E68CujSLx6qP5rQGjprCGbNg5ja0WMPe/vw76sQ==',
            'Content-Type': 'application/json',
            # 'Content-Type': 'text/plain'
        }
        payload = payload.encode('utf-8', errors='ignore')
        response = requests.request("POST", url, headers=headers, data = payload)
        
        response = json.loads(response.content)
        print(response)

        try:
            success_score = response["Results"]["output1"]["value"]["Values"][0][0]
        except: 
            success_score = "Error"

        return Response(
            success_score
        )


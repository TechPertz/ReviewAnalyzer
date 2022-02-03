from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .serializers import UserSerializer
from .models import User
import jwt, datetime

from api.scrapper import *
from api.sentiment import *
from api.keywords import *

# Create your views here.

class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data)

class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email = email).first()

        if user is None:
            raise AuthenticationFailed('User not found!')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password!')

        payload = {
            'id' : user.id,
            'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat' : datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256')

        response = Response()

        response.set_cookie(key = 'jwt', value = token, httponly = True)
        response.data = {
            'jwt' : token
        }
        return response

class Scrape(APIView):
    def post(self, request):
        token = request.COOKIES.get('jwt')
        
        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        try:
            payload = jwt.decode(token, 'secret', algorithms=["HS256"])
            print(payload)
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        reviews = []
        tally = [0, 0, 0]
        data = {"Positive": {"names" : [], "ratings" : [], "data": [], "keywords": [], },
                "Neutral": {"names" : [], "ratings" : [], "data": [], "keywords": [], },
                "Negative": {"names" : [], "ratings" : [], "data": [], "keywords": [], }, 
                "tally": [0,0,0], }

        textarea = request.data['link']
        stars = request.data['stars']
        all_data = get_revs(textarea, stars)
        names = all_data[0]
        ratings = all_data[1]
        reviews = all_data[2]

        if len(reviews) != 0:
            for i in range(len(reviews)):
                sentiment = getSentiment(reviews[i])
                if sentiment == "Positive":
                    data["Positive"]["data"].append(reviews[i])
                    data["Positive"]["names"].append(names[i])
                    data["Positive"]["ratings"].append(ratings[i])
                    data["tally"][2] = data["tally"][2]+1
                if sentiment == "Neutral":
                    data["Neutral"]["data"].append(reviews[i])
                    data["Neutral"]["names"].append(names[i])
                    data["Neutral"]["ratings"].append(ratings[i])
                    data["tally"][1] = data["tally"][1]+1
                if sentiment == "Negative":
                    data["Negative"]["data"].append(reviews[i])
                    data["Negative"]["names"].append(names[i])
                    data["Negative"]["ratings"].append(ratings[i])
                    data["tally"][0] = data["tally"][0]+1

            sum = data["tally"][0] + data["tally"][1] + data["tally"][2]
            negative = data["tally"][0]/sum*100
            neutral = data["tally"][1]/sum*100
            positive = data["tally"][2]/sum*100

            data["tally"] = [negative, neutral, positive]

            data["Positive"]["keywords"] = [list(x) for x in get_hotwords(" ".join(data["Positive"]["data"]))]
            data["Neutral"]["keywords"] = [list(x) for x in get_hotwords(" ".join(data["Neutral"]["data"]))]
            data["Negative"]["keywords"] = [list(x) for x in get_hotwords(" ".join(data["Negative"]["data"]))]

            for a in ["Positive", "Neutral", "Negative"]:
                for i in data[a]["keywords"]:
                    i.append([])
                    for j in range(len(data[a]["data"])):
                        if i[0] in data[a]["data"][j].lower():
                            # i[2].append(j)
                            i[2].append({"name" : data[a]["names"][j] , "rating" : data[a]["ratings"][j], "review" : data[a]["data"][j]})


        response = Response()
        response.data = data
        
        return response

class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'success!'
        }
        return response
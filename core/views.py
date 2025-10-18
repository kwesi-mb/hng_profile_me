from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import requests
from datetime import datetime, timezone 

# Create your views here.

@api_view(['GET'])
def get_profile(request):
    CAT_FACT_URL = "https://catfact.ninja/fact"

    # Try fetching a cat fact dynamically
    try:
        response = requests.get(CAT_FACT_URL, timezone=5)
        response.raise_for_status()
        cat_data = response.json()
        cat_fact = cat_data.get("fact", "Cats are fascinating creatures!")
    except:
        cat_fact = "Could not fetch a cat fact at the moment. Please try again later."

    # Build the JSON response
    data = {
        "status": "success",
        "user": {
            "email": "malachymadu09@gmail.com",
            "name": "Malachy Kwesike Madu",
            "stack": "Python/Django"
        },
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "fact": cat_fact 
    }

    return Response(data, status=status.HTTP_200_OK)

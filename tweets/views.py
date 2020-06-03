from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request, *args, **kwargs):
    print(args, kwargs)
    return HttpResponse("<h1>hi hi</h1>")

def tweet_detail_view(request, tweet_id, *args, **kwargs):
    print(args, kwargs)
    return HttpResponse(f"<h1>{tweet_id}</h1>")
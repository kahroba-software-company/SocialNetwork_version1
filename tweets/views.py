import random
from django.conf import settings
from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render, redirect
from django.utils.http import is_safe_url

from .forms import TweetForm
from .models import Tweet

ALLOWED_HOSTS = settings.ALLOWED_HOSTS

# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, "pages/home.html", context={}, status=200)


def tweet_create_view(request, *args, **kwargs):
    # print(abc)#to console the server error

    #to check that the request is ajax or not
    # print("ajax", request.is_ajax())

    form = TweetForm(request.POST or None)
    # print('post data is', request.POST)
    #we have a hidden input , its name is next
    next_url = request.POST.get("next") or None
    # print("next_url", next_url)
    if form.is_valid():
        obj = form.save(commit=False)
        #we can do other form related logic later
        obj.save()
        if request.is_ajax():
            return JsonResponse(obj.serialize(), status=201)#201 == created items
        if next_url != None and is_safe_url(next_url, ALLOWED_HOSTS):
            return redirect(next_url)
        form = TweetForm()
        #clean_data in forms.py mekes errors
    if form.errors:
        if request.is_ajax():
            return JsonResponse(form.errors, status=400)

    return render(request, "components/form.html", context={"form": form})


def tweet_list_view(request, *args, **kwargs):
    """
    REST API VIEW
    Consume by JavaScript or Swift/Java/iOS/Andriod
    return json data
    """
    qs = Tweet.objects.all()
    tweets_list = [x.serialize() for x in qs]
    # tweets_list = [{"id": x.id, "content": x.content, "likes": random.randint(0, 122)} for x in qs]
    data = {
        "isUser": False,
        "response": tweets_list
    }
    return JsonResponse(data)


def tweet_detail_view(request, tweet_id, *args, **kwargs):
    """
    :param request:
    :param tweet_id:
    :param args:
    :param kwargs:
    :return:
    """
    """
    REST API VIEW
    Consume by JavaScript or Swift or Java or ios/Android
    return json data
    """

    # print(args, kwargs)
    data = {
        "id": tweet_id,
        # "content": obj.content,
        # "image_path":obj.image.url
    }
    status = 200
    try:
        obj = Tweet.objects.get(id=tweet_id)
        data['content'] = obj.content
    except:
        data['message'] = "Not Found"
        status = 404

        # raise Http404

    # return HttpResponse(f"<h1> {tweet_id} - {obj.content} </h1>")
    return JsonResponse(data, status=status)  # json.dumps content_type ='application/json'


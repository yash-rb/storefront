from django.shortcuts import render
from store.models import Product
from tags.models import TaggedItem  


def say_hello(request):
    #Querying generic Relationships using contentType
    query_set = TaggedItem.objects.get_tags_for(Product, 1)

    return render(request, 'hello.html', {'name': 'Yash', 'tags':list(query_set)})


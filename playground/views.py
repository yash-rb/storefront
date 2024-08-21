from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from store.models import Product, OrderItem, Order
from tags.models import TaggedItem  


def say_hello(request):
    #Querying generic Relationships using contentType
    
    contentType = ContentType.objects.get_for_model(Product)
    query_set = TaggedItem.objects.\
        select_related('tag')\
            .filter(
                content_type = contentType,
                object_id = 1
            )
    
    
    
    return render(request, 'hello.html', {'name': 'Yash', 'tags':list(query_set)})


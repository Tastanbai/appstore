from goods.models import Products
from django.db.models import Q
from django.contrib.postgres.search import SearchVector

def q_search(query):
    if query.isdigit() and len(query)<=5:
        return Products.objects.filter(id=int(query))
    
    return Products.objects.annotate(search=SearchVector("name", "description")).filter(search=query)
    # keywords=[word for word in query.split() if len(word)>2]

    # q_object=Q()
    # for token in keywords:
    #     q_object |=Q(description__icontains=token)
    #     q_object |=Q(name__icontains=token)

    # return Products.objects.filter(q_object)

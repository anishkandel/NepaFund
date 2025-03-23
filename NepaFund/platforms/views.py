from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger,Paginator
from .models import Platform
from .choices import price_choices, state_choices, status_choices

# Create your views here.
def index(request):
    platforms=Platform.objects.order_by('-invest_date').filter(is_published=True)
# applying pagination
    paginator=Paginator(platforms, 2)
    page=request.GET.get('page')
    paged_platforms=paginator.get_page(page)
    context={
        'platforms':paged_platforms
    }
    return render(request,'platforms/platforms.html', context)
    
def platform(request, platform_id):
    platform = get_object_or_404(Platform, pk=platform_id)
    context={
        'platform':platform
        }
    return render(request,'platforms/platform.html', context)
def search(request):
    queryset_list=Platform.objects.order_by('-invest_date')   

    #keywords search
    if 'keywords' in request.GET:
     keywords = request.GET['keywords']
     if keywords:
         queryset_list=queryset_list.filter(description__icontains=keywords)

    
 #price search
    if 'price' in request.GET:
      price = request.GET['price']
      if price:
         queryset_list=queryset_list.filter(price__exact=price)

#state search
    if 'state' in request.GET:
      state = request.GET['state']
      if state:
         queryset_list=queryset_list.filter(state__exact=state) 
     

    context={
        'state_choices':state_choices,
        'price_choices':price_choices,
        'platforms':queryset_list,
        'values':request.GET
    }
    return render(request,'platforms/search.html',context)

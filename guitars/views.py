from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Guitar, Category

def all_guitars(request):
    """ A view to show all guitars, including sorting and search queries """

    guitars = Guitar.objects.all()
    query = None
    categories = None
    tier = None
    query_tier = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            
            if sortkey == 'name':
                sortkey = 'lower_name'
                guitars = guitars.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            guitars = guitars.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            guitars = guitars.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

            if 'tier' in request.GET:
                query_tier = request.GET['tier']
                tier = guitars.filter(tier__in=query_tier)


        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Provide a guitar brand or model name for me to search for")
                return redirect(reverse('guitars'))
            
            queries = Q(brand__icontains=query) | Q(guitar_model__icontains=query)
            guitars = guitars.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'guitars': guitars,
        'search_term': query,
        'current_categories': categories,
        'tier': query_tier,
        'current_sorting': current_sorting,
    }

    return render(request, 'guitars/guitars.html', context)


def guitar_detail(request, guitar_id):
    """ A view to show guitar details """

    guitar = get_object_or_404(Guitar, pk=guitar_id)

    context = {
        'guitar': guitar,
    }

    return render(request, 'guitars/guitar_detail.html', context)
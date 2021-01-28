from django.shortcuts import render, redirect
from vault.models import Entry
from operator import attrgetter
from vault.views import get_entry_queryset, create_entry_view



def homepage_view(request):
    context = {}
    user = request.user
    if not user.is_authenticated:
        return redirect('welcome')

    # Add entry
    if request.POST:
        form = create_entry_view(request)
        context['form'] = form
        return redirect("home")

    # Search
    query = ""
    if request.GET:
        query = request.GET.get('q', '')
        context['query'] = str(query)
        sorted_qs = sorted(get_entry_queryset(request, query), key=attrgetter('last_edited'), reverse=True)
        context['qs_list'] = sorted_qs
        context['show_add'] = False
        return render(request, 'home.html', context)

    # Entry list
    account = request.user
    qs_list = Entry.objects.filter(user=account)
    sorted_qs = qs_list.order_by('site_name')

    context['qs_list'] = sorted_qs
    context['show_add'] = True
    return render(request, 'home.html', context)


def welcome_page_view(request):
    context = {}
    if request.user.is_authenticated:
        return redirect('home')
    return render(request, 'welcome_page.html', context)
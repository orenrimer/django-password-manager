from django.shortcuts import render, redirect, get_object_or_404
from .forms import EntryUpdateForm, EntryCreateForm
from django.db.models import Q
from accounts.models import Account
from .models import Entry


def get_entry_queryset(request, query=None):
    queryset = []
    queries = query.split(" ")
    user = request.user
    for q in queries:
        posts = Entry.objects.filter(
            Q(site_url__contains=q) |
            Q(site_name__icontains=q) |
            Q(notes__icontains=q)
        ).distinct()
        for post in posts:
            if post.user == user:
                queryset.append(post)

    return list(set(queryset))



def delete_entry_view(request, entry_id):
    user = request.user
    if not user.is_authenticated:
        return redirect('must_authenticate')
    
    if obj.user != user:
        return redirect("home")
    
    obj = get_object_or_404(Entry, id=entry_id)
    obj.delete()
    return redirect("home")


def create_entry_view(request):
    user = request.user
    if not user.is_authenticated:
        return redirect('must_authenticate')

    form = EntryCreateForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        account = Account.objects.filter(email=request.user.email).first()
        obj.user = account
        obj.save()
        
    return form


def update_entry_view(request, entry_id):
    context = {}
    user = request.user
    if not user.is_authenticated:
        return redirect('must_authenticate')


    obj = get_object_or_404(Entry, id=entry_id)
    if obj.user != user:
        return redirect("home")

    form = EntryUpdateForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        context['msg'] = "Entry Updated!"
        form = EntryUpdateForm(initial={
            'email': obj.email,
            'username': obj.username,
            'password': obj.password,
            'site_name': obj.site_name,
            'site_url': obj.site_url,
            'notes':obj.notes,
        })
    form = EntryUpdateForm(initial={
        'email': obj.email,
        'username': obj.username,
        'password': obj.password,
        'site_name': obj.site_name,
        'site_url': obj.site_url,
        'notes': obj.notes,
    })
    context['form'] = form
    return render(request, 'edit_entry.html', context)

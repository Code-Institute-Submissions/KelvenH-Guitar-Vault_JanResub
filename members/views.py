from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import MemberProfile
from .forms import MemberProfileForm
from checkout.models import Order

def profile(request):
    """
    Display user's profile
    """
    profile = get_object_or_404(MemberProfile, user=request.user)
    

    if request.method == 'POST':
        form = MemberProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated')

    form = MemberProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'members/profile.html'
    context = {
        'form': form,
        'orders': orders,
    }

    return render(request, template, context)


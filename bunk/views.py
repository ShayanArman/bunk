from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib.auth.models import User
from .models import Bunk
from .forms import BunkSomeoneForm

# Create your views here.
# <p>{{bunk.from_user.userprofile_set.get().photo.url}}</p>
def bunk_feed(request):
	bunks = Bunk.objects.all().order_by('-bunk_time')
	data = create_user_profiles_dict(bunks, request.user)

	return render(request, 'bunk/main_page.html', {"data":data, "message":"Bunk Feed"})

@login_required
def my_feed(request, user_key):
	try:
		user = User.objects.get(pk=user_key)
		bunks = Bunk.objects.filter(Q(from_user=user) | Q(to_user=user)).order_by('-bunk_time')
		message = user.first_name + "'s Bunk Feed"
		data = create_user_profiles_dict(bunks, request.user)
		return render(request, 'bunk/personal_feed.html', {"data":data, "message":message})
	except:
		return redirect('bunk.views.bunk_feed')

def create_user_profiles_dict(bunks, current_user):
	data = []
	for bunk in bunks:
		ob = {}
		ob['from_user_pk'] = bunk.from_user.pk
		ob['to_user_pk'] = bunk.to_user.pk
		ob['from_username'] = "You" if bunk.from_user == current_user else bunk.from_user.username
		ob['to_username'] = "You" if bunk.to_user == current_user else bunk.to_user.username
		ob['from_user_url'] = "/" + bunk.from_user.userprofile_set.get().photo.url
		ob['to_user_url'] = "/" + bunk.to_user.userprofile_set.get().photo.url
		ob['bunk_time'] = bunk.bunk_time
		data.append(ob)
	return data

def bunk_someone(request):
	if request.method == 'POST':
		form = BunkSomeoneForm(request.POST, request=request)
		if form.is_valid():
			bunk = form.save(commit=False)
			bunk.from_user = request.user
			bunk.save()
			return redirect('bunk.views.my_feed', user_key=request.user.pk)
	else:
		form = BunkSomeoneForm(request.GET, request=request)
	return render(request, 'bunk/bunk_someone.html', {"form":form, "message":"Bunked'->"})
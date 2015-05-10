from django.shortcuts import render

from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from forms import MyRegistrationForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required




from .models import Art
# Create your views here.


def gallery(request):

	language = 'en-gb'
	session_language = 'en-gb'

	if 'lang' in request.COOKIES:
		language = request.COOKIES['lang']

	if 'lang' in request.session:
		language = request.session['lang']

	a = Art.objects.all()
	context = {"a": a, 'language':language, 'session_language': session_language}
	template = "gallery.html"
	return render(request, template, context)


def language(request, language='en-gb'):
	response = HttpResponse("setting language to %s" % language)

	response.set_cookie('lang', language)

	request.session['lang'] = language

	return response 

@login_required
def aboutme(request):

	context = {}
	template = "about.html"
	return render(request, template, context)




# @login_required
def big(request, title):

	a = Art.objects.get(title=title)
	context = {"a":a}
	template = "bigger.html"
	return render(request, template, context)

def artist_view(request, artist):

	a = Art.objects.filter(artist=artist)
	context = {"a":a, 'artist':artist}
	template = "artist.html"
	return render(request, template, context)



def login(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('login.html', c)

def auth_view(request):
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	user = auth.authenticate(username=username, password=password)

	if user is not None:
		auth.login(request, user)
		return HttpResponseRedirect('/') #loggedin
	else:
		return HttpResponseRedirect('invalid')

def loggedin(request):
	return render_to_response('loggedin.html',{"full_name": request.user.username})

def invalid_login(request):
	return render_to_response('invalid_login.html')

def logout(request):
	auth.logout(request)
	return render_to_response('logout.html')


def register_user(request):
	if request.method == 'POST':
		form = MyRegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('register_success')

	args = {}
	args.update(csrf(request))

	args['form'] = MyRegistrationForm()
	return render_to_response('register.html', args)

def register_success(request):
	return render_to_response('register_success.html')


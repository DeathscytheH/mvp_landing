from django.shortcuts import render, render_to_response, RequestContext
from .forms import SingUpForm
# Create your views here.
def home(request):
	form = SingUpForm(request.POST or None)

	if form.is_valid():
		save=form.save(commit=False)
		save.save()	
	return render_to_response("signup.html", locals(), context_instance=RequestContext(request))

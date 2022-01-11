from django.shortcuts import render

# Create your views here.
def get_ip(request):
	x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
	if x_forwarded_for:
		ip = x_forwarded_for.split(',')[0]
	else:
		ip = request.META.get('REMOTE_ADDR')
	return ip

def home(request):
	ctx = {
		'ip': get_ip(request)
	}
	return render(request, 'home.html', ctx)

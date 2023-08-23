from django.contrib import auth
from django.contrib.auth.models import User
from django.http import JsonResponse

from apartment_backend.contacts.models import Contact


def register(request):
    if request.method == 'POST':
        # Get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Check if passwords match
        if password == password2:
            # Check username
            if User.objects.filter(username=username).exists():
                return JsonResponse({'error': 'That username is taken'})
            elif User.objects.filter(email=email).exists():
                return JsonResponse({'error': 'That email is being used'})
            else:
                # Create user
                user = User.objects.create_user(
                    username=username,
                    password=password,
                    email=email,
                    first_name=first_name,
                    last_name=last_name
                )
                user.save()
                return JsonResponse({'success': True, 'message': 'You are now registered and can log in'})
        else:
            return JsonResponse({'error': 'Passwords do not match'})
    else:
        return JsonResponse({'message': 'Account registration failed', 'success': False})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return JsonResponse({'message': 'You are now logged in'})
        else:
            return JsonResponse({'error': 'Invalid credentials'})
    else:
        return JsonResponse({'message': 'Login failed'})

def user_logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return JsonResponse({'message': 'You are now logged out'})

def dashboard(request):
    if request.user.is_authenticated:
        user_contacts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)
        context = {'contacts': user_contacts}
        data = [{'id': contact.id, 'message': contact.message} for contact in user_contacts]
        return JsonResponse(context, safe=False)

    else:
         return JsonResponse({'error': 'Authentication required for dashboard'})

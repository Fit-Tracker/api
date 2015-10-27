# from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth import authenticate, login
# from django.contrib.auth.decorators import login_required
# from django.views.generic import ListView

# Create your views here.


# def register_user(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             user = authenticate(username=user.username,
#                                 password=request.POST['password1'])
#             login(request, user)
#             return redirect('home_page', request.user.username)
#
#     else:
#         form = UserCreationForm()
#     return render(request, 'api/register.html', {'form': form})

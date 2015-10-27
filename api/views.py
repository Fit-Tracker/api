# from django.shortcuts import render
# from django.contrib.auth.forms import UserCreationForm
#
# # Create your views here.
#
#
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

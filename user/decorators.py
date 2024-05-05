from django.shortcuts import redirect

def already_login(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('main:index')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper
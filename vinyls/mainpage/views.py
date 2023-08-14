from django.shortcuts import render
# imported render from django.shortcuts

# Create your views here.
def main(request):
    # created a main function with the request as a parameter
    return render(request, 'main.html')
    # return to render a request of the main html file

def user_info(request):
    # created a user_info function with the request as a parameter
    return render(request, 'user_info.html')
    # return to render a request of the user_info html file
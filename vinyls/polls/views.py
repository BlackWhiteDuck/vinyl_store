from django.shortcuts import render, get_object_or_404
# imported render and get_object_or_404 from django.shortcuts
from django.http import HttpResponse, HttpResponseRedirect
# imported HttpResponse and HttpResponseRedirect from django.http
from .models import Question, Choice
# imported the Question and Choice classes from .models
from django.urls import reverse
# imported reverse from django.urls
from django.contrib.auth.decorators import login_required
# imported login_required from django.contrib.auth.decorators

# Create your views here.
@login_required
# the function will only run if the user is logged in
def index(request):
    # created a index function with the parameter of a request
    recent_question_list = Question.objects.order_by('-date_published')[:5]
    # made a recent_question_list model with the Question class using the objects method and ordered it by -date_published at indexed it 
    # from the first index until the fifth index
    text = {'recent_question_list': recent_question_list}
    # made a text model and made the recent_question_list string equal to the recent_question_list model itself
    return render(request, "poll.html", text)
    # returned render to render the request of the poll.html file and the text model

@login_required
# the function will only run if the user is logged in
def detail(request, question_id):
    # created a detail function with the parameter of a request and the question_id
    question = get_object_or_404(Question, pk=question_id)
    # created a question model using the get_object_or_404 with the Question class and made the question_id the primary key
    return render(request, 'detail.html', {'question': question})
    # returned render to render the request of the detail.html file 
    # made the question string equal to the question model itself

@login_required
# the function will only run if the user is logged in
def results(request, question_id):
    # created a results function with the parameter of a request and the question_id
    question = get_object_or_404(Question, pk=question_id)
    # created a question model using the get_object_or_404 with the Question class and made the question_id the primary key
    return render(request, 'results.html', {'question': question})
    # returned render to render the request of the results.html file 
    # made the question string equal to the question model itself

@login_required
# the function will only run if the user is logged in
def vote(request, question_id):
    # created a vote function with the parameter of a request and the question_id
    question = get_object_or_404(Question, pk=question_id)
    # created a question model using the get_object_or_404 with the Question class and made the question_id the primary key

    try:
        # try statement
        selected_choice = question.choice_set.get(
            # created a selected_choice model using the choice_set method on the 'question'
            pk=request.POST['choice']
            # and using the .get method to make the primary key equal to the request and used the .POST method on the choice
        )

    except (KeyError, Choice.DoesNotExist):
        # except statement with the parameters of a KeyError and when the Choice does not exist
        return render(request, 'detail.html',
                      # returned render to render the request of the detail.html file 
                      {'question': question,'error_message':"You did not select a choice."})
                        # and render the request of the question string being equal to the actul question string and the error message 
                        # being equal to an error message string

    else:
        # else statement
        selected_choice.votes += 1
        # the selected choice votes will increment by 1 if the else statement runs
        selected_choice.save()
        # and will also save using the .save() method
        return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))
        # returned the HttpResponseRedirect with the reverse function to show the results and made the args equal to the question_id

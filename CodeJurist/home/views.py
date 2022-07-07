from django.shortcuts import render
from problem.models import Problem


def problems(request):
    context = {
        'problems': Problem.objects.all(),
    }
    return render(request, 'problems.html', context)

    # End of Views
from django.shortcuts import render
from SearchResult.models import Person

def menu(request):
    all_Person = Person.objects.all()
    persons = {}
    for i in all_Person:
        persons[str(i.id)] = i.full_name
    persons = dict(sorted(persons.items(), key=lambda item: item[1]))
    print(persons)
    return render(request, "page2.html", context={"persons": persons})

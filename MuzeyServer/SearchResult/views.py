from django.shortcuts import render
from .models import Person

def result(request, ids):
    es_Person = Person.objects.all()
    for i in es_Person:
        if i.id == ids:
            es_Person = i
    rest = {}
    rest["name"] = es_Person.full_name
    rest["biography"] = es_Person.biography
    if es_Person.image1:
        rest['image1'] = es_Person.image1.name
    else:
        rest['image1'] = "static/assets/images/Изображение отсутствует.png"
    if es_Person.image2:
        rest['image2'] = es_Person.image2.name
    else:
        rest['image2'] = "static/assets/images/Изображение отсутствует.png"
    if es_Person.image3:
        rest['image3'] = es_Person.image3.name
    else:
        rest['image3'] = "static/assets/images/Изображение отсутствует.png"
    if es_Person.image4:
        rest['image4'] = es_Person.image4.name
    else:
        rest['image4'] = "static/assets/images/Изображение отсутствует.png"
    if es_Person.image5:
        rest['image5'] = es_Person.image5.name
    else:
        rest['image5'] = "static/assets/images/Изображение отсутствует.png"
    return render(request, "page1.html", context=rest)
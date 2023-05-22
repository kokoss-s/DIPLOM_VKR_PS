from django.shortcuts import render, get_object_or_404
from .models import Fire, Calculate
from .forms import FireForm


PI = 3.14

CHOICE_RESULT = {
    1: 'Административное здание',
    2: 'Больница или школа',
    3: 'Библиотека или торговое предприятие',
    4: 'Склад льноволокна',
    5: 'Склад текстильных изделий',
    6: 'Склад резинотехнических изделий',
    7: 'Склад леса в штабелях',
    8: 'Склад пиломатериалов',
    9: 'Типография',
    10: 'Ремонтный зал ангара',
}

CHOICE_VALUES = {
    1: 1.2,
    2: 2.5,
    3: 0.9,
    4: 4,
    5: 0.4,
    6: 1.5,
    7: 0.7,
    8: 2.3,
    9: 0.7,
    10: 1.3,
    }


def fire_form(request, pk=None, ):
    if pk is not None:
        instance = get_object_or_404(Fire, pk=pk)
    else:
        instance = None
    form = FireForm(request.POST or None, instance=instance)
    context = {'form': form}
    if form.is_valid():
        first_mod = form.save()

        choice1_value = CHOICE_VALUES[first_mod.object_type]
        var1 = first_mod.time
        var2 = first_mod.corner
        object_type = CHOICE_RESULT[first_mod.object_type]
        name = first_mod.name
        time = first_mod.time
        corner = first_mod.corner
        description = first_mod.description

        if var2 < 1:
            squere_first_ten = round(PI * ((0.5 * choice1_value * 10)**2))
            squere = round(PI * ((choice1_value * (var1-10))**2))
            perimeter = round(2 * PI * choice1_value * var1)
            front = perimeter
            speed_of_squere = round(PI * (choice1_value)**2 * var1)
            line_speed = round(choice1_value)
            front_speed = round(2 * PI * choice1_value)
        else:
            squere_first_ten = round(0.5 * PI * ((0.5 * choice1_value * 10)**2))
            squere = round(0.5 * PI * ((choice1_value * (var1-10))**2))
            perimeter = round(choice1_value * var1 * (2 + var2))
            front = round(var2 * choice1_value * var1)
            speed_of_squere = round(0.5 * var2 * (choice1_value)**2 * var1)
            line_speed = round(choice1_value)
            front_speed = round(2 * var2 * choice1_value)

        Calculate.objects.create(
            squere_first_ten=squere_first_ten,
            squere=squere,
            perimeter=perimeter,
            front=front,
            speed_of_squere=speed_of_squere,
            line_speed=line_speed,
            front_speed=front_speed,
            object_type=object_type,
            name=name,
            time=time,
            corner=corner,
            description=description,
        )

    return render(request, 'fire/fire_form.html', context)


def fire_list(request):
    fires = Fire.objects.all()
    calculations = Calculate.objects.all()
    context = {
        'fires': fires,
        'calculations': calculations,
        }
    return render(request, 'fire/fire_list.html', context)

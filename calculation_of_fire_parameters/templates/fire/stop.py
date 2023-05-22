def fire_list(request):

    fires = Fire.objects.all()

    for fire in fires:
        if fire.corner < 1:
            objectP = CHOICE_RESULT[fire.object_type]
            choice1_value = CHOICE_VALUES[fire.object_type]
            var1 = fire.time
            squere_first_ten = round(PI * ((0.5 * choice1_value * 10)**2))
            squere = (round(PI * ((choice1_value * (fire.time-10))**2))) + squere_first_ten
            perimeter = round(2 * PI * choice1_value * var1)
            front = perimeter
            speed_of_squere = round(PI * (choice1_value)**2 * var1)
            line_speed = round(choice1_value)
            front_speed = round(2 * PI * choice1_value)
        else:
            choice1_value = CHOICE_VALUES[fire.object_type]
            var1 = fire.time
            var2 = fire.corner/57
            squere_first_ten = round(0.5 * PI * ((0.5 * choice1_value * 10)**2))
            squere = round(0.5 * PI * ((choice1_value * (var1-10))**2))
            perimeter = round(choice1_value * var1 * (2 + var2))
            front = round(var2 * choice1_value * var1)
            speed_of_squere = round(0.5 * var2 * (choice1_value)**2 * var1)
            line_speed = round(choice1_value)
            front_speed = round(2 * var2 * choice1_value)

    context = {
        'fires': fires,
        'squere_first_ten': squere_first_ten,
        'squere': squere,
        'perimeter': perimeter,
        'front': front,
        'speed_of_squere': speed_of_squere,
        'line_speed': line_speed,
        'front_speed': front_speed,
        'objectP': objectP,
        }

    return render(request, 'fire/fire_list.html', context)



    #squere = models.FloatField()
    #perimeter = models.FloatField()
    #front = models.FloatField()
    #speed_of_squere = models.FloatField()
    #line_speed = models.FloatField()
    #front_speed = models.FloatField()



    <p> Площадь пожара за 10 минут: {{ squere_first_ten }} м2</p>
    <p> Площадь пожара за все время: {{ squere }} м2</p>
    <p> Периметр пожара за все время: {{ perimeter }} м</p>
    <p> Фронт пожара за все время: {{ front }} м</p>
    <p> Скорость роста площади пожара: {{ speed_of_squere }} м2 в минуту</p>
    <p> Линейная скорость роста периметра пожара: {{ line_speed }} м в минуту</p>
    <p> Скорость роста фронта пожара: {{ front_speed }} м в минуту</p>


    class Calculate(models.Model):
    squere_first_ten = models.FloatField('Площадь пожара за первые 10 минут')
    squere = models.FloatField('Площадь пожара')
    perimeter = models.FloatField('Периметр пожара')
    front = models.FloatField('Фронт пожара')
    speed_of_squere = models.FloatField('Скорость роста площади пожара')
    line_speed = models.FloatField('Линейная скорость роста пожара')
    front_speed = models.FloatField('Скорость роста фронта пожара')

    class Meta:
        verbose_name = _("Параметры пожара")
        verbose_name_plural = _("Параметры пожара")
        db_table = 'firescalc'
#5 ejercicio
import calendar
domingo = calendar.monthcalendar(2023, 3)

# imprimir las semanas que empiezan en domingo
for domingo in domingo:
    if domingo[0] == 6:
        print(domingo)
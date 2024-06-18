class WeekDayError(Exception):
    pass
	

class Weeker:
    #
    # Escribir código aquí.
    #

    def __init__(self, day):
        #
        # Escribir código aquí.
        #

    def __str__(self):
        #
        # Escribir código aquí.
        #

    def add_days(self, n):
        #
        # Escribir código aquí.
        #

    def subtract_days(self, n):
        #
        # Escribir código aquí.
        #


try:
    weekday = Weeker('Lun')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Lunes')
except WeekDayError:
    print("Lo siento, no puedo atender tu solicitud.")
    
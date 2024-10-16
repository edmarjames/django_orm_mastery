from django.db import models

# Create your models here.
class Person(models.Model):

    # RED = 'RD'
    # BLUE = 'BL'

    # FAV_COLOR = [
    #     (RED, 'red'),
    #     (BLUE, 'blue')
    # ]

    # to create a Person object via shell, you can access the constants inside this class.
    # Example: Person.objects.create(name='test', color=Person.BLUE)

    # -------------------------------------------------------------------------
    # Alternative approach
    class Colours(models.TextChoices):
        RED = 'RD', 'Red'
        BLUE = 'BL', 'Blue'

    name = models.CharField(max_length=50)
    color = models.CharField(max_length=50, choices=Colours.choices)

    def __str__(self):
        return f"{self.name} - {self.color}"

    # to create a Person object via shell, you can access the constants inside the Colours class.
    # Example: Person.objects.create(name='test', color=Person.Colours.BLUE)
from django.db import models

# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=200)
    #user = models.user()
    create_date = models.DateTimeField('date published')
    description = models.CharField(max_length=5000)

class Tag(models.Model):
	title = models.CharField(max_length=64)
	#tagtype = 

class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe)
    recipe_text = models.CharField(max_length=5000)
    step_num = models.IntegerField(default=0)
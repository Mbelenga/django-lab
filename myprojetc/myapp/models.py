from django.db import models

# Create your models here.
# Here we also create our databases
# Models are also used in configuring our databases
class Feature:
    id: int
    name: str
    details: str
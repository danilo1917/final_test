from django.db import models

# Create your models here.


class Consumer(models.Model):
    name = models.CharField("Nome do Consumidor", max_length=128)
    document = models.CharField("Documento(CPF/CNPJ)", max_length=14, unique=True)
    city = models.CharField("Cidade", max_length=128)
    state = models.CharField("Estado", max_length=128)
    consumption = models.IntegerField("Consumo(kWh)")
    #  create the foreign key for discount rule model here


# TODO: Create the model DiscountRules below
"""Fields:
-> Consumer type  
-> Consumption range
-> Cover
-> discount value
The first three fields should be a select with the values provided in the table
defined in the readme of the repository. Discount should be numerical
"""
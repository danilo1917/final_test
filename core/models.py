from django.db import models

# Create your models here.
class DiscountRules(models.Model):
    CONSUMIDOR_CHOICES = (("I","Industrial"), ("R","Residencial"), ("C","Comercial"))
    CONSUMO_CHOICES = ("<10000",">10000<20000",">20000")
    COVERAGE_CHOICES = (0.9, 0.95,0.99)

    consumidor = models.CharField(max_length = 50)
    consumo = models.CharField(max_length = 70)
    coverage = models.FloatField()
    discount = models.FloatField(blank = True)
    def __str__(self):
        return f"{self.consumidor} {self.consumo} {self.coverage}"

class Consumer(models.Model):
    name = models.CharField("Nome do Consumidor", max_length=128)
    document = models.CharField("Documento(CPF/CNPJ)", max_length=14, unique=True)
    city = models.CharField("Cidade", max_length=128)
    state = models.CharField("Estado", max_length=128)
    consumption = models.IntegerField("Consumo(kWh)", blank=True, null=True)
    distributor_tax = models.FloatField("Tarifa da Distribuidora", blank=True, null=True)
    discount_rules_key = models.ForeignKey(DiscountRules, on_delete=models.CASCADE)
    #  create the foreign key for discount rule model here

    def __str__(self):
        return self.name

# TODO: Create the model DiscountRules below
"""Fields:
-> Consumer type  
-> Consumption range
-> Cover value
-> Discount value
The first three fields should be a select with the values provided in the table
defined in the readme of the repository. Discount should be numerical
"""


# TODO: You must populate the consumer table with the data provided in a sheet
#  and associate each one with the correct discount rule

from django.shortcuts import render
from .models import Consumer, DiscountRules
# Create your views here.
# Todo: Your view should do the follow tasks
"""
-> Recover all consumers from the database
-> Get the discount value for each consumer
-> Calculate the economy
-> Send the data to the template that will be rendered
"""


def view1(request):
	consumidores = Consumer.objects.all().values()
	consumidores_list = []
	for cons in consumidores:
		
		print("Cons id", cons["id"])
		regra = DiscountRules.objects.all().filter(id=cons["discount_rules_key_id"]).values()
		regra = regra[0]
		cons["desconto"] = cons["consumption"]*regra["coverage"]*cons["distributor_tax"]*regra["discount"]
		cons["economia_anual"] = cons["desconto"]*12
		cons["tipo_consumidor"] = regra["consumidor"]
		cons["cobertura"] = regra["coverage"]
		cons["range_consumo"] = regra["consumo"]
		consumidores_list.append(cons)
	contexto = {"consumidores":consumidores_list}
	return render(request, "index.html", context = contexto)

# TODO: The follow task is optional but if performed, will be used in assessment
""" Create a view to perform inclusion of consumers. The view should do:
-> Receive a POST request with the data to register
-> Create and save a new Consumer object associated with the right discount rule object
-> Redirect to the template the list all consumers

Your view must be associated with an url and a template different from the first one. A link to
this page must be provided in the main page.
"""


def view2():
    # Create the optional view here.
    pass

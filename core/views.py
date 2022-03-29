from django.shortcuts import render

# Create your views here.
# Todo: Your view should do the follow tasks
"""
-> Recover all consumers from the database
-> Get the discount value for each consumer
-> Calculate the economy
-> Send the data to the template that will be rendered
"""


def view1():
    # Create the first view here.
    pass


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

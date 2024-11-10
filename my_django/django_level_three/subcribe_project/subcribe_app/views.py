from django.shortcuts import render
from subcribe_app.models import Customer
from subcribe_app.forms import NewSubcriber

# Create your views here.
def index(request):
    return render(request,'subcribe_app/index.html')

def customers(request):
    customer_list = Customer.objects.order_by('first_name')
    customer_dict = {'customers':customer_list}
    return render(request, 'subcribe_app/customers.html', context=customer_dict)

def subcribe(request):
    form = NewSubcriber()

    if request.method == "POST":
        form = NewSubcriber(request.POST)

        form.is_valid()
        form.save(commit=True)
        return customers(request)
    else:
        print("Error: Form invalid")

    return render (request, 'subcribe_app/subcribe.html', {'form':form})
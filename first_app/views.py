from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ClientForm
from .models import Client


@login_required
def home(request):
    return render(request, "home.html", {})


@login_required
def list_client(rq):
    scl = rq.GET.get("search_cli")
    if scl != "" and scl != None:
        clients = Client.objects.filter(client_name__icontains=scl)
    else:
        clients = Client.objects.all()
    context = {}
    context["item_list"] = clients
    return render(rq, "list.html", context)


@login_required
def detail(req, id):
    client = Client.objects.get(client_id=id)
    return render(req, "detail.html", {"item": client})


@login_required
def delete(req, id):
    obj = Client.objects.get(client_id=id)
    if req.method == "POST":
        obj.delete()
        messages.info(req, "Client deleted!")
        return redirect("list_client")
    return render(req, "./delete.html", {})


@login_required
def addClient(req):
    form = ClientForm(req.POST or None, req.FILES or None)
    if form.is_valid():
        form.save()
        # cli = form.cleaned_data.get("client_name")
        # try:
        # data = get_object_or_404(Client, client_name=cli)
        messages.success(req, "Client created!")
        return redirect("list_client")
        # except:
        #     messages.error(req, "Client already exists!")
        #     form = ClientForm()
    else:
        form = ClientForm()
    return render(req, "./add.html", {"form": form})


@login_required
def contact(req):
    return render(req, "./contact.html", {})


@login_required
def products(req):
    return render(req, "./products.html", {})


@login_required
def update(req, id):
    client = Client.objects.get(client_id=id)
    form = ClientForm(req.POST, instance=client)
    if form.is_valid():
        messages.success(req, "Client updated!")
        return redirect("list_client")
    return render(req, "./update.html", {"form": form})


def test(req):
    return render(req, "./test.html", {})

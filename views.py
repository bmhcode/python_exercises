def checkout(request):
    if request == "POST":
        items = request.POST.get('items')
        nom = request.POST.get('nom')
        email = request.POST.get('email')
        address = request.POST.get('address')
        ville = request.POST.get('ville')
        pays = request.POST.get('pays')
        zipcode = request.POST.get('zipcode')
        com = Commande(items=items,nom=nom,email=email,
                       address=address,ville=ville,
                       pays=pays,zipcode=zipcode)
        com.save()
    
    return render(request, 'shop/checkout.html')

        
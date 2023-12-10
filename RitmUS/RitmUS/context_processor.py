from base.models import Cart

def cart(request):
    playlists = []
    playlist_number = 0
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user).first()
        if cart:
            playlists = list(cart.products.all())
            playlist_number = len(playlists)
        else:
            Cart.objects.create(user=request.user)

    return {'cart_playlists': playlists, 'cart_playlist_number': playlist_number}
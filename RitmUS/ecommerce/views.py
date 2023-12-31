from django.shortcuts import render
from .forms import CreateRatingForm, EditRatingForm
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from base.models import Playlist, User, Song, Rating,Cart,Order,Subscription
from django.contrib import messages
import stripe
from django.conf import settings
from django.db.models import Q
from datetime import datetime
from django.utils import timezone
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.core.files.storage import default_storage
from django.core.mail import EmailMultiAlternatives
import os

def home(request):
    playlists = Playlist.objects.all()
    data = {'playlists': playlists}
    return render(request, 'home.html', data)


@login_required
def playlist_detail(request, pk):
    playlist = Playlist.objects.get(pk=pk)
    songs = Song.objects.filter(playlist=playlist)
    ratings = Rating.objects.filter(playlist=playlist)
    user = request.user
    ratingUser = Rating.objects.filter(playlist=playlist, user=user)
    averageRating = 0
    if ratings.count() > 0:
        for rating in ratings:
            averageRating += rating.score
        averageRating /= ratings.count()
        averageRating = round(averageRating, 2) 
    stars=[2,4,6,8,10]
    users = ratings.count()
    inCart = Cart.objects.filter(user=user, products__id=playlist.id).exists()
    suscription = Subscription.objects.filter(playlist=playlist, order__user=user, end_date__gte=timezone.now()).exists()
    
    data = {'playlist': playlist, 'songs': songs, 'averageRating': averageRating, "doubleRating": averageRating*2,
             'users': users, 'ratings': ratings, 'stars': stars, 'ratingUser': ratingUser, 
             "hasSuscription": suscription, "cart": inCart}

    return render(request, 'playlist_details.html', data)

@login_required
def create_rating(request, pk):
    playlist = Playlist.objects.get(pk=pk)
    if Rating.objects.filter(playlist=playlist, user=request.user).exists():
        messages.error(request, 'Ya has creado una reseña para esta playlist')
        return redirect(to='playlist_detail', pk=pk)
    else:
        data = {
            'playlist': playlist,
            'form': CreateRatingForm(initial={'user': request.user, 'playlist': playlist})
        }

        if request.method == 'POST':
            form = CreateRatingForm(data=request.POST)
            if form.is_valid():
                rating = form.save(commit=False)
                rating.user = request.user
                rating.playlist = playlist
                rating.save()
                form.save()
                messages.success(request, 'Reseña creada correctamente')
                return redirect(to='playlist_detail', pk=pk)
            else:
                data['form'] = form

        return render(request, 'ratings/createrating.html', data)

@login_required
def edit_rating(request, pk):
    playlist = Playlist.objects.get(pk=pk)
    rating = Rating.objects.get(playlist=playlist, user=request.user)
    data = {
        'playlist': playlist,
        'form': EditRatingForm(initial={'user': request.user, 'playlist': playlist, 'score': rating.score, 'description': rating.description})
    }
    if request.method == 'POST':
        form = EditRatingForm(data=request.POST)
        if form.is_valid():
            rating.delete()
            rating = form.save(commit=False)
            rating.user = request.user
            rating.playlist = playlist
            rating.save()
            form.save()
            messages.success(request, 'Reseña editada correctamente')
            return redirect(to='playlist_detail', pk=pk)
        else:
            data['form'] = form

    return render(request, 'ratings/editrating.html', data)

@login_required
def delete_rating(request, pk):
    playlist = Playlist.objects.get(pk=pk)
    rating = Rating.objects.get(playlist=playlist, user=request.user)
    rating.delete()
    messages.success(request, 'Reseña eliminada correctamente')
    return redirect(to='playlist_detail', pk=pk)

def playlist_search(request):
    query=get_queryset(request)
    data = {'playlists': query}
    return render(request, 'home.html', data)

def get_queryset(request):
        queryset = request.GET.get("search","")
        price_range = request.GET.get('price_range', '')
        queryset2 = Playlist.objects.filter(name__icontains=queryset)
        queryset2 |= Playlist.objects.filter(genre__icontains=queryset)
        if price_range:
            min_price, max_price = map(int, price_range.split('-'))
            queryset2 &= Playlist.objects.filter(price__gte=min_price, price__lte=max_price)
        return queryset2

@login_required
def add_to_cart(request, pk):
    playlist = Playlist.objects.get(pk=pk)
    user = request.user
    cart = Cart.objects.filter(user=user).first() 
    if not cart:
        cart = Cart.objects.create(user=user)
    cart.products.add(playlist)  
    cart.save()
    messages.success(request, 'Playlist añadida al carrito correctamente')
    return redirect(to='playlist_detail', pk=pk)

@login_required
def cart(request):
    user = request.user
    cart = Cart.objects.filter(user=user).first()
    playlists= None
    if cart:
        playlists = list(cart.products.all())
    else:
        cart = Cart.objects.create(user=user)
    total = 0
    if playlists:
        for playlist in playlists:
            total += playlist.price
    data = {'playlists': playlists, 'total': total}
    return render(request, 'cart.html', data)

@login_required
def remove_from_cart(request, pk):
    playlist = Playlist.objects.get(pk=pk)
    user = request.user
    cart = Cart.objects.filter(user=user).first()
    cart.products.remove(playlist)
    cart.save()
    messages.success(request, 'Playlist eliminada del carrito correctamente')
    return redirect(to='cart')

@login_required
def empty_cart(request):
    user = request.user
    cart = Cart.objects.filter(user=user).first()
    cart.products.clear()
    cart.save()
    messages.success(request, 'Carrito vaciado correctamente')
    return redirect(to='cart')

@login_required
def checkout(request):
    user = request.user
    cart = Cart.objects.filter(user=user).first()
    playlists = list(cart.products.all())
    total = 0
    if playlists:
        for playlist in playlists:
            total += playlist.price
    stripe_total = int(total*100)
    stripe_key=settings.STRIPE_API_KEY
    data = {'playlists': playlists, 'total': total,'stripe_key': stripe_key,'stripe_total': stripe_total}
    
    if request.method == 'GET':
        return render(request, 'checkout.html', data)
    
    if request.method == 'POST':
        stripe.api_key = settings.STRIPE_SECRET_KEY
        token = request.POST.get('stripeToken')
        try:
            
            charge = stripe.Charge.create(
                amount=stripe_total,  
                currency='eur',
                source=token,
            )
            
            order = Order.objects.create(user=user)            
            for playlist in playlists:
                Subscription.objects.create(playlist=playlist, order=order, price=playlist.price)
            cart.products.clear()
            cart.save()

            cuerpo = purchase_email(order) 
            email = EmailMultiAlternatives(subject="Tu compra en RitmUS", body=cuerpo, from_email=settings.EMAIL_HOST_USER, to=[order.user.email])
            email=attach_images(email,order)
            email.fail_silently=False
            email.content_subtype = "html"
            email.send()

            # mensaje = purchase_email(order)
            # server = smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT)
            # server.starttls()
            # server.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
            # server.sendmail(settings.EMAIL_HOST_USER, order.user.email, mensaje.as_string())
            # server.quit()

            return redirect(to="/checkout/completed?success=true")

        except stripe.error.CardError as e:
             return redirect(to="/checkout/completed?success=false")
        
    return redirect(to="/checkout/completed?success=false")
    
def purchase_email(order):
    products = Subscription.objects.filter(order=order)

    cuerpo = f'''<p>Gracias por tu compra en RitmUS.</p>
        <p>Esta es tu factura:</p><br>
        <p>Id de compra: {order.id}</p>
        <p>Fecha de compra: {datetime.strftime(order.purchase_date, "%d/%m/%Y a las %H:%M")}</p>
        <p>Productos:</p>'''
    for product in products:
        cuerpo += f'''
        <div style="display: flex; align-items: center; padding:20px; margin:20px; padding-bottom:30px; background-color:black; color:white;">
            <img src="cid:{product.playlist.id}" alt="Playlist Image" width="100" height="100" style="display: inline-block; margin:10px;">
            <div>
                <p style="margin:10px;">Playlist: {product.playlist.name}</p>
                <p style="margin:10px;">Precio: {str(product.price)}€</p>
            </div>
        </div>
        '''

    cuerpo +=f'''<p>Total: {str(order.total_amount())}€</p><br>
    <p>Gracias por confiar en nosotros.</p> <br>
    <p>El equipo de RitmUS</p>'''
    return cuerpo
    
def attach_images(mensaje,order):
    products = Subscription.objects.filter(order=order)
    for product in products:
        image_path = os.path.join(settings.BASE_DIR, "photos" ,product.playlist.image.name)
        with default_storage.open(product.playlist.image.name, 'rb') as image_file:
            image_data = image_file.read()
        mensaje_image = MIMEImage(image_data)
        image_file.close()
        mensaje_image.add_header('Content-ID', f'<{product.playlist.id}>')
        mensaje.attach(mensaje_image)
    return mensaje

@login_required
def checkout_completed(request):    
    return render(request, 'checkout_complete.html', {'success': request.GET.get('success', False)})

@login_required
def get_all_sales(request):

    orders = Order.objects.all()
    subs_sale = []

    if not request.user.is_superuser:
        subs_sale = [(order, order.total_amount(), Subscription.objects.filter(order=order, order__user=request.user)) for order in orders]
        subs_sale = [x for x in subs_sale if x[2].count() > 0]            
    else:         
        subs_sale = [(order, order.total_amount(), Subscription.objects.filter(order=order)) for order in orders]   

    return render(request, 'sales.html', {'subs_sale': subs_sale, 'admin': request.user.is_superuser})
    
@login_required
def sales_search(request):
    
    query = get_sales_queryset(request)
    return render(request, 'sales.html', {'subs_sale': query, 'admin': request.user.is_superuser})

@login_required
def get_sales_queryset(request):

    orders = []
    res = Q()

    queryset = request.GET.get("search","")
    start_date = request.GET.get("start_date","")
    end_date = request.GET.get("end_date","")

    if request.user.is_superuser: 
        if queryset != "":
            orders = Order.objects.filter(user__username__icontains=queryset)
        else:
            orders = Order.objects.all()
    else:
        orders = Order.objects.filter(user=request.user)

    if start_date != "":
        start_date = start_date + " 00:00:00"
        formatted_start_date = datetime.strptime(start_date, "%Y-%m-%d %H:%M:%S") 
        res &= Q(purchase_date__gte=formatted_start_date)

    if end_date != "":
        end_date = end_date + " 23:59:59"
        formatted_end_date = datetime.strptime(end_date, "%Y-%m-%d %H:%M:%S")
        res &= Q(purchase_date__lte=formatted_end_date)

    result_set = [(order, order.total_amount(), Subscription.objects.filter(order=order)) for order in orders.filter(res)]

    return result_set



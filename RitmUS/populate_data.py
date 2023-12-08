import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'RitmUS.settings')

import django
django.setup()

from base.models import Playlist, Song, Order, Subscription
from customuser.models import CustomUser

def populate():

    playlists = [
        {'name': 'Metálico', 'description': 'Los éxitos del metal', 'price': 10, 'image': 'static/img/GenerosRock.png', 'genre': 'Rock', 'is_active': True},
        {'name': 'Like BlackPink', 'description': 'Los éxitos del KPOP más recientes', 'price': 20, 'image': 'static/img/GenerosKPOP.png', 'genre': 'KPOP', 'is_active': True},
        {'name': 'DellaBanco', 'description': 'Los éxitos de DellaBanco', 'price': 15, 'image': 'static/img/GenerosTrap.png', 'genre': 'Trap', 'is_active': True},
        {'name': 'MerengueLatino', 'description': 'Los éxitos del merengue latino', 'price': 12, 'image': 'static/img/Merengue.png', 'genre': 'Merengue', 'is_active': True},
    ]

    if Playlist.objects.all().count() > 0:
        for playlist_data in Playlist.objects.all():
            playlist_data.delete()

    for playlist_data in playlists:
        Playlist.objects.create(**playlist_data)

    songs = [
        {'title': 'Undefeatable', 'artist': 'Sega Sound Team', 'genre': 'Rock', 'album': 'Sonic Frontiers','duration': 5 ,'image': 'static/img/Sonic.png', 'release_date': '2021-05-01', 'file_url': 'https://www.youtube.com/watch?v=3NoKAOTE_ZI&ab_channel=SonictheHedgehog', 'playlist': Playlist.objects.get(name='Metálico')},
        {'title': 'Can´t Hold Me Now', 'artist': 'Criz', 'genre': 'Rock', 'album': 'Borderlands 3:Original Soundtrack','duration': 4 ,'image': 'static/img/Borderlands3.png', 'release_date': '2021-05-01', 'file_url': 'https://www.youtube.com/watch?v=PhXe6OD32g0&ab_channel=GeekMusic-Topic', 'playlist': Playlist.objects.get(name='Metálico')},
        {'title': 'Pink Venom', 'artist': 'Blackpink', 'genre': 'KPOP', 'album': 'BORN PINK','duration': 3 ,'image': 'static/img/PinkVenom.png', 'release_date': '2021-05-01', 'file_url': 'https://www.youtube.com/watch?v=3NoKAOTE_ZI&ab_channel=SonictheHedgehog', 'playlist': Playlist.objects.get(name='Like BlackPink')},
        {'title': 'How You Like That', 'artist': 'Blackpink', 'genre': 'KPOP', 'album': 'THE ALBUM','duration': 3 ,'image': 'static/img/HowYouLikeThat.png', 'release_date': '2021-05-01', 'file_url': 'https://www.youtube.com/watch?v=3NoKAOTE_ZI&ab_channel=SonictheHedgehog', 'playlist': Playlist.objects.get(name='Like BlackPink')},
        {'title': 'K Animal', 'artist': 'DELLAFUENTE, Morad', 'genre': 'Trap', 'album': 'ZIZOU','duration': 3 ,'image': 'static/img/KANIMAL.png', 'release_date': '2021-05-01', 'file_url': 'https://www.youtube.com/watch?v=uUfmk9zp9mk&ab_channel=DELLAFUENTE', 'playlist': Playlist.objects.get(name='DellaBanco')},
        {'title': 'Me Pelea', 'artist': 'DELLAFUENTE', 'genre': 'Trap', 'album': 'Sencillo','duration': 3 ,'image': 'static/img/MePelea.png', 'release_date': '2021-05-01', 'file_url': 'https://www.youtube.com/watch?v=stC_LSekh4w&ab_channel=DellafuenteVEVO', 'playlist': Playlist.objects.get(name='DellaBanco')},
        {'title': 'Tú Eres Ajena', 'artist': 'Eddy Herrera', 'genre': 'Merengue', 'album': 'Atrevido','duration': 5 ,'image': 'static/img/Ajena.png', 'release_date': '2021-05-01', 'file_url': 'https://www.youtube.com/watch?v=L_M8XP0nVFM&ab_channel=ForYourRelaxOnly', 'playlist': Playlist.objects.get(name='MerengueLatino')},
        {'title': 'El Tamarindo', 'artist': 'Kinito Mendez', 'genre': 'Merengue', 'album': 'Los éxitos de Kinito Mendez','duration': 5 ,'image': 'static/img/Tamarindo.png', 'release_date': '2021-05-01', 'file_url': 'https://www.youtube.com/watch?v=UEY7bagwQbU&ab_channel=carlitoswey', 'playlist': Playlist.objects.get(name='MerengueLatino')},    
    ]

    if Song.objects.all().count() > 0:
        for song_data in Song.objects.all():
            song_data.delete()
    for song_data in songs:
        Song.objects.create(**song_data)

    users = [
        {'username': 'admin', 'password': 'pbkdf2_sha256$600000$ZjkcpGFL7xqTT8if75ALyw$rCbw3blhbgKRswz7vjpKL8m5a+ZWpISLzZA6nV3QqeY=', 'email': 'admin@gmail.com' ,'first_name': 'contraseña admin', 'last_name': 'admin', 'is_active': True, 'is_staff': True, 'is_superuser': True},
        {'username': 'usuario1', 'password': 'pbkdf2_sha256$600000$JDgXFkQAApjXfqfL9xLkHB$Pk9Z+xIoJ7tcIWaWDq+1OpPAaMEfkIPaxejwi02QgOQ=', 'email': 'usuario1@gmail.com' ,'first_name': 'contraseña nabo2002', 'last_name': 'usuario1', 'is_active': True, 'is_staff': False, 'is_superuser': False},
        {'username': 'usuario2', 'password': 'pbkdf2_sha256$600000$JDgXFkQAApjXfqfL9xLkHB$Pk9Z+xIoJ7tcIWaWDq+1OpPAaMEfkIPaxejwi02QgOQ=', 'email': 'usuario2@gmail.com' ,'first_name': 'contraseña nabo2002', 'last_name': 'usuario2', 'is_active': True, 'is_staff': False, 'is_superuser': False},
    ]

    if CustomUser.objects.all().count() > 0:
        for user_data in CustomUser.objects.all():
            user_data.delete()
    for user_data in users:
        CustomUser.objects.create(**user_data)

    orders = [
        {'user': CustomUser.objects.get(username='usuario1'), 'purchase_date': '2023-11-01 00:00:00'},
        {'user': CustomUser.objects.get(username='usuario1'), 'purchase_date': '2023-12-04 17:50:01'},
        {'user': CustomUser.objects.get(username='usuario1'), 'purchase_date': '2023-12-06 11:00:00'},
        {'user': CustomUser.objects.get(username='usuario2'), 'purchase_date': '2023-12-07 23:59:00'},
    ]

    if Order.objects.all().count() > 0:
        for order_data in Order.objects.all():
            order_data.delete()
    for order_data in orders:
        Order.objects.create(**order_data)

    subscriptions = [
        {'init_date': '2023-11-01 00:00:00', 'end_date': '2023-11-30 00:00:00', 'price': 10, 'is_favourite': False, 'playlist': Playlist.objects.get(name='Metálico'), 'order': Order.objects.filter(user=CustomUser.objects.get(username='usuario1'))[0]},
        {'init_date': '2023-12-04 17:50:01', 'end_date': '2024-01-03 17:50:01', 'price': 20, 'is_favourite': True, 'playlist': Playlist.objects.get(name='Like BlackPink'), 'order': Order.objects.filter(user=CustomUser.objects.get(username='usuario1'))[1]},
        {'init_date': '2023-12-04 17:50:01', 'end_date': '2024-01-03 17:50:01', 'price': 15, 'is_favourite': False, 'playlist': Playlist.objects.get(name='DellaBanco'), 'order': Order.objects.filter(user=CustomUser.objects.get(username='usuario1'))[1]},
        {'init_date': '2023-12-06 11:00:00', 'end_date': '2024-01-05 11:00:00', 'price': 12, 'is_favourite': True, 'playlist': Playlist.objects.get(name='MerengueLatino'), 'order': Order.objects.filter(user=CustomUser.objects.get(username='usuario1'))[2]},
        {'init_date': '2023-12-07 23:59:00', 'end_date': '2024-01-06 23:59:00', 'price': 20, 'is_favourite': False, 'playlist': Playlist.objects.get(name='Like BlackPink'), 'order': Order.objects.filter(user=CustomUser.objects.get(username='usuario2'))[0]},
    ]

    if Subscription.objects.all().count() > 0:
        for subscription_data in Subscription.objects.all():
            subscription_data.delete()
    for subscription_data in subscriptions:
        Subscription.objects.create(**subscription_data)

if __name__ == '__main__':
    print('Poblando datos...')
    populate()
    print('Población completa.')

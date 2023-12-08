import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'RitmUS.settings')

import django
django.setup()

from base.models import Playlist, Song

def populate():
    playlists = [
        {'name': 'Metálico', 'description': 'Los éxitos del metal', 'price': 10, 'image': 'static/img/GenerosRock.png', 'genre': 'Rock', 'is_active': True},
        {'name': 'Like BlackPink', 'description': 'Los éxitos del KPOP más recientes', 'price': 20, 'image': 'static/img/GenerosKPOP.png', 'genre': 'KPOP', 'is_active': True},
        {'name': 'DellaBanco', 'description': 'Los éxitos de DellaBanco', 'price': 15, 'image': 'static/img/GenerosTrap.png', 'genre': 'Trap', 'is_active': True},
        {'name': 'MerengueLatino', 'description': 'Los éxitos del merengue latino', 'price': 12, 'image': 'static/img/Merengue.png', 'genre': 'Merengue', 'is_active': True},
        
        # Agrega más datos según sea necesario
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

if __name__ == '__main__':
    print('Poblando datos...')
    populate()
    print('Población completa.')

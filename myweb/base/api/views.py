from rest_framework.response import Response
from rest_framework.decorators import api_view
from ..models import Album
from .serialicers import AlbumSerializer

@api_view(['GET'])
def get_routes(request):
    routes = [
        "GET /api",
        "GET /api/albums",
        "GET /api/album/:id"
    ]
    return Response(routes)

@api_view(['GET'])
def get_albums(request):
    albums = Album.objects.all()
    serializer = AlbumSerializer(albums, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_album(request, id):
    album = Album.objects.get(id=id)
    serializer = AlbumSerializer(album, many=False)
    return Response(serializer.data)
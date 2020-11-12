"""Songs app schema"""

import graphene
from graphql_jwt.decorators import login_required
from graphene_django import DjangoObjectType

from .models import Album


class AlbumType(DjangoObjectType):
    """Album object for GraphQL"""
    class Meta:
        model = Album
        fields = ("name", "cover")

    def resolve_cover(self, info):
        """Resolve product image absolute path"""
        if self.cover:
            self.cover = info.context.build_absolute_uri(self.cover.url)
        return self.cover


class Query(graphene.ObjectType):
    """Songs app queries"""
    get_albums = graphene.List(AlbumType)

    @login_required
    def resolve_get_albums(root, info):
        return Album.objects.all()

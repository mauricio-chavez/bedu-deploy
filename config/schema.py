"""Project schema"""

from django.utils.translation import gettext_lazy as _

import graphene
import graphql_jwt

from songs.schema import Query as SongsQuery


class Query(SongsQuery):
    """Project root query"""
    hello = graphene.String(required=True)

    def resolve_hello(info, context):
        """Returns a hello world"""
        return _('¡Hola mundo!')


class Mutation(graphene.ObjectType):
    """Project root mutation"""
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)

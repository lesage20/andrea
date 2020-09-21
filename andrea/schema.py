import graphene
import blog.schema, website.schema


class Query(blog.schema.Query,website.schema.Query ):
    pass







schema = graphene.Schema(query=Query)
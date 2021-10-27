import graphene
from sampleapp.schema import Query as user_query
from sampleapp.schema import Mutations as user_mutation

class Query(user_query):
    pass
class Mutations(user_mutation):
    pass

schema = graphene.Schema(query = Query , mutation = Mutations)


import graphene
from graphene_django.types import DjangoObjectType
from sampleapp.models import Userdata


class UserType(DjangoObjectType):
    class Meta:
        model = Userdata

class Query(graphene.ObjectType):
    all_users = graphene.List(UserType)
    print(all_users)

    def resolve_all_users(self,info,**kwargs):
        return Userdata.objects.all()
    
class CreateUser(graphene.Mutation):
    user=graphene.Field(UserType)
    class Arguments:
        username = graphene.String()
        email = graphene.String()
        firstname = graphene.String()
        lastname = graphene.String()

        
    def mutate(self,info,**kwargs):
            user = Userdata(username=kwargs.get('username'),email=kwargs.get('email'),firstname=kwargs.get('firstname'),lastname=kwargs.get('lastname'))
            '''username = user(username=username)
            email = user(email=email)
            firstname = user(firstname = firstname)
            lastname = user(lastname = lastname)'''
            user.save()
            return CreateUser(user=user)
        


class Mutations(graphene.ObjectType):
    create_user = CreateUser.Field()
    
    



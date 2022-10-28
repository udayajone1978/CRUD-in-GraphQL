import graphene
from graphene_django import DjangoObjectType
from .models import employee


class empdetailstype(DjangoObjectType):
    class Meta:
        model = employee
        fields = ("empid", "empname", "empage", "empaddress")


class Query(graphene.ObjectType):
    all_details = graphene.List(empdetailstype)



    def resolve_all_details(root,info):
            return employee.objects.all()


schema = graphene.Schema(query=Query)
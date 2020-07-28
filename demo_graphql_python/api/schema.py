# cookbook/ingredients/schema.py
import graphene

from graphene_django.types import DjangoObjectType

from demo_graphql_python.api.models import Student


class StudentType(DjangoObjectType):
    class Meta:
        model = Student


class Query(graphene.ObjectType):
    students = graphene.List(StudentType)

    def resolve_all_categories(self, info, **kwargs):
        return Student.objects.all()

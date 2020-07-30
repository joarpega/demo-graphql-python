import graphene
from graphene_django import DjangoObjectType
from .models import *


class StudentType(DjangoObjectType):
    class Meta:
        model = Student


class Query(graphene.ObjectType):
    students = graphene.List(StudentType)

    def resolve_students(self, info, **kwargs):
        return Student.objects.all()

'''StudentMutation'''
class StudentMutation(graphene.Mutation):
    class Arguments:
        '''The input arguments for this mutation'''
        name = graphene.String()
        email = graphene.String()
        phone = graphene.String()
        id = graphene.ID()
    
    # The class attributes define the response of the mutation
    student = graphene.Field(StudentType)

    def mutate(self, info, name, email, phone, id=None):
        student = Student.objects.get(pk=id)
        student.name = name
        student.email = email
        student.phone = phone
        student.save()

        return StudentMutation(student=student)

class Mutation(graphene.ObjectType):
    ''' update_student '''
    update_student = StudentMutation.Field()

"""demo_graphql_python URL Configuration"""
""" URLs Module """

from django.contrib import admin
from django.urls import path, include

from django.views.decorators.csrf import csrf_exempt

from graphene_django.views import GraphQLView

urlpatterns = [
    path('', csrf_exempt(GraphQLView.as_view(graphiql=True))),
]

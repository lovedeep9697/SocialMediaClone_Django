# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth import LoginRequiredMixin,PermissionRequiredMixin
from djando.url import reverse
from django.views import generic
from groups.models import Group,GroupMember
# Create your views here.


class CreateGroup(LoginRequiredMixin,generic.CreateView):
	fields = ('name','description')
	model = Group

class SingleGroup(generic.DetailView):
	model = Group

class ListGroups(generic.ListView):
	models = Group


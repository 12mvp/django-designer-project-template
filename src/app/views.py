# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import TemplateView

ROLE_1 = 'role_1'
ROLE_2 = 'role_2'
ROLE_3 = 'role_3'
DEFAULT_ROLE = ROLE_1

class LoggedInView(TemplateView):
    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        role = request.GET.get('role', None)

        if role is not None:
            request.session['role'] = role
            context['role'] = role
        else:
            context['role'] = request.session.get('role', DEFAULT_ROLE)
        request.session.save()

        response = self.render_to_response(context)        
        return response


class IndexView(LoggedInView):
    template_name = 'index.html'

class DashboardView(LoggedInView):
    template_name = 'dashboard.html'

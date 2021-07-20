# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.conf.urls import include
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', include('nobinobi_core.urls', namespace='nobinobi_core')),
    path('admin/', admin.site.urls),

]


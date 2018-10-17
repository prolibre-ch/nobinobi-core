# -*- coding: utf-8
from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class NobinobiCoreConfig(AppConfig):
    name = 'nobinobi_core'
    verbose_name = _("Core")
    verbose_name_plural = _("Core")

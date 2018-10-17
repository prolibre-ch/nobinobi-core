# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import gettext_lazy as _


class Holiday(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    date = models.DateField(_("Date"))

    class Meta:
        ordering = ['date']
        verbose_name = _("Holiday")
        verbose_name_plural = _("Holidays")

    def __str__(self):  # __unicode__ on Python 2
        # Returns the person's full name.
        return "{} - {}".format(self.name, self.date)

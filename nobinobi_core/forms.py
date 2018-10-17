# -*- coding: utf-8 -*-
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from django.utils.translation import gettext as _


class AddOfficialHolidayForm(forms.Form):
    """form de validation pour l'ajout"""

    def __init__(self, *args, **kwargs):
        super(AddOfficialHolidayForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        # self.helper.
        self.helper.form_class = 'form-horizontal blueForms'
        self.helper.label_class = ""
        self.helper.field_class = "col-lg-12"
        self.helper.add_input(Submit('submit', _("Submit")))

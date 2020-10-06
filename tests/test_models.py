#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_nobinobi-core
------------

Tests for `nobinobi-core` models module.
"""

from django.test import TestCase
from django.utils import timezone

from nobinobi_core.models import Holiday, Company, CompanyClosure


class TestNobinobiCoreModels(TestCase):

    def setUp(self):
        self.holiday = Holiday(name="My entry title", date=timezone.localdate())
        self.company = Company(name="Prolibre", short_code="PRO")
        self.company_closure = CompanyClosure(from_date=timezone.localdate(), end_date=timezone.localdate(),
                                              company=self.company)

    def test_str_representation_holiday(self):
        self.assertEqual(str(self.holiday), "{} - {}".format(self.holiday.name, self.holiday.date))

    def test_str_representation_company(self):
        self.assertEqual(str(self.company), "{} - {}".format(self.company.name, self.company.short_code))

    def test_str_representation_company_closure(self):
        self.assertEqual(str(self.company_closure),
                         "{} ({} | {})".format(self.company.name, self.company_closure.from_date,
                                               self.company_closure.end_date))

    def tearDown(self):
        pass

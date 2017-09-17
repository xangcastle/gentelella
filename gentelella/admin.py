# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin


class GentelellaSite(admin.AdminSite):
    site_header = "DC Group"
    index_template = "gentelella/index.html"
    app_index_template = "gentelella/app_index.html"
    #password_change_template = ""


site = GentelellaSite(name="gentelella")


class ModelAdmin(admin.ModelAdmin):
    change_form_template = "gentelella/change_form.html"
    change_list_template = "gentelella/change_list.html"


# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url
from django.contrib import admin

from kvstore.admin.views import upload


class KVStoreAdminApp(admin.ModelAdmin):

    def get_urls(self):
        return [
            url(
                r'^kvstore/upload/?$',
                self.admin_site.admin_view(upload),
                name="kvstore_upload"
            ),
        ]

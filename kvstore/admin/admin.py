# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.urls import path
from django.contrib import admin

from kvstore.admin.views import upload, upload_bulk, upload_csv


class KVStoreAdminApp(admin.ModelAdmin):

    def get_urls(self):
        return [
            path(
                'kvstore/upload/',
                self.admin_site.admin_view(upload),
                name="kvstore_upload_ui"
            ),
            path(
                'kvstore/upload_bulk/',
                self.admin_site.admin_view(upload_bulk),
                name="kvstore_upload_bulk"
            ),
            path(
                'kvstore/upload_csv/',
                self.admin_site.admin_view(upload_csv),
                name="kvstore_upload_csv"
            ),
        ]

from django.contrib import admin

from .admin_site import edc_sync_file_monitor_admin
from edc_base.modeladmin_mixins import audit_fieldset_tuple


from edc_base.modeladmin_mixins import (
    ModelAdminNextUrlRedirectMixin, ModelAdminFormInstructionsMixin,
    ModelAdminFormAutoNumberMixin, ModelAdminAuditFieldsMixin,
    ModelAdminReadOnlyMixin, ModelAdminInstitutionMixin)
from django_revision.modeladmin_mixin import ModelAdminRevisionMixin

from .forms import ClientForm

from .models import Client


@admin.register(Client, site=edc_sync_file_monitor_admin)
class ClientAdmin(ModelAdminNextUrlRedirectMixin,
                  ModelAdminFormInstructionsMixin,
                  ModelAdminFormAutoNumberMixin, ModelAdminRevisionMixin,
                  ModelAdminAuditFieldsMixin, ModelAdminReadOnlyMixin,
                  ModelAdminInstitutionMixin, admin.ModelAdmin):

    form = ClientForm

    fieldsets = (
        (None, {
            'fields': (
                'sftp_url',
                'sftp_user',
                'sftp_pass',
                'active',
                'remote_dirname')}),
        audit_fieldset_tuple)

    radio_fields = {
    }

from django.contrib import admin
from amoma.models import Patient, PatientRecord, PatientRecordForm

def get_records(object):
 return object.patientRecord.prescription
get_records.short_description = 'Records'

def get_patient_name(obj):
 return "%s %s %s" % (obj.patient.firstname, obj.patient.middlename, obj.patient.lastname)
get_patient_name.short_description = 'Name'

def patientrecord_link(inst):
 url = u'../patientrecord/?q=%s ' % (inst.id)
 return u'<b><a href="%s">Records</a></b>' % url
patientrecord_link.allow_tags = True
patientrecord_link.short_description = u'Patient Records'

class PatientAdmin(admin.ModelAdmin):
 list_display         = (get_patient_name,'age','address', patientrecord_link,)
 search_fields        = ['firstname','middlename','lastname']

class PatientRecordAdmin(admin.ModelAdmin):
 form = PatientRecordForm
 list_display = ('patient','consultation_date','diagnosis', 'labresults','prescription')
 search_fields = ['patient__id','patient__firstname','patient__middlename','patient__lastname']

 def get_model_perms(self, request):
	"""
	return empty perms dic
	"""
	return {}

admin.site.register(Patient, PatientAdmin)
admin.site.register(PatientRecord, PatientRecordAdmin)

# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PatientRecord'
        db.create_table('amoma_patientrecord', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('diagnosis', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('labResults', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('prescription', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('amoma', ['PatientRecord'])

        # Adding field 'Patient.patientRecord'
        db.add_column('amoma_patient', 'patientRecord',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['amoma.PatientRecord']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'PatientRecord'
        db.delete_table('amoma_patientrecord')

        # Deleting field 'Patient.patientRecord'
        db.delete_column('amoma_patient', 'patientRecord_id')


    models = {
        'amoma.patient': {
            'Meta': {'object_name': 'Patient', '_ormbases': ['amoma.Person']},
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'patientRecord': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['amoma.PatientRecord']"}),
            'person_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['amoma.Person']", 'unique': 'True', 'primary_key': 'True'}),
            'registration_date': ('django.db.models.fields.DateField', [], {'max_length': '15'})
        },
        'amoma.patientrecord': {
            'Meta': {'object_name': 'PatientRecord'},
            'diagnosis': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'labResults': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'prescription': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        'amoma.person': {
            'Meta': {'object_name': 'Person'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'age': ('django.db.models.fields.IntegerField', [], {}),
            'birthdate': ('django.db.models.fields.DateField', [], {'max_length': '15'}),
            'citizenship': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'marital': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'religion': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'telNo': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['amoma']
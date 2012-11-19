# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Patient.slug'
        db.add_column('amoma_patient', 'slug',
                      self.gf('django.db.models.fields.SlugField')(default=1, unique=True, max_length=50),
                      keep_default=False)

        # Adding field 'PatientRecord.slug'
        db.add_column('amoma_patientrecord', 'slug',
                      self.gf('django.db.models.fields.SlugField')(default=1, unique=True, max_length=50),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Patient.slug'
        db.delete_column('amoma_patient', 'slug')

        # Deleting field 'PatientRecord.slug'
        db.delete_column('amoma_patientrecord', 'slug')


    models = {
        'amoma.patient': {
            'Meta': {'object_name': 'Patient', '_ormbases': ['amoma.Person']},
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'patientRecord': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['amoma.PatientRecord']"}),
            'person_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['amoma.Person']", 'unique': 'True', 'primary_key': 'True'}),
            'registration_date': ('django.db.models.fields.DateField', [], {'max_length': '15'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'})
        },
        'amoma.patientrecord': {
            'Meta': {'object_name': 'PatientRecord'},
            'diagnosis': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'labResults': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'prescription': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'})
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
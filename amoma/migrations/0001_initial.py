# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Person'
        db.create_table('amoma_person', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('age', self.gf('django.db.models.fields.IntegerField')()),
            ('telNo', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('marital', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('citizenship', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('religion', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('birthdate', self.gf('django.db.models.fields.DateField')(max_length=15)),
        ))
        db.send_create_signal('amoma', ['Person'])

        # Adding model 'Patient'
        db.create_table('amoma_patient', (
            ('person_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['amoma.Person'], unique=True, primary_key=True)),
            ('registration_date', self.gf('django.db.models.fields.DateField')(max_length=15)),
            ('notes', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('amoma', ['Patient'])


    def backwards(self, orm):
        # Deleting model 'Person'
        db.delete_table('amoma_person')

        # Deleting model 'Patient'
        db.delete_table('amoma_patient')


    models = {
        'amoma.patient': {
            'Meta': {'object_name': 'Patient', '_ormbases': ['amoma.Person']},
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'person_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['amoma.Person']", 'unique': 'True', 'primary_key': 'True'}),
            'registration_date': ('django.db.models.fields.DateField', [], {'max_length': '15'})
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
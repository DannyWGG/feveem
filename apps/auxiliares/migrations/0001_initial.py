# Generated by Django 5.1.3 on 2024-11-22 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plantel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(blank=True, max_length=255, null=True)),
                ('periodo_escolar', models.CharField(blank=True, max_length=255, null=True)),
                ('municipio', models.CharField(blank=True, max_length=255, null=True)),
                ('parroquia', models.CharField(blank=True, max_length=255, null=True)),
                ('cod_plantel', models.CharField(blank=True, max_length=255, null=True)),
                ('nombre_plantel', models.CharField(blank=True, max_length=255, null=True)),
                ('tipo_dependencia', models.CharField(blank=True, max_length=255, null=True)),
                ('modalidad_principal', models.CharField(blank=True, max_length=255, null=True)),
                ('estatus_plantel', models.CharField(blank=True, max_length=255, null=True)),
                ('nivel_principal', models.CharField(blank=True, max_length=255, null=True)),
                ('zona_ubicacion', models.CharField(blank=True, max_length=255, null=True)),
                ('maternal_masculino', models.IntegerField(blank=True, null=True)),
                ('maternal_femenino', models.IntegerField(blank=True, null=True)),
                ('prescolar_masculino', models.IntegerField(blank=True, null=True)),
                ('prescolar_femenino', models.IntegerField(blank=True, null=True)),
                ('primaria_masculino', models.IntegerField(blank=True, null=True)),
                ('primaria_femenino', models.IntegerField(blank=True, null=True)),
                ('media_masculino', models.IntegerField(blank=True, null=True)),
                ('media_femenino', models.IntegerField(blank=True, null=True)),
                ('media_general_masculino', models.IntegerField(blank=True, null=True)),
                ('media_general_femenino', models.IntegerField(blank=True, null=True)),
                ('tecnica_masculino', models.IntegerField(blank=True, null=True)),
                ('tecnica_femenino', models.IntegerField(blank=True, null=True)),
                ('adulto_masculino', models.IntegerField(blank=True, null=True)),
                ('adulto_femenino', models.IntegerField(blank=True, null=True)),
                ('especial_masculino', models.IntegerField(blank=True, null=True)),
                ('especial_femenino', models.IntegerField(blank=True, null=True)),
                ('total', models.IntegerField(blank=True, null=True)),
                ('director_nombre', models.CharField(blank=True, max_length=255, null=True)),
                ('director_apellido', models.CharField(blank=True, max_length=255, null=True)),
                ('tipo_documento', models.CharField(blank=True, max_length=255, null=True)),
                ('documento_identidad', models.CharField(blank=True, max_length=255, null=True)),
                ('telefono_director', models.CharField(blank=True, max_length=255, null=True)),
                ('telefono_movil_director', models.CharField(blank=True, max_length=255, null=True)),
                ('correo', models.EmailField(blank=True, max_length=255, null=True)),
                ('twitter', models.CharField(blank=True, max_length=255, null=True)),
                ('direccion', models.CharField(blank=True, max_length=255, null=True)),
                ('peridoescolar', models.IntegerField(blank=True, null=True)),
                ('zona_ubucacion', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'plantel',
                'verbose_name_plural': 'planteles',
                'db_table': 'auxiliares"."plantel',
                'managed': False,
            },
        ),
    ]

# Generated by Django 5.0.7 on 2024-11-08 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feveem', '0002_alter_asistente_extra_curricular_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='asistente',
            options={'managed': True, 'verbose_name': 'Vocero', 'verbose_name_plural': 'Voceros'},
        ),
        migrations.AlterField(
            model_name='asistente',
            name='identificador',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]

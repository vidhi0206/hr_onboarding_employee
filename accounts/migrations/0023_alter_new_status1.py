# Generated by Django 3.2 on 2021-10-04 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0022_auto_20211003_0942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='status1',
            field=models.BooleanField(blank=True, choices=[(True, 'Approved'), (False, 'Declined')]),
        ),
    ]
# Generated by Django 5.1.7 on 2025-03-28 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tables', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='published',
            field=models.BooleanField(choices=[(0, 'Планируемый'), (1, 'Принятый')], default=0),
        ),
    ]

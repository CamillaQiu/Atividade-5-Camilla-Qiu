# Generated by Django 5.0.2 on 2024-04-19 17:56

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meuapp', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='movimento',
            name='usuario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='movimento',
            name='tipo',
            field=models.CharField(choices=[('Aquecimento', 'Aquecimento'), ('Acrobacia', 'Acrobacia'), ('Giro', 'Giro'), ('Outros', 'Outro Tipo')], max_length=60),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trip', '0004_auto_20150317_1004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='mail',
            field=models.EmailField(default=b'', unique=True, max_length=70),
            preserve_default=True,
        ),
    ]

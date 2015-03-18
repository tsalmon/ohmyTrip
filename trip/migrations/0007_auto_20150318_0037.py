# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trip', '0006_auto_20150318_0028'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profil',
            old_name='nightClub',
            new_name='nightclub',
        ),
    ]

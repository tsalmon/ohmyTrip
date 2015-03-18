# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trip', '0005_auto_20150317_1017'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profil',
            old_name='Board',
            new_name='board',
        ),
        migrations.RenameField(
            model_name='profil',
            old_name='Bridge',
            new_name='bridge',
        ),
        migrations.RenameField(
            model_name='profil',
            old_name='Church',
            new_name='church',
        ),
        migrations.RenameField(
            model_name='profil',
            old_name='Landmarks',
            new_name='landmarks',
        ),
        migrations.RenameField(
            model_name='profil',
            old_name='NightClub',
            new_name='nightClub',
        ),
        migrations.RenameField(
            model_name='profil',
            old_name='Restaurant',
            new_name='restaurant',
        ),
        migrations.RenameField(
            model_name='profil',
            old_name='Zoo',
            new_name='zoo',
        ),
    ]

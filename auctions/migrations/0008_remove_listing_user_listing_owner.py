# Generated by Django 4.0.5 on 2022-07-07 22:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0007_listing_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='user',
        ),
        migrations.AddField(
            model_name='listing',
            name='owner',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='listings', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
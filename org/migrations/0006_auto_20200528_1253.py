# Generated by Django 3.0.5 on 2020-05-28 12:53

from django.db import migrations
import org.custom_model_field


class Migration(migrations.Migration):

    dependencies = [
        ('org', '0005_auto_20200506_2047'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='default_permission_set',
        ),
        migrations.RemoveField(
            model_name='member',
            name='permissions',
        ),
        migrations.AddField(
            model_name='group',
            name='default_permissions',
            field=org.custom_model_field.PermissionField(),
        ),
        migrations.DeleteModel(
            name='PermissionSet',
        ),
    ]

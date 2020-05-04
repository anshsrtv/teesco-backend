# Generated by Django 3.0.5 on 2020-04-29 11:17

from django.db import migrations, models
import org.custom_model_field


class Migration(migrations.Migration):

    dependencies = [
        ('org', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PermissionSetTestModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('perm', org.custom_model_field.PermissionField()),
            ],
        ),
        migrations.DeleteModel(
            name='PermissionField',
        ),
        migrations.DeleteModel(
            name='Test',
        ),
    ]
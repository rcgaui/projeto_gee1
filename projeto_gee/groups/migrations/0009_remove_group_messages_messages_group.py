# Generated by Django 4.1.1 on 2022-09-28 01:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0008_messages_group_messages'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='messages',
        ),
        migrations.AddField(
            model_name='messages',
            name='group',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='groups.group'),
            preserve_default=False,
        ),
    ]
# Generated by Django 5.0.6 on 2024-05-16 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_evaluation_assi_falta_injust_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='evaluation',
            old_name='assi_falta_injust',
            new_name='dispo',
        ),
        migrations.RenameField(
            model_name='evaluation',
            old_name='assi_falta_just',
            new_name='falta_injust',
        ),
        migrations.AddField(
            model_name='evaluation',
            name='dispo_comment',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='evaluation',
            name='expert',
            field=models.IntegerField(default=4),
        ),
        migrations.AddField(
            model_name='evaluation',
            name='expert_comment',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='evaluation',
            name='falta_comment',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='evaluation',
            name='falta_just',
            field=models.IntegerField(default=3),
        ),
        migrations.AddField(
            model_name='evaluation',
            name='geral_comment',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AddField(
            model_name='evaluation',
            name='produ',
            field=models.IntegerField(default=4),
        ),
        migrations.AddField(
            model_name='evaluation',
            name='produ_comment',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='evaluation',
            name='respo',
            field=models.IntegerField(default=3),
        ),
        migrations.AddField(
            model_name='evaluation',
            name='respo_comment',
            field=models.CharField(default='', max_length=100),
        ),
    ]

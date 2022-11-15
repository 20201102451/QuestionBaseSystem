# Generated by Django 4.1.1 on 2022-11-15 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CollectTestpaper', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='score',
            field=models.IntegerField(default=2, verbose_name='分值'),
        ),
        migrations.AddField(
            model_name='gapfill',
            name='score',
            field=models.IntegerField(default=3, verbose_name='分值'),
        ),
        migrations.AddField(
            model_name='testpaper',
            name='apply_time',
            field=models.DateField(blank=True, null=True, verbose_name='出题时间'),
        ),
        migrations.AddField(
            model_name='testpaper',
            name='hard',
            field=models.IntegerField(blank=True, null=True, verbose_name='试卷难度'),
        ),
        migrations.AddField(
            model_name='testpaper',
            name='intro',
            field=models.TextField(blank=True, null=True, verbose_name='试卷简介'),
        ),
        migrations.AddField(
            model_name='trueorfalse',
            name='score',
            field=models.IntegerField(default=1, verbose_name='分值'),
        ),
    ]

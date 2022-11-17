# Generated by Django 4.1.3 on 2022-11-17 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Consumer', '0003_consumer_answer_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='consumer',
            options={'verbose_name': '普通用户', 'verbose_name_plural': '普通用户'},
        ),
        migrations.AlterField(
            model_name='consumer',
            name='birthday',
            field=models.DateField(blank=True, null=True, verbose_name='出生日期'),
        ),
        migrations.AlterField(
            model_name='consumer',
            name='consumer_account',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='用户账户'),
        ),
        migrations.AlterField(
            model_name='consumer',
            name='consumer_id',
            field=models.BigAutoField(primary_key=True, serialize=False, verbose_name='用户id'),
        ),
        migrations.AlterField(
            model_name='consumer',
            name='consumer_name',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='用户名'),
        ),
        migrations.AlterField(
            model_name='consumer',
            name='consumer_password',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='用户密码'),
        ),
        migrations.AlterField(
            model_name='consumer',
            name='email',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='电子邮箱'),
        ),
        migrations.AlterField(
            model_name='consumer',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='姓名'),
        ),
        migrations.AlterField(
            model_name='consumer',
            name='number',
            field=models.CharField(blank=True, max_length=12, null=True, verbose_name='电话号'),
        ),
        migrations.AlterField(
            model_name='consumer',
            name='security_answer',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='密保答案'),
        ),
        migrations.AlterField(
            model_name='consumer',
            name='security_question',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='密保问题'),
        ),
        migrations.AlterField(
            model_name='consumer',
            name='sex',
            field=models.CharField(blank=True, max_length=2, null=True, verbose_name='性别'),
        ),
    ]
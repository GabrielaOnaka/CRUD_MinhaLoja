# Generated by Django 4.1.7 on 2023-03-22 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LojaInstituto', '0002_rename_cliente_pessoa'),
    ]

    operations = [
        migrations.AddField(
            model_name='pessoa',
            name='uf',
            field=models.CharField(max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='cpf',
            field=models.CharField(max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='email',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='nome',
            field=models.CharField(max_length=60, null=True),
        ),
    ]

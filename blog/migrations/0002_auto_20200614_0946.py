# Generated by Django 3.0.7 on 2020-06-14 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('quarantine', 'Quarantine related'), ('stigma', 'Stigma related'), ('testing', 'Testing related')], default='stigma', max_length=32),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
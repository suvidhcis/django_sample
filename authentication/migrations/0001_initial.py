# Generated by Django 3.2.6 on 2021-08-12 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eid', models.CharField(max_length=20)),
                ('ename', models.CharField(max_length=500)),
                ('email', models.EmailField(max_length=500)),
                ('econtact', models.CharField(max_length=12)),
            ],
            options={
                'db_table': 'employee',
            },
        ),
    ]

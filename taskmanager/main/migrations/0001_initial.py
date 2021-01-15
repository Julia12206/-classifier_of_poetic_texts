# Generated by Django 3.1.4 on 2021-01-10 15:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TextsModel',
            fields=[
                ('klaccName', models.TextField(db_column='klaccName', unique=True)),
                ('klacc', models.AutoField(db_column='klaccID', primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'texts_klasses',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Texts',
            fields=[
                ('itemID', models.AutoField(db_column='itemID', primary_key=True, serialize=False)),
                ('author', models.TextField(db_column='author', unique=True)),
                ('nazvanie', models.TextField(db_column='nazvanie', unique=True)),
                ('stih', models.TextField(db_column='stih', unique=True)),
                ('klacc', models.ForeignKey(db_column='klaccID', on_delete=django.db.models.deletion.DO_NOTHING, to='main.textsmodel')),
            ],
            options={
                'db_table': 'texts',
                'managed': True,
            },
        ),
    ]

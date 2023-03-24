# Generated by Django 4.1.5 on 2023-03-23 15:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('C_name', models.CharField(max_length=200, unique=True)),
            ],
            options={
                'db_table': 'College',
            },
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fac_Name', models.CharField(max_length=200, unique=True)),
            ],
            options={
                'db_table': 'Faculty',
            },
        ),
        migrations.CreateModel(
            name='UserType',
            fields=[
                ('UT_ID', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('UT_Name', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'db_table': 'UserType',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=50, unique=True)),
                ('Password', models.CharField(max_length=50, unique=True)),
                ('UT_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Webtranfer.usertype')),
            ],
            options={
                'db_table': 'User',
            },
        ),
        migrations.CreateModel(
            name='Major',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Mj_Name', models.CharField(max_length=200, unique=True)),
                ('Fac_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Webtranfer.faculty')),
            ],
            options={
                'db_table': 'Major',
            },
        ),
        migrations.CreateModel(
            name='Groups',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('G_Name', models.CharField(max_length=200, unique=True)),
                ('Fac_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Faculty', to='Webtranfer.faculty')),
                ('Mj_Name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Major', to='Webtranfer.major')),
            ],
            options={
                'db_table': 'Groups',
            },
        ),
        migrations.CreateModel(
            name='Coll_Major',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cmj_name', models.CharField(max_length=200)),
                ('Coll_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Webtranfer.college')),
            ],
            options={
                'db_table': 'Coll_Majors',
            },
        ),
    ]
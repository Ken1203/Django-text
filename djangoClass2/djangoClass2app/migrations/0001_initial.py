# Generated by Django 3.0.8 on 2020-08-06 04:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('btitle', models.CharField(max_length=20)),
                ('bpub_date', models.DateField()),
                ('bread', models.IntegerField(default=0)),
                ('bcomment', models.IntegerField(default=0)),
                ('isDelete', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='pocketInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=20)),
                ('pgender', models.BooleanField()),
                ('pcomment', models.CharField(max_length=100)),
                ('isDelete', models.BooleanField(default=False)),
                ('pbook', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djangoClass2app.BookInfo')),
            ],
        ),
    ]

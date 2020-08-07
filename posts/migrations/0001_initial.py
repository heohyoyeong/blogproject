# Generated by Django 3.0.8 on 2020-08-06 04:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=20, verbose_name='작성자')),
                ('contents', models.TextField(max_length=1000, verbose_name='글내용')),
            ],
        ),
        migrations.CreateModel(
            name='Datt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=20, verbose_name='사용자')),
                ('contents', models.CharField(max_length=50, verbose_name='글내용')),
                ('author_text', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.Post')),
            ],
        ),
    ]

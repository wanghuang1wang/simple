# Generated by Django 2.1 on 2020-06-06 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_desc', models.CharField(max_length=100, verbose_name='评论内容')),
                ('comment_time', models.DateTimeField(auto_now_add=True, verbose_name='评论时间')),
                ('ariticle', models.CharField(max_length=30, verbose_name='评论文章')),
            ],
            options={
                'verbose_name': '评论',
                'verbose_name_plural': '评论',
            },
        ),
    ]

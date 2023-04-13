# Generated by Django 4.1.7 on 2023-04-09 06:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TemplateSelect',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faculty', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=20)),
                ('image', models.ImageField(blank=True, upload_to='profile_pics')),
                ('room', models.CharField(max_length=100)),
                ('professor', models.CharField(max_length=100)),
                ('comment', models.CharField(max_length=100)),
                ('url', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lab_id', models.CharField(max_length=10, verbose_name='研究室ID')),
                ('lab_name', models.CharField(max_length=200, verbose_name='研究室名')),
                ('comment', models.TextField(verbose_name='レビューコメント')),
                ('score1', models.PositiveSmallIntegerField(choices=[(1, '★'), (2, '★★'), (3, '★★★'), (4, '★★★★'), (5, '★★★★★')], default='3', verbose_name='担当教授の干渉度')),
                ('score2', models.PositiveSmallIntegerField(choices=[(1, '★'), (2, '★★'), (3, '★★★'), (4, '★★★★'), (5, '★★★★★')], default='3', verbose_name='先輩・後輩との関わり')),
                ('score3', models.PositiveSmallIntegerField(choices=[(1, '★'), (2, '★★'), (3, '★★★'), (4, '★★★★'), (5, '★★★★★')], default='3', verbose_name='研究室の設備')),
                ('score4', models.PositiveSmallIntegerField(choices=[(1, '★'), (2, '★★'), (3, '★★★'), (4, '★★★★'), (5, '★★★★★')], default='3', verbose_name='学会などのレベル')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('lab_id', 'user')},
            },
        ),
    ]

# Generated by Django 4.0.2 on 2022-03-07 12:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0001_initial'),
        ('user', '0005_auto_20220301_1448'),
    ]

    operations = [
        migrations.CreateModel(
            name='MedalType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medal_name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='LearningHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='생성된 날짜')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='수정된 날짜')),
                ('score', models.IntegerField(blank=True)),
                ('learning_video_id', models.ForeignKey(db_column='learning_video_id', default='', on_delete=django.db.models.deletion.CASCADE, to='video.learningvideo')),
                ('medal_id', models.ForeignKey(db_column='medal_id', default='', on_delete=django.db.models.deletion.CASCADE, to='user.medaltype')),
                ('user_id', models.ForeignKey(db_column='user_id', default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'learning_history',
            },
        ),
    ]

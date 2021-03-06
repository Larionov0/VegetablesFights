# Generated by Django 3.0.3 on 2020-02-19 19:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authsys', '0001_initial'),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='user_profiles',
            field=models.ManyToManyField(to='authsys.UserProfile'),
        ),
        migrations.CreateModel(
            name='Deck',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=30)),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authsys.UserProfile')),
            ],
        ),
    ]

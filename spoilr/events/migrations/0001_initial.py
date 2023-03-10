# Generated by Django 4.0.7 on 2023-02-19 21:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('spoilr_core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True)),
                ('name', models.CharField(max_length=200)),
                ('expected_start_time', models.DateTimeField()),
                ('min_participants', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('max_participants', models.PositiveSmallIntegerField(default=1)),
                ('status', models.CharField(choices=[('unavailable', 'The event is not yet available for registration'), ('open', 'Teams can register for the event'), ('closed', 'Teams can no longer register for the event'), ('post', 'The event is over and the event answer checker can be shown')], default='unavailable', max_length=20)),
                ('location', models.CharField(blank=True, max_length=64, null=True)),
                ('description', models.TextField()),
                ('puzzle', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='spoilr_core.puzzle')),
            ],
        ),
        migrations.CreateModel(
            name='EventParticipant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('pronouns', models.CharField(blank=True, max_length=200)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='participants', to='spoilr_events.event')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spoilr_core.team')),
            ],
        ),
    ]

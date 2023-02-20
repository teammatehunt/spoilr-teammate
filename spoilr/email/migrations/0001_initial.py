# Generated by Django 4.0.7 on 2023-02-19 21:35

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('spoilr_hq', '__first__'),
        ('spoilr_core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BadEmailAddress',
            fields=[
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('reason', models.CharField(choices=[('UNS', 'Unsubscribed'), ('BOU', 'Bounced')], max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='CannedEmail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('subject', models.TextField(help_text='Automatically prepended with [Mystery Hunt]')),
                ('from_address', models.CharField(help_text='The email address this email should be sent from', max_length=256)),
                ('text_content', models.TextField(blank=True)),
                ('html_content', models.TextField(blank=True)),
                ('description', models.CharField(help_text='A description of when this email should be used, including to which recipients', max_length=1000)),
                ('interaction', models.ForeignKey(blank=True, help_text='If this field is blank, it will show up for all interactions.', null=True, on_delete=django.db.models.deletion.PROTECT, to='spoilr_core.interaction')),
            ],
        ),
        migrations.CreateModel(
            name='EmailTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.TextField(blank=True)),
                ('text_content', models.TextField(blank=True)),
                ('html_content', models.TextField(blank=True)),
                ('from_address', models.TextField()),
                ('scheduled_datetime', models.DateTimeField()),
                ('status', models.CharField(choices=[('SCHD', 'Scheduled'), ('SOUT', 'Sending'), ('SENT', 'Sent'), ('DRFT', 'Draft'), ('CANC', 'Cancelled')], default='DRFT', max_length=4)),
                ('recipients', models.CharField(choices=[('TE', 'all_teams'), ('AD', 'batch_addresses')], max_length=2)),
                ('addresses', models.JSONField(blank=True, default=list)),
                ('batch_size', models.IntegerField(default=50)),
                ('batch_delay_ms', models.IntegerField(default=100)),
                ('last_user_pk', models.IntegerField(default=-1)),
                ('last_team_pk', models.IntegerField(default=-1)),
                ('last_address_index', models.IntegerField(default=-1)),
            ],
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('raw_content', models.BinaryField(blank=True)),
                ('subject', models.TextField(blank=True)),
                ('text_content', models.TextField(blank=True)),
                ('html_content', models.TextField(blank=True)),
                ('header_content', models.BinaryField(blank=True)),
                ('from_address', models.TextField(blank=True)),
                ('to_addresses', models.JSONField(blank=True, default=list)),
                ('cc_addresses', models.JSONField(blank=True, default=list)),
                ('bcc_addresses', models.JSONField(blank=True, default=list)),
                ('has_attachments', models.BooleanField(default=False)),
                ('message_id', models.TextField(blank=True, db_index=True)),
                ('in_reply_to_id', models.TextField(blank=True, db_index=True)),
                ('root_reference_id', models.TextField(blank=True, db_index=True)),
                ('reference_ids', models.JSONField(blank=True, default=list)),
                ('sent_datetime', models.DateTimeField(blank=True, null=True)),
                ('is_spam', models.BooleanField(default=False)),
                ('is_authenticated', models.BooleanField(default=False)),
                ('attempted_send_datetime', models.DateTimeField(blank=True, null=True)),
                ('received_datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('uidvalidity', models.IntegerField(blank=True, null=True)),
                ('uid', models.IntegerField(blank=True, null=True)),
                ('modseq', models.IntegerField(blank=True, null=True)),
                ('is_from_us', models.BooleanField()),
                ('created_via_webapp', models.BooleanField()),
                ('scheduled_datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('opened', models.BooleanField(default=False)),
                ('status', models.CharField(choices=[('SOUT', 'Sending'), ('SENT', 'Sent'), ('RNR', 'Received - No reply'), ('RANS', 'Received - Answered'), ('RNRR', 'Received - No reply required'), ('RH', 'Received - Hint'), ('RB', 'Received - Bounce'), ('RUNS', 'Received - Unsubscribe'), ('RSUB', 'Received - Resubscribe'), ('DRFT', 'Draft'), ('CANC', 'Cancelled')], max_length=4)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='spoilr_hq.handler')),
                ('canned_template', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='spoilr_email.cannedemail')),
                ('interaction', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='spoilr_core.interaction')),
                ('response', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='request_set', to='spoilr_email.email')),
                ('team', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='spoilr_core.team')),
                ('template', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='spoilr_email.emailtemplate')),
            ],
            options={
                'ordering': ['-received_datetime'],
                'unique_together': {('uidvalidity', 'uid'), ('team', 'canned_template')},
            },
        ),
    ]

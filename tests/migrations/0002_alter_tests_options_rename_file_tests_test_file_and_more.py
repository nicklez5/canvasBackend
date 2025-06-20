# Generated by Django 5.2.1 on 2025-06-01 15:31

import django.db.models.deletion
import tests.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tests',
            options={},
        ),
        migrations.RenameField(
            model_name='tests',
            old_name='file',
            new_name='test_file',
        ),
        migrations.RemoveField(
            model_name='tests',
            name='student_file',
        ),
        migrations.RemoveField(
            model_name='tests',
            name='student_points',
        ),
        migrations.RemoveField(
            model_name='tests',
            name='submitter',
        ),
        migrations.AlterField(
            model_name='tests',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterModelTable(
            name='tests',
            table=None,
        ),
        migrations.CreateModel(
            name='TestSubmission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submitted_at', models.DateTimeField(auto_now_add=True)),
                ('student_file', models.FileField(blank=True, null=True, storage=tests.models.select_storage, upload_to='tests/submissions/')),
                ('student_points', models.IntegerField(blank=True, null=True)),
                ('graded_at', models.DateTimeField(blank=True, null=True)),
                ('feedback', models.TextField(blank=True)),
                ('graded_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='graded_test_submissions', to=settings.AUTH_USER_MODEL)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='test_submissions', to=settings.AUTH_USER_MODEL)),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submissions', to='tests.tests')),
            ],
            options={
                'ordering': ['-submitted_at'],
                'unique_together': {('test', 'student')},
            },
        ),
    ]

# Generated by Django 2.1.7 on 2019-04-17 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Submissions_Demo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_id', models.CharField(max_length=64)),
                ('task_name', models.CharField(max_length=64)),
                ('task_type', models.CharField(max_length=64)),
                ('train_data', models.CharField(max_length=64)),
                ('test_data', models.CharField(max_length=64)),
                ('label', models.CharField(max_length=64)),
                ('feat_sel', models.CharField(max_length=64)),
                ('estimator', models.CharField(max_length=64)),
                ('cv_type', models.CharField(max_length=64)),
                ('note', models.CharField(max_length=64)),
                ('verbose', models.IntegerField(max_length=64)),
            ],
        ),
    ]

# Generated by Django 5.0.1 on 2024-02-28 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apostilas', '0002_viewapostila'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='apostila',
            name='tags',
            field=models.ManyToManyField(to='apostilas.tags'),
        ),
    ]

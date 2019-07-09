# Generated by Django 2.0.7 on 2018-09-17 16:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='genres',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(choices=[('arcade', 'arcade'), ('action', 'action'), ('racing', 'racing'), ('puzzle', 'puzzle'), ('strategy', 'strategy'), ('sports', 'sports'), ('war', 'war')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='launch',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('year', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='manufacturer',
            fields=[
                ('company', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('about', models.CharField(max_length=1000)),
            ],
        ),
        migrations.AlterField(
            model_name='description',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.launch'),
        ),
        migrations.AlterField(
            model_name='popular',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.launch'),
        ),
        migrations.DeleteModel(
            name='about',
        ),
        migrations.AddField(
            model_name='launch',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.manufacturer'),
        ),
        migrations.AddField(
            model_name='genres',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.launch'),
        ),
    ]
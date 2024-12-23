# Generated by Django 4.2.5 on 2024-11-12 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapa', '0004_rename_url_imagem_imagem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projeto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
                ('imagem', models.ImageField(upload_to='imagens/')),
                ('link', models.URLField(blank=True)),
            ],
        ),
    ]

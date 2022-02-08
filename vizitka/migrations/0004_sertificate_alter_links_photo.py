# Generated by Django 4.0.2 on 2022-02-08 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vizitka', '0003_remove_info_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sertificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=45, verbose_name='Название ')),
                ('photo', models.ImageField(blank=True, upload_to='vizitka/imgSert')),
                ('url', models.URLField(blank=True, verbose_name='Ссылка')),
            ],
        ),
        migrations.AlterField(
            model_name='links',
            name='photo',
            field=models.ImageField(blank=True, upload_to='vizitka/imgLink'),
        ),
    ]

# Generated by Django 4.1.7 on 2023-04-02 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_image_alter_post_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='name',
            field=models.CharField(db_index=True, default='Anonymous', max_length=55, verbose_name='Name'),
        ),
    ]
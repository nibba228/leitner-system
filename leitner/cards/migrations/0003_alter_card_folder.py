# Generated by Django 4.0.2 on 2022-02-20 16:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0002_remove_card_card_set_card_folder_delete_cardset'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='folder',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cards.folder'),
        ),
    ]
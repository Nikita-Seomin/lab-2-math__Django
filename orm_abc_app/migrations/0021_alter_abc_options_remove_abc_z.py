# Generated by Django 4.1.7 on 2023-06-05 21:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orm_abc_app', '0020_alter_abc_options_rename_a_abc_x_rename_b_abc_y_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='abc',
            options={'ordering': ('-id', '-x'), 'verbose_name': 'Z_Y_Z', 'verbose_name_plural': 'X_Y_Z_S'},
        ),
        migrations.RemoveField(
            model_name='abc',
            name='z',
        ),
    ]

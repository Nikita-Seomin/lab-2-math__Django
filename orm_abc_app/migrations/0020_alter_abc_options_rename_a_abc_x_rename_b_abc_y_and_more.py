# Generated by Django 4.1.7 on 2023-06-05 18:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orm_abc_app', '0019_alter_abc_a_alter_abc_b_alter_abc_c_alter_abc_task'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='abc',
            options={'ordering': ('-id', '-x'), 'verbose_name': 'A_B_C', 'verbose_name_plural': 'A_B_C_S'},
        ),
        migrations.RenameField(
            model_name='abc',
            old_name='a',
            new_name='x',
        ),
        migrations.RenameField(
            model_name='abc',
            old_name='b',
            new_name='y',
        ),
        migrations.RenameField(
            model_name='abc',
            old_name='c',
            new_name='z',
        ),
    ]
# Generated by Django 4.1 on 2022-11-13 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_addmoney_info_category_articulo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addmoney_info',
            name='Category',
            field=models.CharField(choices=[('Comida', 'Comida'), ('Viaje', 'Viaje'), ('Compras', 'Compras'), ('Necesidades', 'Necesidades'), ('Entretenimiento', 'Entretenimiento'), ('Ingresos', 'Ingresos'), ('Otro', 'Otro')], default='Comida', max_length=20),
        ),
        migrations.AlterField(
            model_name='addmoney_info',
            name='add_money',
            field=models.CharField(choices=[('Gasto', 'Gasto'), ('Ingreso', 'Ingreso')], max_length=10),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profession',
            field=models.CharField(choices=[('Empleado', 'Empleado'), ('Finanzas', 'Finanzas'), ('Estudiante', 'Estudiante'), ('Otro', 'Otro')], max_length=10),
        ),
    ]

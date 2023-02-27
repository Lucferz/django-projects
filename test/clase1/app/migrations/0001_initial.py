# Generated by Django 4.1.7 on 2023-02-26 21:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('cli_id', models.AutoField(primary_key=True, serialize=False)),
                ('cli_razon_social', models.CharField(max_length=100, null=True)),
                ('cli_ruc', models.CharField(max_length=15, null=True)),
                ('fecha_alta', models.DateField(auto_now_add=True)),
                ('usuario_alta', models.IntegerField()),
                ('fecha_mod', models.DateField(auto_now=True)),
                ('usuario_mod', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Estados',
            fields=[
                ('es_id', models.AutoField(primary_key=True, serialize=False)),
                ('es_desc', models.CharField(max_length=80)),
                ('es_cod', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Servicios',
            fields=[
                ('ser_id', models.AutoField(primary_key=True, serialize=False)),
                ('ser_desc', models.CharField(max_length=100)),
                ('fecha_alta', models.DateField(auto_now_add=True)),
                ('usuario_alta', models.IntegerField()),
                ('fecha_mod', models.DateField(auto_now=True)),
                ('usuario_mod', models.IntegerField(null=True)),
                ('estado_id', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='app.estados')),
            ],
        ),
        migrations.CreateModel(
            name='TipoCliente',
            fields=[
                ('tc_id', models.AutoField(primary_key=True, serialize=False)),
                ('tc_desc', models.CharField(blank=True, max_length=70, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tickets',
            fields=[
                ('ticket_id', models.AutoField(primary_key=True, serialize=False)),
                ('ticket_desc', models.CharField(max_length=250)),
                ('fecha_alta', models.DateField(auto_now_add=True)),
                ('usuario_alta', models.IntegerField()),
                ('fecha_mod', models.DateField(auto_now=True)),
                ('usuario_mod', models.IntegerField(null=True)),
                ('estado_id', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='app.estados')),
            ],
        ),
        migrations.CreateModel(
            name='Terminales',
            fields=[
                ('ter_id', models.AutoField(primary_key=True, serialize=False)),
                ('usuario_id', models.IntegerField()),
                ('ter_desc', models.CharField(max_length=100)),
                ('fecha_alta', models.DateField(auto_now_add=True)),
                ('usuario_alta', models.IntegerField()),
                ('fecha_mod', models.DateField(auto_now=True)),
                ('usuario_mod', models.IntegerField(null=True)),
                ('estado_id', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='app.estados')),
                ('ser_id', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='app.servicios')),
            ],
        ),
        migrations.CreateModel(
            name='Prioridades',
            fields=[
                ('pri_id', models.AutoField(primary_key=True, serialize=False)),
                ('pri_desc', models.CharField(max_length=100)),
                ('fecha_alta', models.DateField(auto_now_add=True)),
                ('usuario_alta', models.IntegerField()),
                ('fecha_mod', models.DateField(auto_now=True)),
                ('usuario_mod', models.IntegerField(null=True)),
                ('estado_id', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='app.estados')),
            ],
        ),
        migrations.CreateModel(
            name='Personas',
            fields=[
                ('per_id', models.AutoField(primary_key=True, serialize=False)),
                ('per_nombre', models.CharField(max_length=100)),
                ('per_apellido', models.CharField(max_length=100)),
                ('per_cedula', models.CharField(max_length=10, null=True)),
                ('per_telefono', models.CharField(max_length=50, null=True)),
                ('per_email', models.EmailField(max_length=254, null=True)),
                ('fecha_alta', models.DateField(auto_now_add=True)),
                ('usuario_alta', models.IntegerField()),
                ('fecha_mod', models.DateField(auto_now=True)),
                ('usuario_mod', models.IntegerField(null=True)),
                ('estado_id', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='app.estados')),
            ],
        ),
        migrations.CreateModel(
            name='Colas',
            fields=[
                ('cola_id', models.AutoField(primary_key=True, serialize=False)),
                ('cola_desc', models.CharField(max_length=150)),
                ('cola_entrada', models.DateField(auto_now=True)),
                ('cola_salida', models.DateField()),
                ('cli_id', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='app.clientes')),
                ('pri_id', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='app.prioridades')),
                ('ser_id', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='app.servicios')),
                ('ter_id', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='app.terminales')),
                ('ticket_id', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='app.tickets')),
            ],
        ),
        migrations.AddField(
            model_name='clientes',
            name='estado_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='app.estados'),
        ),
        migrations.AddField(
            model_name='clientes',
            name='persona_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='app.personas'),
        ),
        migrations.AddField(
            model_name='clientes',
            name='tipo_cliente_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='app.tipocliente'),
        ),
    ]
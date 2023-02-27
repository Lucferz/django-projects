from django.db import models

# Create your models here.
#los fields aparentemente tienen los siguientes parametros max_length, null, blank
class Estados(models.Model):
    es_id = models.AutoField(primary_key=True)
    es_desc =models.CharField(max_length=80,null=False,blank=False)
    es_cod = models.IntegerField(null=False, blank=False)
    def __str__(self) -> str:
        return super().__str__()
        
class Personas(models.Model):
    per_id = models.AutoField(primary_key=True)
    estado_id = models.ForeignKey(Estados, on_delete=models.RESTRICT)
    per_nombre = models.CharField(max_length=100, null=False, blank=False)
    per_apellido = models.CharField(max_length=100, null=False, blank=False)
    per_cedula = models.CharField(max_length=10, null=True)
    per_telefono = models.CharField(max_length=50, null=True)
    per_email = models.EmailField(null=True)
    fecha_alta = models.DateField(auto_now_add=True)
    usuario_alta = models.IntegerField(null=False)
    fecha_mod = models.DateField(auto_now=True)
    usuario_mod= models.IntegerField(null=True)
    def __str__(self) -> str:
        return super().__str__()

class TipoCliente(models.Model):
    tc_id = models.AutoField(primary_key=True)
    tc_desc = models.CharField(max_length=70, null=True, blank=True)
    def __str__(self) -> str:
        return super().__str__()

class Clientes(models.Model):
    cli_id = models.AutoField(primary_key=True)
    persona_id = models.ForeignKey(Personas, on_delete=models.RESTRICT)
    tipo_cliente_id = models.ForeignKey(TipoCliente, on_delete=models.RESTRICT)
    estado_id = models.ForeignKey(Estados, on_delete=models.RESTRICT)
    cli_razon_social = models.CharField(max_length=100, null=True, blank=False)
    cli_ruc = models.CharField(max_length=15, null=True, blank=False)
    fecha_alta = models.DateField(auto_now_add=True)
    usuario_alta = models.IntegerField(null=False)
    fecha_mod = models.DateField(auto_now=True)
    usuario_mod= models.IntegerField(null=True)
    def __str__(self) -> str:
        return super().__str__()

class Prioridades(models.Model):
    pri_id = models.AutoField(primary_key=True)
    estado_id = models.ForeignKey(Estados, on_delete=models.RESTRICT)
    pri_desc = models.CharField(max_length=100, null=False, blank=False)
    fecha_alta = models.DateField(auto_now_add=True)
    usuario_alta = models.IntegerField(null=False)
    fecha_mod = models.DateField(auto_now=True)
    usuario_mod= models.IntegerField(null=True)
    def __str__(self) -> str:
        return super().__str__()
    
class Tickets(models.Model):
    ticket_id = models.AutoField(primary_key=True)
    estado_id = models.ForeignKey(Estados, on_delete=models.RESTRICT)
    ticket_desc = models.CharField(max_length=250, null=False, blank=False)
    fecha_alta = models.DateField(auto_now_add=True)
    usuario_alta = models.IntegerField(null=False)
    fecha_mod = models.DateField(auto_now=True)
    usuario_mod= models.IntegerField(null=True)
    def __str__(self) -> str:
        return super().__str__()

class Servicios(models.Model):
    ser_id = models.AutoField(primary_key=True)
    estado_id = models.ForeignKey(Estados, on_delete=models.RESTRICT)
    ser_desc = models.CharField(max_length=100, null=False, blank=False)
    fecha_alta = models.DateField(auto_now_add=True)
    usuario_alta = models.IntegerField(null=False)
    fecha_mod = models.DateField(auto_now=True)
    usuario_mod= models.IntegerField(null=True)
    def __str__(self) -> str:
        return super().__str__()

#Hacer un alter table para poder enlazar la tabla auth user con 
#la tabla terminales
#ALTER TABLE app_terminales 
#ADD FOREIGN KEY (usuario_id) REFERENCES auth_user(id); 
class Terminales(models.Model):
    ter_id = models.AutoField(primary_key=True)
    estado_id = models.ForeignKey(Estados, on_delete=models.RESTRICT)
    ser_id = models.ForeignKey(Servicios, on_delete=models.RESTRICT)
    usuario_id = models.IntegerField()
    ter_desc = models.CharField(max_length=100, null=False, blank=False)
    fecha_alta = models.DateField(auto_now_add=True)
    usuario_alta = models.IntegerField(null=False)
    fecha_mod = models.DateField(auto_now=True)
    usuario_mod= models.IntegerField(null=True)
    def __str__(self) -> str:
        return super().__str__()

class Colas(models.Model):
    cola_id = models.AutoField(primary_key=True)
    cli_id = models.ForeignKey(Clientes, on_delete=models.RESTRICT)
    pri_id = models.ForeignKey(Prioridades, on_delete=models.RESTRICT)
    ser_id = models.ForeignKey(Servicios, on_delete=models.RESTRICT)
    ticket_id = models.ForeignKey(Tickets, on_delete=models.RESTRICT)
    ter_id = models.ForeignKey(Terminales, on_delete=models.RESTRICT)
    cola_desc = models.CharField(max_length=150, null=False, blank=False)
    cola_entrada = models.DateField(auto_now=True)
    cola_salida = models.DateField()
    def __str__(self) -> str:
        return super().__str__()


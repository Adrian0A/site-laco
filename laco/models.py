from django.db import models

# Create your models here.
class Preco(models.Model):
    preco = models.DecimalField(max_digits=4, decimal_places=2, null=False)


class Tema(models.Model):
    tema = models.CharField(max_length= 64)

class Laco(models.Model):
    preco = models.ForeignKey(Preco, on_delete=models.CASCADE)
    tema = models.ForeignKey(Tema, on_delete=models.CASCADE)

    descricao = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at =  models.DateTimeField(auto_now_add=True)

    picture = models.BinaryField(null=True, editable=True)
    content_type =  models.CharField(max_length=256, null=True, help_text='The MIMEType of the file')
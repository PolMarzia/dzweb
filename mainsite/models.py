from django.db import models

# Create your models here.
class skazka_dar(models.Model):
    id_skazka=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    author=models.CharField(max_length=50)
    image=models.ImageField(upload_to='static/img')
    text=models.TextField(max_length=2000,default='123')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Сказка"
        verbose_name_plural = "Сказки"


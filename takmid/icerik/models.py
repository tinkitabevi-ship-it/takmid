from django.db import models

class Kategori(models.Model):
    isim = models.CharField(max_length=100)
    # Kendi kendine bağlayarak alt kategori özelliğini ekliyoruz:
    ust_kategori = models.ForeignKey(
        'self', 
        on_delete=models.CASCADE, 
        null=True, 
        blank=True, 
        related_name='alt_kategoriler'
    )

    def __str__(self):
        return self.isim

class Yazi(models.Model):
    baslik = models.CharField(max_length=200)
    icerik = models.TextField()
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE)
    kayit_tarihi = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.baslik
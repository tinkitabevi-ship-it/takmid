from django.shortcuts import render, get_object_or_404  # 👈 get_object_or_404 EKLENDİ
from .models import Kategori, Yazi

def anasayfa(request):
    # Tüm ana kategorileri ve onların alt kategorilerini ve yazılarını TEK SORGULA çek
    kategoriler = Kategori.objects.filter(ust_kategori__isnull=True).prefetch_related(
        'alt_kategoriler__yazi_set'  # alt kategorilerin yazılarını da önceden yükle
    )
    # Son eklenen 5 yazıyı çek (Orta alan için)
    son_yazilar = Yazi.objects.all().order_by('-id')[:5]
    
    context = {
        'kategoriler': kategoriler,
        'son_yazilar': son_yazilar,
    }
    return render(request, 'icerik/anasayfa.html', context)


# 👇 BU FONKSİYONUN TAMAMINI EKLEYİN
def yazi_detay(request, id):
    yazi = get_object_or_404(Yazi, id=id)
    context = {
        'yazi': yazi,
    }
    return render(request, 'icerik/yazi_detay.html', context)
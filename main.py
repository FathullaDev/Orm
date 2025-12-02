'''
#1
filter() - malumotlarni berilgan shart bo'yicha saralab oladi.
Misol:
Category.objects.filter(id=5) id si 5 bo'lgan categorylar
News.objects.filter(id=5, views__gt=100) idsi 5 bo'lgan va vkorishlar soni 100dan ortiq bolgan
News.objects.filter(title__contains="news") title da news so'zi bolgan
News.objects.filter(title__icontains="news") title da news so'zi bolgan (katta kichik harflarni inobatga olmaydi)



'''
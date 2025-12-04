'''
#1
filter() - malumotlarni berilgan shart bo'yicha saralab oladi.
Misol:
Category.objects.filter(id=5) id si 5 bo'lgan categorylar
News.objects.filter(id=5, views__gt=100) idsi 5 bo'lgan va vkorishlar soni 100dan ortiq bolgan
News.objects.filter(title__contains="news") title da news so'zi bolgan
News.objects.filter(title__icontains="news") title da news so'zi bolgan (katta kichik harflarni inobatga olmaydi)

#2
exclude() - malumotlarni berilgan shartga mos kelmaydigani bo'yicha saralab oladi.
Category.objects.exclude(id__gt=1) 1 dan katta bo'lmaganlarni qaytaradi

#3
annotate() - natijaga qo'shimcha ustun qo'shish uchun ishlatiladi
Har bir categoryda nechta news borligini chiqarish uchun
Category.objects.annotate(total_news=Count("news"))

#4
alias() - annotate bilan bir xil, faqat vaqtincha nom berish uchun ishlatiladi
cat=Category.objects.annotate(total_news=Count("news"))
for i in cat:
    print(i.total_news)
har bir categoryda nechta news borligini chiqaradi

cat=Category.objects.alias(total_news=Count("news"))
for i in cat:
    print(i.total_news)
xatolik beradi

#5
order_by - saralash uchun
Category.objects.order_by('id') o'sish bo'yicha
Category.objects.order_by('-id') kamayish bo'yicha

#6
reverse() - Saralashni teskari qiladi.
Category.objects.order_by('id').reverse()

#7
distinct() - Dublikatlarni o'chiradi.
News.objects.values('title').distinct()

#8
values() - dictionary qaytadi
News.objects.values('title')

#9
values_list() - tuple qaytaradi
News.objects.values_list('title')

#10
dates() - Faqat sanalarni chiqaradi.
News.objects.dates('created_ed')

#11
datetimes() - vaqtlarni chiqaradi

#12
none() - bosh obyekt qaytaradi
News.objects.none()

#13
all() - barcha obyektlarni qaytaradi
News.objects.all()

#14
union() - Bir nechta querysetlarni birlashtirish
qs1 = News.objects.filter(is_bool=True)
qs2 = News.objects.filter(views__gt=100)
result = qs1.union(qs2)

#15

'''


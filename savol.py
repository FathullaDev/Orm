#1 filter
#2 annotate
#3 alias
#4 values_list
#5 difference()
#6 prefetch_realated()
#7 select_for_update()
#8 raw
#9 create
#10 get or create
#11 bulk_create()
#12 bulk_update()

'''
filter() - malumotlarni berilgan shart bo'yicha saralab oladi
News.objects.filter(id=5)

annotate() - jadvallarni birlashtirish uchun ishlatiladi
Har bir categoryda nechtadan new borligini chiqarish uchun
Category.objects.annotate(total_news=Count("news"))

alias() - annotate bilan bir xil faqat vaqtinchalik nom berish uhun ishlatiladi
Category.objects.alias(total_news=Count("news"))

values_list() - malumotlarni tuple da qaytaradi
News.objects.values_list('title')

difference() -

prefetch_related() - bitta jadvaldagi malumotga ikkinchi jadvaldagi malumotlarni bitta query bilan olib keladi
news = News.objects.all().prefetch_related('category')
har bir news yonidan categoryasi chiqadi

select_realeted()





'''
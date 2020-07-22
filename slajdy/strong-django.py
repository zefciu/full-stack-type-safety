b = Book.objects.get(id=1)
b.author = Publisher.objects.get(name='Chilton Books')

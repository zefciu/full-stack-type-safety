from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'


class Publisher(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self) -> str:
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=256)
    price = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    published_date = models.DateField()
    publisher = models.ForeignKey(
        Publisher,
        null=False,
        blank=False,
        on_delete=models.PROTECT,
    )
    author = models.ForeignKey(
        Author,
        null=True,
        blank=True,
        on_delete=models.PROTECT,
    )

    def __str__(self) -> str:
        return (
            f'{self.author.first_name} {self.author.last_name}: '
            f'{self.title}'
        )

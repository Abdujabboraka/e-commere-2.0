from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='nomi')
    slug = models.SlugField(max_length=100, unique=True)
    photo = models.ImageField(upload_to='Category-photos/', null=True, blank=True)
    parent = models.ForeignKey('self', on_delete=models.PROTECT, null=True, blank=True, verbose_name='sub-category')

    def __str__(self):
        if self.parent:
            return f"Sub: {self.name}"
        return self.name

    class Meta:
        verbose_name = 'Toifa'
        verbose_name_plural = 'Toifalar'



class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name='nomi')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='narxi')
    is_available = models.BooleanField(verbose_name='bormi')
    size = models.PositiveIntegerField(verbose_name='olchami')
    description = models.TextField(verbose_name='xaqida')
    card_details = models.TextField(verbose_name='card-details')
    shipping = models.TextField(verbose_name='shipping')

    def get_image(self):
        return Image.image

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Maxsulot'
        verbose_name_plural = 'Maxsulotlar'


class Image(models.Model):
    image = models.ImageField(upload_to='Product-images/', verbose_name='Rasmi')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Mahsulot')

    def __str__(self):
        return f"{self.product.name} | {self.image.name}"

    class Meta:
        verbose_name = 'Rasm'
        verbose_name_plural = 'Rasmlar'








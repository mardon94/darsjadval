from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel
from mptt.fields import TreeForeignKey

# Create your models here.

class Faculty(MPTTModel):
    parent = TreeForeignKey('self', blank=True,
                               related_name='children',
                               null=True,
                               on_delete=models.CASCADE)
    faculty = models.CharField(max_length=100)
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return self.faculty

    class MPTTMeta:
        order_insertion_by = ['faculty']

    def get_absolute_url(self):
        return reverse('faculty', kwargs={'slug': self.slug})

    def __str__(self):
        full_path = [self.faculty]
        k = self.parent
        while k is not None:
            full_path.append(k.faculty)
            k = k.parent
        return '/'.join(full_path[::-1])


class Time(models.Model):
    soat = models.CharField(max_length=50)

    def __str__(self):
        return self.soat


class Dars(models.Model):
    WEEK = (
        ('Dushanba', 'Dushanba'),
        ('Seshanba', 'Seshanba'),
        ('Chorshanba', 'Chorshanba'),
        ('Payshanba', 'Payshanba'),
        ('Juma', 'Juma'),
        ('Shanba', 'Shanba'),
    )

    yunalish = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    hafta = models.CharField(max_length=100, choices=WEEK)
    fan = models.CharField(max_length=200)
    room = models.CharField(max_length=100, null=True, blank=True)
    teacher = models.CharField(max_length=100, blank=True)
    guruh = models.CharField(max_length=100, blank=True)
    time = models.ForeignKey(Time, on_delete=models.CASCADE, null=True)
    zoom = models.CharField(max_length=800)

    def __str__(self):
        return self.fan





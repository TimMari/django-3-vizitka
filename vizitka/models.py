from django.db import models


class Info(models.Model):
    about = models.TextField('Информация про себя', blank=True)
    photo = models.ImageField('Фото', upload_to='vizitka/images/', blank=True)



class Links(models.Model):
    title = models.TextField('На что ссылка')
    extra = models.TextField('Дополнительная информация', blank=True)
    url = models.URLField('Ссылка')
    photo = models.ImageField( upload_to='vizitka/imgLink',blank=True)
    email = models.EmailField('Ваш Email', blank=True)


class Sertificate(models.Model):
    title = models.CharField('Название ', max_length=45)
    photo = models.ImageField(upload_to='vizitka/imgSert', blank=True)
    url = models.URLField('Ссылка', blank=True)

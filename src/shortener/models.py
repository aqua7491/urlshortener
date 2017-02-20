
from django.db import models
from .utils import create_shortcode
from django.conf import settings

from django_hosts.resolvers import reverse

from .validators import validate_url

SHORTCODE_MAX = getattr(settings, 'SHORTCODE_MAX', 15)


class KirrURLManager(models.Manager):
    def all(self, *args, **kwargs):
        return super(KirrURLManager, self).all(*args, **kwargs).filter(active=False)

    def refresh_shortcodes(self, items=100):
        qs = KirrURL.objects.filter(id__gte=1)
        if qs is not None and isinstance(items, int):
            qs = qs.order_by('-id')[:items]
        new_codes = 0
        for q in qs:
            q.shortcode = create_shortcode(q)
            print(q.id)
            q.save()
            new_codes += 1
        return "New codes made: {i}".format(i=new_codes)


class KirrURL(models.Model):
    ''' Model for url-shourtener'''
    url = models.CharField(max_length=220, validators=[validate_url])
    shortcode = models.CharField(max_length=SHORTCODE_MAX, unique=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    objects = KirrURLManager()
    # some_random = KirrURLManager()

    def save(self, *args, **kwargs):
        if self.shortcode is None or self.shortcode == "":
            self.shortcode = create_shortcode(self)
        super(KirrURL, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.url)

    def get_short_url(self):
        url_path = reverse('scode', kwargs={'shortcode': self.shortcode}, host='www', scheme='http')
        return url_path

from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse

class StaticViewSitemap(Sitemap):
    def items(self):
        return ['home', 'about', 'contact', 'faq', 'overview', 'privacy_policy', 'it_solutions']

    def location(self, item):
        return reverse(item)

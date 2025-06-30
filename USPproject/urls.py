from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.sitemaps.views import sitemap
from USPapp.sitemaps import StaticViewSitemap

# Sitemap configuration
sitemaps = {
    'static': StaticViewSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('USPapp.urls')),

    # ✅ Google Search Console verification file
    path('googled6d5880962e61c7c.html', TemplateView.as_view(
        template_name='googled6d5880962e61c7c.html',
        content_type='text/plain'
    )),

    # ✅ Sitemap (SEO)
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),

    # ✅ robots.txt (SEO)
    path('robots.txt', TemplateView.as_view(
        template_name='robots.txt',
        content_type='text/plain'
    )),
]

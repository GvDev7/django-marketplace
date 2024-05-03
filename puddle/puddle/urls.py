from django.contrib import admin
from django.urls import path, include
from core.views import index, contact
# Do not do the below code outside of development
from django.conf import settings
from django.conf.urls.static import static
# Do not do the above code outside of development


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index, name='index'),
    path('items/', include('item.urls')),
    path("contact/", contact, name= 'contact'),
    # Do not do the below code outside of dev
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # Do not do the above code outside of dev



from django.contrib import admin
from django.urls import path, include
# Do not do the below code outside of development
from django.conf import settings
from django.conf.urls.static import static
# Do not do the above code outside of development


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('core.urls')),
    path('items/', include('item.urls')),
    # Do not do the below code outside of dev
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # Do not do the above code outside of dev



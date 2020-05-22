from django.conf.urls import url
from basicapp import views

#TEMPLATE TAGGING
app_name = 'basicapp'#tells django tolook under the basicapp and find the url that matches
#^/basicapp/
urlpatterns = [
    #here, ^ means anything before relative, and $ means anything after relative
    url(r'^relative/$',views.relative,name='relative'),
    url(r'^other/$',views.other,name='other'),

]

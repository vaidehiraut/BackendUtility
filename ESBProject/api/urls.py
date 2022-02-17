from django.urls import path
from .views import SampleAPIView

urlpatterns = [
    # Function based api view
    # path('test/', sample_list),    
    # path('detail/<int:pk>/', sample_detail),

    # Class based api view
    # path('test/', SampleAPIView.as_view()),
    # path('detail/<int:id>/', SampleDetails.as_view()),

    # Generic API view
    # path('generic/test/<int:id>/', GenericAPIView.as_view()),
    # path('generic/test/', GenericAPIView.as_view()),


    path('test/', SampleAPIView.as_view()),

    


]
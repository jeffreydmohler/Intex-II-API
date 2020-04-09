"""intexapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from api import views
from django.conf.urls import url, include 
from django.contrib.auth.models import User 
from rest_framework import routers, serializers, viewsets # Serializers define the API representation. 
from api.models import Campaign, Update, Donation
from django.urls import include, path



# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

# Serializers define the API representation.
class CampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaign
        fields = [ 
            'id',
            'url',
            'campaign_id',
            'auto_fb_post_mode',
            'collected_date',
            'category_id',
            'category',
            'currencycode',
            'current_amount',
            'goal',
            'donators',
            'days_active',
            'days_created',
            'title',
            'description',
            'default_url',
            'has_beneficiary',
            'media_type',
            'project_type',
            'turn_off_donations',
            'user_id',
            'user_first_name',
            'user_last_name',
            'user_profile_url',
            'visible_in_search',
            'status',
            'deactivated',
            'state',
            'is_launched',
            'campaign_image_url',
            'created_at',
            'launch_date',
            'campaign_hearts',
            'social_share_total',
            'social_share_last_update',
            'location_city',
            'location_country',
            'location_zip',
            'is_charity',
            'charity_valid',
            'charity_npo_id',
            'charity_name',
            'velocity',
            'location_state',
            'current_amount_USD',
            'goal_USD',
            'percent_of_goal',
            'amount_per_donation',
            'percent_of_goal_score',
            'amt_per_donor_score',
            'success_score',
            ]

# Serializers define the API representation.
class UpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Update
        fields = [ 
            'id', 
            'campaign_id',
            'collected_date',
            'photo_url',
            'created_at',
            'updates_author',
            'updates_author_type',
            'updates_text',
            ]

# Serializers define the API representation.
class DonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donation
        fields = [ 
            'id', 
            'campaign_id',
            'collected_date',
            'amount',
            'is_offline',
            'is_anonymous',
            'name',
            'created_at',
            'profile_url',
            'verified',
            ]
# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'user', UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [ 
        path('campaign/', views.CampaignList.as_view()),
        path('campaign/<int:pk>/', views.CampaignDetail.as_view()),
        path('update/', views.UpdateList.as_view()),
        path('update/<int:pk>/', views.UpdateDetail.as_view()),
        path('donation/', views.DonationList.as_view()),
        path('donation/<int:pk>/', views.DonationDetail.as_view()),
        path('predict/', views.Predict.as_view()),
     ]
from . import views
from django.urls import path, re_path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny




schema_view = get_schema_view(
    openapi.Info(
        title="HeaderTop API",
        default_version="v1",
        description="API для управления HeaderTop объектами",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(AllowAny,),
)





urlpatterns = [
    path('',views.index,name='index'),
    path('meeting_details/',views.meeting_details,name='meeting_details'),
    path('meetings/',views.meetings,name='meetings'),
    path('admin/',views.baza_site,name='admin'),
    
    path('register/',views.register,name='register'),
    path('login/',views.user_login,name='login'),
    
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'), 
    

    # Header
    # Creat
    path('creat_header_top/',views.creat_header_top,name='creat_header_top'),
    path('creat_header_center/',views.creat_header_center,name='creat_header_center'),
    path('creat_header_end/',views.creat_header_end,name='creat_header_end'),   
    path('creat_header_slider/',views.creat_header_slider,name='creat_header_slider'),   
    # Update
    path('update_header_top/<int:head_id>/',views.update_header_top,name='update_header_top'),
    path('update_header_center/<int:head_id>/',views.update_header_center,name='update_header_center'),
    path('update_header_end/<int:head_id>/',views.update_header_end,name='update_header_end'),
    path('update_header_slider/<int:head_id>/',views.update_header_slider,name='update_header_slider'),
    # Delete
    path('delete_header_top/<int:head_id>/',views.delete_header_top,name='delete_header_top'),
    path('delete_header_center/<int:head_id>/',views.delete_header_center,name='delete_header_center'),
    path('delete_header_end/<int:head_id>/',views.delete_header_end,name='delete_header_end'),
    path('delete_header_slider/<int:head_id>/',views.delete_header_slider,name='delete_header_slider'),
    # End Header
    
    # Main One
    # Creat
    path('creat_main_one_top/',views.creat_main_one_top,name='creat_main_one_top'),
    path('creat_main_one_left/',views.creat_main_one_left,name='creat_main_one_left'),
    path('creat_main_one_right/',views.creat_main_one_right,name='creat_main_one_right'),   
    # Update
    path('update_main_one_top/<int:head_id>/',views.update_main_one_top,name='update_main_one_top'),
    path('update_main_one_left/<int:head_id>/',views.update_main_one_left,name='update_main_one_left'),
    path('update_main_one_right/<int:head_id>/',views.update_main_one_right,name='update_main_one_right'),
    # Delete
    path('delete_main_one_top/<int:head_id>/',views.delete_main_one_top,name='delete_main_one_top'),
    path('delete_main_one_left/<int:head_id>/',views.delete_main_one_left,name='delete_main_one_left'),
    path('delete_main_one_right/<int:head_id>/',views.delete_main_one_right,name='delete_main_one_right'),
    #End Main one
    
    # Main Two
    # Creat
    path('creat_main_two_left/',views.creat_main_two_left,name='creat_main_two_left'),
    path('creat_main_two_right/',views.creat_main_two_right,name='creat_main_two_right'),   
    # Update
    path('update_main_two_left/<int:head_id>/',views.update_main_two_left,name='update_main_two_left'),
    path('update_main_two_right/<int:head_id>/',views.update_main_two_right,name='update_main_two_right'),
    # Delete
    path('delete_main_two_left/<int:head_id>/',views.delete_main_two_left,name='delete_main_two_left'),
    path('delete_main_two_right/<int:head_id>/',views.delete_main_two_right,name='delete_main_two_right'),
    # Main Two End
    
    # Main Thee Start
    # Creat
    path('creat_main_thee_top/',views.creat_main_thee_top,name='creat_main_thee_top'),
    path('creat_main_thee_content/',views.creat_main_thee_content,name='creat_main_thee_content'),   
    # Update
    path('update_main_thee_top/<int:head_id>/',views.update_main_thee_top,name='update_main_thee_top'),
    path('update_main_thee_content/<int:head_id>/',views.update_main_thee_content,name='update_main_thee_content'),
    # Delete
    path('delete_main_thee_top/<int:head_id>/',views.delete_main_thee_top,name='delete_main_thee_top'),
    path('delete_main_thee_content/<int:head_id>/',views.delete_main_thee_content,name='delete_main_thee_content'),
    # Main Thee End
    
    # Main Four
    path('creat_main_four_top/',views.creat_main_four_top,name='creat_main_four_top'),
    path('creat_main_four_left/',views.creat_main_four_left,name='creat_main_four_left'),
    path('creat_main_four_right/',views.creat_main_four_right,name='creat_main_four_right'),   
    # Update
    path('update_main_four_top/<int:head_id>/',views.update_main_four_top,name='update_main_four_top'),
    path('update_main_four_left/<int:head_id>/',views.update_main_four_left,name='update_main_four_left'),
    path('update_main_four_right/<int:head_id>/',views.update_main_four_right,name='update_main_four_right'),
    # Delete
    path('delete_main_four_top/<int:head_id>/',views.delete_main_four_top,name='delete_main_four_top'),
    path('delete_main_four_left/<int:head_id>/',views.delete_main_four_left,name='delete_main_four_left'),
    path('delete_main_four_right/<int:head_id>/',views.delete_main_four_right,name='delete_main_four_right'),
    
    # Footer Start
    path('creat_footer/',views.creat_footer,name='creat_footer'),
    # Update
    path('update_footer/<int:head_id>/',views.update_footer,name='update_footer'),
    # Delete
    path('delete_footer/<int:head_id>/',views.delete_footer,name='delete_footer'),
    # Footer End
    
    # User Start
    path('creat_user/',views.creat_user,name='creat_user'),
    # Update
    path('update_user/<int:head_id>/',views.update_user,name='update_user'),
    # Delete
    path('delete_user/<int:head_id>/',views.delete_user,name='delete_user'),
    # User End
    
    # Meeting Details Start
    path('creat_meeting_details/',views.creat_meeting_details,name='creat_meeting_details'),
    # Update
    path('update_meeting_details/<int:head_id>/',views.update_meeting_details,name='update_meeting_details'),
    # Delete
    path('delete_meeting_details/<int:head_id>/',views.delete_meeting_details,name='delete_meeting_details'),
    # Meeting Details End
    
    # Meetings
    path('creat_meetings/',views.creat_meetings,name='creat_meetings'),
    # Update
    path('update_meetings/<int:head_id>/',views.update_meetings,name='update_meetings'),
    # Delete
    path('delete_meetings/<int:head_id>/',views.delete_meetings,name='delete_meetings'),
    # Meetings End
    
    
    
    
    # API Start
    
    # Header API Start
    path('api/header-top/', views.HeaderTopAPIView.as_view(), name='header_top_list_create'),
    path('api/header-top/<int:head_id>/', views.HeaderTopAPIView.as_view(), name='header_top_detail_update_delete'),
    
    path('api/header-center/', views.HeaderCenterAPIView.as_view(), name='header_center_list_create'),
    path('api/header-center/<int:head_id>/', views.HeaderCenterAPIView.as_view(), name='header_center_detail_update_delete'),
    
    path('api/header-end/', views.HeaderEndAPIView.as_view(), name='header_end_list_create'),
    path('api/header-end/<int:head_id>/', views.HeaderEndAPIView.as_view(), name='header_end_detail_update_delete'),
    
    path('api/header-slider/', views.HeaderSliderAPIView.as_view(), name='header_slider_list_create'),
    path('api/header-slider/<int:head_id>/', views.HeaderSliderAPIView.as_view(), name='header_slider_detail_update_delete'),
    
    # Header API End
    
    # Main One API Start
    
    path('api/main-one-top/', views.MainOneTopAPIView.as_view(), name='main_one_top_list_create'),
    path('api/main-one-top/<int:head_id>/', views.MainOneTopAPIView.as_view(), name='main_one_top_detail_update_delete'),
    
    path('api/main-one-left/', views.MainOneLeftAPIView.as_view(), name='main_one_left_list_create'),
    path('api/main-one-left/<int:head_id>/', views.MainOneLeftAPIView.as_view(), name='main_one_left_detail_update_delete'),
    
    path('api/main-one-right/', views.MainOneRightAPIView.as_view(), name='main_one_right_create'),
    path('api/main-one-right/<int:head_id>/', views.MainOneRightAPIView.as_view(), name='main_one_right_detail_update_delete'),
    
    # Main One API End
    
    # Main Two API Start
    
    path('api/main-two-left/', views.MainTwoLeftAPIView.as_view(), name='main_two_left_list_create'),
    path('api/main-two-left/<int:head_id>/', views.MainTwoLeftAPIView.as_view(), name='main_two_left_detail_update_delete'),
    
    path('api/main-two-right/', views.MainTwoRightAPIView.as_view(), name='main_two_left_right_create'),
    path('api/main-two-right/<int:head_id>/', views.MainTwoRightAPIView.as_view(), name='main_two_right_detail_update_delete'),
    
    # Main Two API End
    
    # Main Thee API Start
    
    path('api/main-thee-top/', views.MainTheeTopAPIView.as_view(), name='main_thee_top_list_create'),
    path('api/main-thee-top/<int:head_id>/', views.MainTheeTopAPIView.as_view(), name='main_thee_top_detail_update_delete'),
    
    path('api/main-thee-content/', views.MainTheeContentAPIView.as_view(), name='main_thee_content_create'),
    path('api/main-thee-content/<int:head_id>/', views.MainTheeContentAPIView.as_view(), name='main_thee_content_detail_update_delete'),
    
    # Main Thee API End
    
    # Main Four API Start
    
    path('api/main-four-top/', views.MainFourTopAPIView.as_view(), name='main_four_top_list_create'),
    path('api/main-four-top/<int:head_id>/', views.MainFourTopAPIView.as_view(), name='main_four_top_detail_update_delete'),
    
    path('api/main-four-left/', views.MainFourLeftAPIView.as_view(), name='main_four_left_list_create'),
    path('api/main-four-left/<int:head_id>/', views.MainFourLeftAPIView.as_view(), name='main_four_left_detail_update_delete'),
    
    path('api/main-four-right/', views.MainFourRightAPIView.as_view(), name='main_four_right_create'),
    path('api/main-four-right/<int:head_id>/', views.MainFourRightAPIView.as_view(), name='main_four_right_detail_update_delete'),
    
    # Main Four API End
    
    # Footer API Start
    
    path('api/footer/', views.FooterAPIView.as_view(), name='footer_list_create'),
    path('api/footer/<int:head_id>/', views.FooterAPIView.as_view(), name='footer_detail_update_delete'),
    
    # Footer API End
    
    # API End
    
]

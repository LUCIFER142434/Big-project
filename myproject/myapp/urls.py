from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('admin/',views.admin,name='admin'),
    path('meeting_details/',views.meeting_details,name='meeting_details'),
    path('meetings/',views.meetings,name='meetings'),
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
]

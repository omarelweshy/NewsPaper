from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('<slug:slug>/', CategoryReportsView.as_view(), name='categories_reports'),
    path('report/<uuid:pk>/', ReportDetailView.as_view(), name='report_detail'),
    path('report/create/', CreateReportView.as_view(), name='create_report'),
    path('report/<uuid:pk>/update/', UpdateReportView.as_view(), name='update_report'),
    path('report/<uuid:pk>/delete/', DeleteReportView.as_view(), name='delete_report'),

]

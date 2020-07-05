from django.views.generic import *
from news.models import *
from categories.models import *
from news.forms import *
from django.urls import reverse, reverse_lazy

class HomePageView(TemplateView):
    model = Report
    template_name = 'home.html'
    context_object_name = 'report_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories_list'] = Categories.objects.all()
        return context

class CategoryReportsView(DetailView):
    model = Categories
    template_name = "category_reports_list.html"
    context_object_name = 'category'

class ReportDetailView(DetailView):
    model = Report
    template_name = "report_detail.html"
    context_object_name = 'report'

class CreateReportView(CreateView):
    model = Report
    form_class = CreateReportForm
    template_name = "forms/create_report.html"

class UpdateReportView(UpdateView):
    model = Report
    form_class = CreateReportForm
    template_name = "forms/update_report.html"
    context_object_name = 'report'

class DeleteReportView(DeleteView):
    model = Report
    form_class = CreateReportForm
    template_name = "forms/delete_report.html"
    context_object_name = 'report'
    success_url = reverse_lazy('home')
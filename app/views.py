from django.shortcuts import render
from django.views.generic import ListView

from app.models import IELTS
# Create your views here.

class IELTSViews(ListView):
    model = IELTS
    template_name = "index.html"
    context_object_name = "IELTS"
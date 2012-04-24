# -*-coding: utf-8-*-
from start.models import IndexPage
from works.models import Work
from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response, get_object_or_404

def index(request):
    return render_to_response('index.html', {
        'indexpage' : IndexPage.objects.all(),
        'works' : Work.objects.all()[:1],
    })
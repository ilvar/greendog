# -*-coding: utf-8-*-
from works.models import Work
from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response, get_object_or_404
from endless_pagination.decorators import page_template
from django.template import RequestContext

@page_template("archive_page.html")
def works(request, extra_context=None):
    context = {
        'works' : Work.objects.filter(arch=False),
    }
    if extra_context is not None:
        context.update(extra_context)
    return render_to_response('works.html', context, context_instance=RequestContext(request))

def view_work(request, slug):
    return render_to_response('work.html', {
        'work' : get_object_or_404(Work, slug=slug),
        # 'work' : Work.objects.all(),
    })
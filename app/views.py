from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from app.models import *
from app.ajax import *

# Create your views here.


def index(request):
	ctx = {}
	query = request.GET.get('query', None)
	if query and query != '':
		ctx['query'] = query

		# q = Q(number=query) | Q(name__contains=query)
		q = Q(name__contains=query)
		# fixes = Fix.objects.filter(q).order_by('name')
		moviles = list(Movil.objects.filter(q).order_by('name'))
		# objs = fixes + moviles
		objs = moviles

		paginator = Paginator(objs,10)
		page = request.GET.get('page')
		try:
			result = paginator.page(page)
		except PageNotAnInteger:
			result = paginator.page(1)
		except EmptyPage:
			result = paginator.page(paginator.num_pages)

		ctx['result'] = result
		ctx['count'] = objs.count

	return render(request, 'app/index.html',ctx)
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template.loader import get_template
from django.template import Context
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from app.models import *

def ajax_search(request):
	query = request.GET.get('query', None)
	json = {}
	html = ''
	if query and query != '':

		q = Q(name__contains=query)
		# fixes = list(Fix.objects.filter(q).order_by('name'))
		# objs = Fix.objects.filter(q).order_by('name')
		moviles = list(Movil.objects.filter(q).order_by('name'))
		objs = moviles

		paginator = Paginator(objs,10)
		page = request.GET.get('page')
		try:
			result = paginator.page(page)
		except PageNotAnInteger:
			result = paginator.page(1)
		except EmptyPage:
			result = paginator.page(paginator.num_pages)

		template = get_template('app/item.html')
		for item in result:
			ctx = {'item':item}
			context = Context(ctx)
			html += template.render(context)

		json['total_items'] = objs.count()
		json['table_content'] = html
		json['total_pages'] = paginator.num_pages
		json['current_page'] = result.number
		json['result_query'] = query

	return JsonResponse(json)
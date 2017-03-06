var results_table = $('#results_table');

var a_back = $('#a_back');
var a_next = $('#a_next');

var q = escape($('#query').val());
var a_search = $('#a_search');
var a_form = $('#a_form');

var total_items = $('#total_items');
var result_query = $('#result_query');
var table_content = $('#table_content');
var current_page = $('#current_page');
var total_pages = $('#total_pages');

var page = 1

function get_and_load(table_content, url, page){
	var img_loading = $('#img_loading');
	$.ajax({
		url: url,
		type: 'GET',
		dataType: 'json',
		beforeSend: function(){
			img_loading.show();
		}
	})
	.done(function(data) {
		console.log("success");
		results_table.show();

		total_items.text(data.total_items);
		result_query.text(data.result_query);
		table_content.html(data.table_content);
		current_page.text(data.current_page);
		total_pages.text(data.total_pages);

		show_or_hide(parseInt(data.current_page), parseInt(data.total_pages))
		img_loading.hide();
	})
	.fail(function(data) {
		console.log("error");
		results_table.hide();
	})
	.always(function(data) {
		console.log("complete");
	});

}

function show_or_hide(page, total){
	a_back.hide();
	a_next.hide();

	if(page > 1){
		a_back.show();
	}
	if(page < total){
		a_next.show();
	}
}


$(document).ready(function() {
	a_form.on('submit', function(){
		q = escape($('#query').val());
		page = 1;
		var url = '/ajax_search/?query='+q+'&page='+page;
		console.log(url);
		get_and_load(table_content, url, page)
		return false;
	});

	a_back.on('click', function(){
		q = escape($('#query').val());
		page--;
		var url = '/ajax_search/?query='+q+'&page='+page;
		console.log(url);
		get_and_load(table_content, url, page)
	});

	
	a_next.on('click', function(){
		q = escape($('#query').val());
		page++;
		var url = '/ajax_search/?query='+q+'&page='+page;
		console.log(url);
		get_and_load(table_content, url, page);
	});
});

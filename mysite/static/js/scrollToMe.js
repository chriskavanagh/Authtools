//uses scrollTo plugin to scroll from Home (in Nav) to #target in footer.


$(function(){
    $('#home').click(function() {
		$.scrollTo($('#target'), 2000);
	});
 });
/* Kingdom Come Script File */


/* Fade out title on click */
$(document).ready(function(){
	$(".kingdomcome").one('click', function(){
		$("#back").fadeOut(1000, function() {
			$(this).css('background', 'linear-gradient(to right, rgba(0,0,0,1) 0%,rgba(0,0,0,0) 30%,rgba(0,0,0,0) 70%,rgba(0,0,0,1) 100%').fadeIn('3000');
			$(".kingdomcome").fadeOut(1000, function(){
				$(".kingdomtitle").append("Kingdom Come<hr>");
				$(".kingdomtitle").fadeIn(1000);
				//$("body").append("<hr>");
			});
		});
	});
});
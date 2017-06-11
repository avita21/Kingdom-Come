/* Kingdom Come Script File */

/* CONSTANTS: */
var TITLEFADE = 1000;

/* Fade out title on click */
$(document).ready(function(){
	/* Detect if on desktop: */
	var isDesktop = window.matchMedia("only screen and (min-device-width: 600px)");
	$(".kingdomcome").one('click', function(){
		$("#back").fadeOut(TITLEFADE, function() {
			/* add faded black background if not on mobile: */
			if (isDesktop.matches) {
				$(this).css('background', 
				'linear-gradient(to right, rgba(0,0,0,1) 0%,rgba(0,0,0,0) 20%,rgba(0,0,0,0) 80%,rgba(0,0,0,1) 100%').fadeIn('3000');
			}
			/* fade the titles, story, and pictures: */
			$(".kingdomcome").fadeOut(TITLEFADE, function(){
				$(".kingdomtitle").hide();
				$(".kingdomtitle").append("Kingdom Come<hr>");
				$(".kingdomtitle").fadeIn(TITLEFADE);
	
				$("#narrative").hide();
				/* BEGIN THE GAME: */
				kingdom_come();
			});
		});
	});
});


/* 
   ######################################################
		BEGINNING THE NARRATIVE - XML PARSING
	####################################################
*/

function kingdom_come(){
	var xhttp = new XMLHttpRequest();
	xhttp.onreadystatechange = function() {
	    if (this.readyState == 4 && this.status == 200) {
	        begin_narrative(this);
	    }
	};
	xhttp.open("GET", "KingdomCome.xml", true);
	xhttp.send();
}

function begin_narrative(xml) {
	xmlDoc = xml.responseXML;
	txt = xmlDoc.getElementsByTagName("beginning")[0].childNodes[0];
	document.getElementById("narrative").innerHTML = txt.nodeValue;
	/* FIRST TEXT ANIMATION!!!! */
	$('#narrative').fadeIn(TITLEFADE * 3);
}
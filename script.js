/* Kingdom Come Script File */


/* Fade out title on click */
$(document).ready(function(){
	/* Detect if on desktop: */
	var isDesktop = window.matchMedia("only screen and (min-width: 600px)");
	$(".kingdomcome").one('click', function(){
		$("#back").fadeOut(1000, function() {
			/* add faded black background if not on mobile: */
			if (isDesktop.matches) {
				$(this).css('background', 
				'linear-gradient(to right, rgba(0,0,0,1) 0%,rgba(0,0,0,0) 20%,rgba(0,0,0,0) 80%,rgba(0,0,0,1) 100%').fadeIn('3000');
			}
			/* fade the titles */
			$(".kingdomcome").fadeOut(1000, function(){
				$(".kingdomtitle").hide();
				$(".kingdomtitle").append("Kingdom Come<hr>");
				$(".kingdomtitle").fadeIn(1000);
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
	var x, i, txt;
	txt = "";
    x = xmlDoc.documentElement.childNodes;
    for (i = 0; i < x.length; i++) { 
        if (x[i].nodeType == 1) {
            txt += x[i].nodeName + "<br>";
        }
    }
	document.getElementById("narrative").innerHTML = txt;
}
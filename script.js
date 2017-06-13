/* Kingdom Come Script File */

/* CONSTANTS: */
var DEFAULTFADE = 1000;

/* Fade out title on click */
$(document).ready(function(){
	/* Detect if on desktop: */
	var isDesktop = window.matchMedia("only screen and (min-device-width: 600px)");
	$(".kingdomcome").one('click', function(){
		$("#back").fadeOut(DEFAULTFADE, function(){
			/* add faded black background if not on mobile: */
			if (isDesktop.matches) {
				$(this).css('background', 
				'linear-gradient(to right, rgba(0,0,0,1) 0%,rgba(0,0,0,0) 20%,rgba(0,0,0,0) 80%,rgba(0,0,0,1) 100%').fadeIn('3000');
			}
			/* fade the titles, story, and pictures: */
			$(".kingdomcome").fadeOut(DEFAULTFADE, function(){
				$(".kingdomtitle").hide();
				$(".kingdomtitle").append("Kingdom Come<hr>");
				$(".kingdomtitle").fadeIn(DEFAULTFADE);
				/* Add gradient to bottom */
				$("body").append("<div class='bottom'></div>");

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
	var xmlDoc = xml.responseXML;
	var txt = xmlDoc.getElementsByTagName("beginning")[0].childNodes[0];
	document.getElementById("narrative").innerHTML = txt.nodeValue;
	/* FIRST TEXT ANIMATION!!!! */
	$('#narrative').fadeIn(DEFAULTFADE * 3, function(){ 
		var x = xmlDoc.getElementsByTagName("decision")[0];
		var choices = x.getElementsByTagName('choice'); 
		txt = "<p></p>";
		/* array of the next story, based on choice: */
		var next = [open_letter, wait_for_friends];  
		for (i = 0; i < choices.length; i++) {
			txt += "<div class='choice'>"+choices[i].firstChild.nodeValue+"</div><p></p>"
		}
		$('#narrative').append(txt);
		$(".choice").fadeIn(DEFAULTFADE, function(){
			$(".choice").each(function(index, obj){
				$(obj).one('click', function(){
					var color    = new RGBColor($(this).css('background-color'));
					$(obj).animate({
						color: jQuery.Color('#FFF'),
						boxShadow: "0 0 50px 30px rgba(100,100,200,0.4)",
						opacity: 0}, 
						{duration: DEFAULTFADE*2,
						complete: function(){
									$(".choice").hide();
									console.log(index);
									return;
								} 
						});
					$(".choice").animate({opacity: 0}, {duration: DEFAULTFADE});
				}).delay(DEFAULTFADE*2).promise().then(next[index](xmlDoc));
			});
		});
	});
}

function open_letter(xml){
	console.log('open the letter');
	$('#narrative').append(xml.getElementsByTagName('openLetter')[0].childNodes[0].nodeValue);
}

function wait_for_friends(xml){
	console.log('waiting for friends');
	$('#narrative').append(xml.getElementsByTagName('letter')[0].childNodes[0].nodeValue);
}
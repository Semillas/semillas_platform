function reset() {
	$._pos=null;
}
function resetMap () {
	document.getElementById("mapholder").innerHTML = "";
}
function getLocation() {
	$.pos(
		function(position){
			var latlon = position.coords.latitude + "," + position.coords.longitude;
			var img_url = "http://maps.googleapis.com/maps/api/staticmap?center="+latlon+"&zoom=14&size=400x300&sensor=false";
			document.getElementById("mapholder").innerHTML = "<img src='"+img_url+"'>";
		},
		function(error){
			var x = document.getElementById("demo");
			if (error.UNSUPPORTED) {
				x.innerHTML = "Geolocation is not supported by this browser.";
				return;
			}
			switch(error.code) {
				case error.PERMISSION_DENIED:
				    x.innerHTML = "User denied the request for Geolocation.";
				    break;
				case error.POSITION_UNAVAILABLE:
				    x.innerHTML = "Location information is unavailable.";
				    break;
				case error.TIMEOUT:
				    x.innerHTML = "The request to get user location timed out.";
				    break;
				case error.UNKNOWN_ERROR:
				    x.innerHTML = "An unknown error occurred.";
				    break;
			}
		}
	);
}
function getLocation2() {
	alert(JSON.stringify($.pos()));
}

function getLocation3() {
	$.pos(
		function() {
			alert("OK");
		},function() {
			alert("KO");
		}
	);
}

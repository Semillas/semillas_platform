/* Project specific Javascript goes here. */

/* Up button JS */

var amountScrolled = 300;

$(window).scroll(function() {
	if ( $(window).scrollTop() > amountScrolled ) {
		$('a.back-to-top').fadeIn('slow');
	} else {
		$('a.back-to-top').fadeOut('slow');
	}
});

$('a.back-to-top').click(function() {
	$('html, body').animate({
		scrollTop: 0
	}, 700);
	return false;
});

/* Get location */

$.pos=function(showPosition,showError){
	if (!this._pos) {
		if (!navigator.geolocation) {
			this._pos={UNSUPPORTED:true}
			if (showError) showError(this._pos);
		} else {
			this._pos={ASKING: true};
			var _showPosition=function(position) {
				$._pos=position;
				if (showPosition) showPosition.apply(this,arguments);
			};
			var _showError=function(error) {
				$._pos=error;
				if (showError) showError.apply(this,arguments);
			};
			navigator.geolocation.getCurrentPosition(_showPosition, _showError);
		}
	} else {
		if (showPosition && this._pos.coords) showPosition(this._pos);
		else if (showError) showError(this._pos)
	}
	return this._pos;
};



        
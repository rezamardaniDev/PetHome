$(document).ready(function () {
    var coll = document.getElementsByClassName("collapsible");
    var i;

    for (i = 0; i < coll.length; i++) {
        coll[i].addEventListener("click", function () {
            this.classList.toggle("active");
            var content = this.nextElementSibling;
            if (content.style.maxHeight) {
                content.style.maxHeight = null;
            } else {
                content.style.maxHeight = content.scrollHeight + "px";
            }
        });
    }

});



(function ($) {
	$.fn.countTo = function (options) {
		options = options || {};
		
		return $(this).each(function () {
			// set options for current element
			var settings = $.extend({}, $.fn.countTo.defaults, {
				from:            $(this).data('from'),
				to:              $(this).data('to'),
				speed:           $(this).data('speed'),
				refreshInterval: $(this).data('refresh-interval'),
				decimals:        $(this).data('decimals')
			}, options);
			
			// how many times to update the value, and how much to increment the value on each update
			var loops = Math.ceil(settings.speed / settings.refreshInterval),
				increment = (settings.to - settings.from) / loops;
			
			// references & variables that will change with each update
			var self = this,
				$self = $(this),
				loopCount = 0,
				value = settings.from,
				data = $self.data('countTo') || {};
			
			$self.data('countTo', data);
			
			// if an existing interval can be found, clear it first
			if (data.interval) {
				clearInterval(data.interval);
			}
			data.interval = setInterval(updateTimer, settings.refreshInterval);
			
			// initialize the element with the starting value
			render(value);
			
			function updateTimer() {
				value += increment;
				loopCount++;
				
				render(value);
				
				if (typeof(settings.onUpdate) == 'function') {
					settings.onUpdate.call(self, value);
				}
				
				if (loopCount >= loops) {
					// remove the interval
					$self.removeData('countTo');
					clearInterval(data.interval);
					value = settings.to;
					
					if (typeof(settings.onComplete) == 'function') {
						settings.onComplete.call(self, value);
					}
				}
			}
			
			function render(value) {
				var formattedValue = settings.formatter.call(self, value, settings);
				$self.html(formattedValue);
			}
		});
	};
	
	$.fn.countTo.defaults = {
		from: 0,               // the number the element should start at
		to: 0,                 // the number the element should end at
		speed: 1000,           // how long it should take to count between the target numbers
		refreshInterval: 100,  // how often the element should be updated
		decimals: 0,           // the number of decimal places to show
		formatter: formatter,  // handler for formatting the value before rendering
		onUpdate: null,        // callback method for every time the element is updated
		onComplete: null       // callback method for when the element finishes updating
	};
	
	function formatter(value, settings) {
		return value.toFixed(settings.decimals);
	}
}(jQuery));

jQuery(function ($) {
  // custom formatting example
  $('.count-number').data('countToOptions', {
	formatter: function (value, options) {
	  return value.toFixed(options.decimals).replace(/\B(?=(?:\d{3})+(?!\d))/g, ',');
	}
  });
  
  // start all the timers
  $('.timer').each(count);  
  
  function count(options) {
	var $this = $(this);
	options = $.extend({}, options || {}, $this.data('countToOptions') || {});
	$this.countTo(options);
  }
});



    $(document).ready(function(){

        var quantitiy=0;
           $('.quantity-right-plus').click(function(e){
                
                // Stop acting like a button
                e.preventDefault();
                // Get the field name
                var quantity = parseInt($('#quantity').val());
                
                // If is not undefined
                    
                    $('#quantity').val(quantity + 1);
        
                  
                    // Increment
                
            });
        
             $('.quantity-left-minus').click(function(e){
                // Stop acting like a button
                e.preventDefault();
                // Get the field name
                var quantity = parseInt($('#quantity').val());
                
                // If is not undefined
              
                    // Increment
                    if(quantity>0){
                    $('#quantity').val(quantity - 1);
                    }
            });
            
        });
    


function mainslider() {
    jQuery('#owl-mainslider').owlCarousel({
        items: 1,
        nav: false,
        dots:true,
        autoplay: true,
        loop: true,
        mouseDrag: true,
        touchDrag: true,
        autoplayHoverPause: true,
        smartSpeed: 1500,
        autoplayTimeout: 5000,
    });
}



function owlproduct() {
    jQuery('.owl-product').owlCarousel({
        rtl: true,
        loop: true,
        dots:true,
        autoplay: true,
        autoplayHoverPause: true,
        smartSpeed: 1500,
        autoplayTimeout: 8000,
        responsiveClass: true,
        responsive: {
            0: {
                items: 1,
            },
            490: {
                items: 2,
            },
            577: {
                items: 3,
            },
            769: {
                items: 4,
            },
            1200: {
                items: 4,
            }
        }
    });
}



function owlproduct_page() {
    jQuery('.owl-product-page').owlCarousel({
        rtl: true,
        loop: true,
        dots:true,
        autoplay: true,
        autoplayHoverPause: true,
        smartSpeed: 1500,
        autoplayTimeout: 8000,
        responsiveClass: true,
        responsive: {
            0: {
                items: 1,
            },
            490: {
                items: 1,
            },
            577: {
                items: 1,
            },
            769: {
                items: 1,
            },
            1200: {
                items: 1,
            }
        }
    });
}



function owlStory() {
    jQuery('#owl-Story').owlCarousel({
        items:1,
        rtl: true,
        loop: true,
        dots: true,
        nav: false,
        autoplay: true,
        autoplayHoverPause: true,
        smartSpeed: 1300,
        autoplayTimeout: 5000,
        });
}



$(document).ready(function () {

    mainslider(),
    owlproduct(),
    owlStory(),
    owlproduct_page();

});
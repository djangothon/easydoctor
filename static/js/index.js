app = angular.module("index", []);
app.controller("mainCtrl", [ '$http', '$location', function (server, navigate) {
        var self = this;
        self.test = "hi";
        self.signIn = function (argument) {
        	//console.log("User : "+self.user.emailId+" and "+self.user.category);
        	self.param = {
                method : 'POST',
                url : 'portal/verify/',
                data : self.user
            };
            server(self.param).then(function (response) {
            	self.response = response.data;
            }, function (errorResponse) {
                console.log(errorResponse);
            });
        }
}]);
$(document).ready(function(){
	
	$("#loginpopup").bind("click", function() {
		$('#login').modal('toggle');
	});
	
	 $('#signup-link').bind("click", function() {
	    $('#login').modal('hide');
	     $('#signup').modal('toggle');
	 });
	 $('#login-link').bind("click", function() {
	    $('#signup').modal('hide');
	     $('#login').modal('toggle');
	 });
	 
	 // Boostrap Slider
	 $('.carousel').carousel();
	 
			// navigation click actions	
			$('.scroll-link').on('click', function(event){
				event.preventDefault();
				var sectionID = $(this).attr("data-id");
				scrollToID('#' + sectionID, 750);
				$('.navbar-nav li').each(function(){
					$(this).removeClass("active");
				});
				$(this).parent().addClass("active");
			});
			// scroll to top action
			$('.scroll-top').on('click', function(event) {
				event.preventDefault();
				$('html, body').animate({scrollTop:0}, 'slow'); 		
			});
			// mobile nav toggle
			$('#nav-toggle').on('click', function (event) {
				event.preventDefault();
				$('#main-nav').toggleClass("open");
			});
		
		// scroll function
		function scrollToID(id, speed){
			var offSet = 50;
			var targetOffset = $(id).offset().top - offSet;
			var mainNav = $('#main-nav');
			$('html,body').animate({scrollTop:targetOffset}, speed);
			if (mainNav.hasClass("open")) {
				mainNav.css("height", "1px").removeClass("in").addClass("collapse");
				mainNav.removeClass("open");
			}
		}
		if (typeof console === "undefined") {
		    console = {
		        log: function() { }
		    };
		}
	 
})

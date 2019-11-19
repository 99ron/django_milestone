/*global $ */

// This shows a basic prompt to whether the user wants to go ahead with their decision.
$(document).on('click', '.confirm-delete', function(){
    return confirm('Are you sure you want to delete this?');
});

// Function for scroll to top. Fades in when greater than 100px from the top.
$(window).scroll(function(){ 
    if ($(this).scrollTop() > 100) { 
        $('#scroll').fadeIn(); 
    } else { 
        $('#scroll').fadeOut(); 
    } 
}); 

// Once button is clicked it'll scroll to the top.
$('#scroll').click(function(){ 
    $("html, body").animate({ scrollTop: 0 }, 600); 
    return false; 
});

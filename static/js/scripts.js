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



// This function changes the text between 'More Options' and 'Show Less'.
function ShowMoreChange(id) {
    if(id == "ShowMoreOptional") {
       let SMO = document.getElementById('ShowMoreOptional');
        if (SMO.innerHTML == "More Options") { 
            SMO.innerHTML ="Show Less"; 
        } else { 
            SMO.innerHTML = "More Options"; 
        }
    }
    
    // This is for the damage container on the quotes and edit pages.
    if(id == "ShowMoreDamage") {
        let SMD = document.getElementById('ShowMoreDamage');
        if (SMD.innerHTML == "More Options") { 
            SMD.innerHTML ="Show Less"; 
        } else { 
            SMD.innerHTML = "More Options"; 
        }
    }
    
    // This is for the orders page.
    if(id == "ShowMoreOrder") {
        let SMO = document.getElementById('ShowMoreOrder');
        if (SMO.innerHTML == "Show More") { 
            SMO.innerHTML ="Show Less"; 
        } else { 
            SMO.innerHTML = "Show More"; 
        }
    }
}



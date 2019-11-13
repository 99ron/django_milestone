/*global $ */

// This shows a basic prompt to whether the user wants to go ahead with their decision.
$(document).on('click', '.confirm-delete', function(){
    return confirm('Are you sure you want to delete this?');
});


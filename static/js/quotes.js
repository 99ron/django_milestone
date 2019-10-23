/* global $ */

let tos, os, totalPrice;

// Hides all the containers until options are selected.
$("#wrap-colour-container").hide();
$("#optional-service-container").hide();
$("#damage-container").hide();
$("#make-model-container").hide(); 
$("#price-container").hide();

// Updates the image on the quotes page to show vehicle sizing which also hides or show's certain div's depending on choosen option.
$('#type-of-service').change(function(){
    var dropdown = this.value;
    
    // Changes the image and fades in the needed containers.
    if(dropdown=="1") {
        $("#service-image").html( "<img class='img-responsive' src='/media/quotes/Large_veh.jpg'>");
        $("#wrap-colour-container").fadeIn();
        $("#optional-service-container").fadeIn();
        $("#damage-container").fadeIn();
        $("#make-model-container").fadeIn(); 
        $("#price-container").fadeIn();
    }
    
    // Changes the image and fades in the needed containers.
    if(dropdown=="2") {
        $("#service-image").html( "<img class='img-responsive' src='/media/quotes/Mid_veh.jpg'>");
        $("#wrap-colour-container").fadeIn();
        $("#optional-service-container").fadeIn();
        $("#damage-container").fadeIn();
        $("#make-model-container").fadeIn(); 
        $("#price-container").fadeIn();
    }
    
    // Changes the image and fades in the needed containers.    
    if(dropdown=="3") {
        $("#service-image").html( "<img class='img-responsive' src='/media/quotes/Small_veh.jpg'>");
        $("#wrap-colour-container").fadeIn();
        $("#optional-service-container").fadeIn();
        $("#damage-container").fadeIn();
        $("#make-model-container").fadeIn(); 
        $("#price-container").fadeIn();
    }
    
    // Changes the image and fades in/out the needed containers.
    if(dropdown=="4") {
        $("#service-image").html( "<img class='img-responsive' src='/media/quotes/bonnet_wrap.jpg'>");
        $("#wrap-colour-container").fadeIn();
        $("#optional-service-container").fadeOut();
        $("#damage-container").fadeOut();
        $("#make-model-container").fadeIn(); 
        $("#price-container").fadeIn();
    }
 });


// This will read what the price is for the selected items and then add it to show a total before processing.

$('#type-of-service').change(function() {
    tos = $(this).children(":selected").data("price");
    return tos;
});

/*
Checks if the checkbox for the optional services on the quotes page have been
toggled and if so the price gets extracted and returned for the live update
on price. 
*/
 
$('.optional-services').change(function() {
let osArray = $('.optional-services:checked').map(function() {
    return $(this).data('price');
}).get();

// This converts the array to be int.
osArray = osArray.map(Number);

// This takes 2 of the numbers from the conversion and adds them together
// ready to display in the total cost box and if no numbers are found it defaults to 0.
os = osArray.reduce(function(a,b){
    return a+b}, 0);
});


// This function checks and updates the total price every second.
$(function(){
    setInterval(priceCheckerFunction, 1000);
});

// Checks to see what checkboxes are selected and add's the price to the total, with a few checks.
function priceCheckerFunction() {
    if (tos > 0) {
        if (os > 0) {
            totalPrice = parseInt(tos) + parseInt(os);
            $(".total-price").val(totalPrice); 
        } else {
            totalPrice = tos;
            $(".total-price").val(totalPrice); 
        }
    } else {
        totalPrice = 0;
        $(".total-price").val(totalPrice); 
    }
}

// This allows the row to be clicked on oppose to just the text or image.
$('.table tbody tr').click(function(event) {
    if (event.target.type !== 'radio') {
    $(':radio', this).trigger('click');
  }
});

// This targets the table and adds the class to the selected cell while removing it from the others. 
$('#quotes-table tr').click(function () {
    $(this).find('td input:radio').prop('checked', true);
    $('#quotes-table tr').removeClass("blue-cell-white-text");
    $(this).addClass("blue-cell-white-text");
});
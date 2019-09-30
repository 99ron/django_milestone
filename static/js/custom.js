/* global $ */

let tos, os;

// Updates the image on the quotes page to show vehicle sizing.
$('#type-of-service').change(function(){
    var dropdown = this.value;

    if(dropdown=="1") {
        $("#service-image").html( "<img class='img-responsive' src='/media/quotes/Large_veh.jpg'>");

    }
    if(dropdown=="2") {
        $("#service-image").html( "<img class='img-responsive' src='/media/quotes/Mid_veh.jpg'>");
    }
        
    if(dropdown=="3") {
        $("#service-image").html( "<img class='img-responsive' src='/media/quotes/Small_veh.jpg'>");
    }
 });


// This will read what the price is for the selected items and then add it to show a total before processing.



$('#type-of-service').change(function() {
    tos = $(this).children(":selected").data("price");
    return tos;
});

// Checks if the checkbox for the optional services on the quotes page have been
// toggled and if so the price gets extracted and returned for the live update
// on price.
$('.optional-services').change(function() {
let osArray = $('.optional-services:checked').map(function() {
    return $(this).data('price');
}).get();

// This converts the array to be int.
osArray = osArray.map(Number);

// This takes 2 of the numbers from the conversion and adds them together
// ready to be display in the total cost box.
os = osArray.reduce(function(a,b){
    return a+b}, 0);
});



$(function(){
    setInterval(priceCheckerFunction, 1000);
});

function priceCheckerFunction() {
  $(".total-price").html('£' + os);  
}

/* global $ */

let tos, os, totalPrice, dropdown, car_make;

// Upon page loading this checks what the value is of the service dropdown to dictate what's shown on the screen.
$( document ).ready(function() {
    dropdown = $("#type-of-service option:selected").val();
    
    // If the option is set the default "select an option" it will hide everything bar the service option.
    if (dropdown ==  "0"  ) {

        $("#wrap-colour-container").hide();
        $("#optional-service-container").hide();
        $("#damage-container").hide();
        $("#make-model-container").hide(); 
        $("#price-container").hide();
        
    } else if (dropdown == "4") {
        // If option 4 (bonnet wrap) is chosen it hides the optional extras as they're not needed.
        $("#optional-service-container").hide();    
        
    } else {
       // Any of the other options is selected the optional extras are displayed. 
       $("#optional-service-container").fadeIn(); 
    } 
    
    
    // This renders the list of models if there's an option selected for the car model. Ie. The Edit page.
    car_make = $('select[name=car_make] option:selected').val();
    var request_url = 'https://vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMake/' + car_make + '?format=json';

    $.ajax({
        url: request_url, 
        success: function(data){
      
            for (let i=0, item; item=data.Results[i]; i++) {
                let car_model = item.Model_Name;

                $('select[name=car_model]').append(
                $('<option></option>').val(car_model).html(car_model)
                );
                
            }
       }
    });
    
    // Fetches the current selected type of service price on page load.
    tos = $('#type-of-service').children(":selected").data("price");
    
    // Gets the selected options on page load and returns the price.
    $('.optional-services').ready(function() {
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

    
});

// This collects the option in car_make, and when changed it pulls the options for the car_model option list.
$('select[name=car_make]').change(function(){
    car_make = $(this).val();
    var request_url = 'https://vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMake/' + car_make + '?format=json';
    
    $('select[name=car_model]').empty();
    $.ajax({
        url: request_url,
        success: function(data){
            for (let i=0, item; item=data.Results[i]; i++) {
                let car_model = item.Model_Name;

                $('select[name=car_model]').append(
                $('<option></option>').val(car_model).html(car_model)
                );
            }
       }
    });
});

// Updates the image on the quotes page to show vehicle sizing which also hides or show's certain div's depending on choosen option.
$('#type-of-service').change(function(){
    dropdown = this.value;
    
    // Changes the image and fades in the needed containers.
    if(dropdown=="1") {
        $("#service-image").html( "<img class='img-responsive' src='https://autowraps-bucket.s3.eu-west-2.amazonaws.com/media/quotes/Large_veh.jpg'>");
        $("#wrap-colour-container").fadeIn();
        $("#optional-service-container").fadeIn();
        $("#damage-container").fadeIn();
        $("#make-model-container").fadeIn(); 
        $("#price-container").fadeIn();
    }
    
    // Changes the image and fades in the needed containers.
    if(dropdown=="2") {
        $("#service-image").html( "<img class='img-responsive' src='https://autowraps-bucket.s3.eu-west-2.amazonaws.com/media/quotes/Mid_veh.jpg'>");
        $("#wrap-colour-container").fadeIn();
        $("#optional-service-container").fadeIn();
        $("#damage-container").fadeIn();
        $("#make-model-container").fadeIn(); 
        $("#price-container").fadeIn();
    }
    
    // Changes the image and fades in the needed containers.    
    if(dropdown=="3") {
        $("#service-image").html( "<img class='img-responsive' src='https://autowraps-bucket.s3.eu-west-2.amazonaws.com/media/quotes/Small_veh.jpg'>");
        $("#wrap-colour-container").fadeIn();
        $("#optional-service-container").fadeIn();
        $("#damage-container").fadeIn();
        $("#make-model-container").fadeIn(); 
        $("#price-container").fadeIn();
    }
    
    // Changes the image and fades in/out the needed containers.
    if(dropdown=="4") {
        $("#service-image").html( "<img class='img-responsive' src='https://autowraps-bucket.s3.eu-west-2.amazonaws.com/media/quotes/bonnet_wrap.jpg'>");
        $("#wrap-colour-container").fadeIn();
        $("#optional-service-container").fadeOut();
        $("#damage-container").fadeIn();
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
        // This is mainly for the orders page as it's hidden on the quotes page until an option is slected which will then display the correct page.
        totalPrice = $(".total-price-input").val();
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
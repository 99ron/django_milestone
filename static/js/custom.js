/* global $ */
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

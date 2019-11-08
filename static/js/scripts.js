

<script>
    jQuery("#delete_order").click(function(){
        $("<div></div>").appendTo('body')
           .html('<div><h3> Are you sure you want to delete this order? </h3></div>')
           .dialog({
                title: "Confirm" ,
                width:500, height:300,
                modal:true,
                resizable: false, 
                show: { effect: 'drop', direction: "left" }, 
                hide:{effect:'blind'}

                buttons: {
                    Yes: function() {
                          jQuery.ajax({
                              type:"POST", //post data
                              data:{'key':key}, //if you want to send any data to view 
                              url:'/delete/' // your url that u write in action in form tag
                          }).done(function(result){
                               alert("am done") //this will executes after your view executed  
                          })
                     },
                    Cancel: function() {
                        $( this ).dialog( "close" );
                    }
               }
           });
    });
<script> 
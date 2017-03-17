$(document).ready(function(){
$("#submit").click(function(){
    event.preventDefault();
    var location = $("#pickup").val();
    var destination = $("#dest").val();
    var travel_size = $("#seat").val();
    var driver = $("#driver").val();
    var vehicle_class = $("#vtype").val();
    var waiting_factor = $("#wfactor").val();
    
    // Returns successful data submission message when the entered information is stored in database.
    var taxi_request = {
        'location': location,
        'destination': destination,
        'travel_size': travel_size,
        'driver': driver,
        'vehicle_class': vehicle_class,
        'waiting_factor': waiting_factor,
        
    };
    
    var data=JSON.stringify(taxi_request);
    
    // AJAX Code To Submit Form.
    $.ajax({
        type: "POST",
        url: "request",
        data: data,
        dataType:"json",
        contentType:"application/json",
        success:function(data){
            console.log(data);
        },
        error: function()
        {
            console.log('Error');
        }
    });
    return false;
});
});
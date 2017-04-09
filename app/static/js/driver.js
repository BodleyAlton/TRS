var run;
var intv= 15000;
var dpos;
var lat;
var lng;
var status;
var url= '/dloc-update'
$(document).ready(function(){
  $('#start').on('click',function(){
    console.log("start")
    run= setInterval(function(){
          if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(function(position){
              dpos = {
                lat: position.coords.latitude,
                lng: position.coords.longitude
              };
            console.log("current pos; lat:"+dpos.lat+" lng:"+dpos.lng);
            console.log(url)
            $.ajax({url,
            data:{
              dlat: dpos.lat,
              dlng: dpos.lng
            },
            method: 'POST'
          }).done(function(status){
              console.log(status)
            })},function() {
            });
          }
        },intv);
        console.log("AFTER")
  });
  $('#stop').on('click',function(){
    console.log("Stop")
    clearInterval(run);
  });
});

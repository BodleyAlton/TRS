var run;
var intv= 15000;
var dpos;
function myFunction(){
  status = 'inactive';
  stat(status);
}
function update(){
  status='active'
  stat(status);
}
function stat(status){
  if (status!='inactive'){
    run= setInterval(function(){
      if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function(position) {
          dpos = {
            lat: position.coords.latitude,
            lng: position.coords.longitude
          };
        console.log("current pos; lat:"+cpos.lat+" lng:"+cpos.lng);
        }, function() {
        });
      }
    },intv);

  }
  else {
    clearInterval(run);
  }
}

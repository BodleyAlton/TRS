// Note: This example requires that you consent to location sharing when
      // prompted by your browser. If you see the error "The Geolocation service
      // failed.", it means you probably did not give permission for the browser to
      // locate you.

// ------Global Variables-----
var map; // The map object
var pickUp; //pick-up location Marker
var cpos; //current (position) location of device
var dest; //destination Marker
var destLoc;//destination location
var pickUpLoc; //Pick up location
var pos;
var coords;
var geocoder;
var markers=[pickUp,dest];

// -----Generate Map-----
function createMap(){
  map = new google.maps.Map(document.getElementById('map'), {
    center: {lat: 18.0179, lng: -76.8199},
    zoom: 14,
    mapTypeId: 'roadmap'
  });
  geocoder = new google.maps.Geocoder();
  getCurrent();
  search();
  setPickUp();
  setDestination();
  drawRoute();
  //request(pickUpLoc,destLoc);
}

// --Returns the current location of the user--
function getCurrent() {
//------HTML5 geolocation.------
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(function(position) {
      cpos = {
        lat: position.coords.latitude,
        lng: position.coords.longitude
      };
    pickUp =new google.maps.Marker({
      position:cpos,
      title: 'Wet Pig',
      draggable: false
    });
    pickUpLoc=cpos;
    map.setCenter(cpos);
    pickUp.setMap(map);
    console.log("current pos; lat:"+cpos.lat+" lng:"+cpos.lng);
    // console.log("Pickup if set to current: "+pickUpLoc.lat+","+pickUpLoc.lng);
    // $.ajax('/save-coord', {
    //   data: {
    //     x:  '12',
    //     y: '123'
    //   },
    //   method: 'POST'
    // }).then(function(response) {
    //    console.log(response);
    //   //  var coords = JSON.parse('{x: 12, y:13}');
    //   var coords = response;
    //    console.log(coords.xcoord);
    // });
    }, function() {
    });
  }
}
function search(){
  var pickup = document.getElementById('pickup');
  var plbl= document.getElementById('p');
  var psub= document.getElementById('psubmit');

  var psearchBox = new google.maps.places.SearchBox(pickup);
  map.controls[google.maps.ControlPosition.TOP_LEFT].push(plbl);
  map.controls[google.maps.ControlPosition.TOP_LEFT].push(pickup);
  map.controls[google.maps.ControlPosition.TOP_LEFT].push(psub);

  var dests = document.getElementById('dest');
  var dlbl= document.getElementById('d');
  var dsub= document.getElementById('dsubmit');

  var dsearchBox = new google.maps.places.SearchBox(dests);
  map.controls[google.maps.ControlPosition.TOP_LEFT].push(dlbl);
  map.controls[google.maps.ControlPosition.TOP_LEFT].push(dests);
  map.controls[google.maps.ControlPosition.TOP_LEFT].push(dsub);


}
function setPickUp(){
  document.getElementById('psubmit').addEventListener('click',function(){
    var address=$("#pickup").val();
    geocoder.geocode({'address': address},function(results,status){
      if (status === 'OK'){
        pickUpLoc = (results[0].geometry.location.lat()+','+results[0].geometry.location.lng());
      }else{('We could not locate the address you entered. Status: '+status);}
      pickUp.setPosition(results[0].geometry.location);
      pickUp.setMap(map);
      pickUp.setTitle("Pick up");
      map.setCenter(results[0].geometry.location);
    });
  });
}
function setDestination(){
  document.getElementById('dsubmit').addEventListener('click',function(){
    var address=$("#dest").val();
    geocoder.geocode({'address': address},function(results,status){
      if (status === 'OK'){
        destLoc = (results[0].geometry.location.lat()+','+results[0].geometry.location.lng());
      }else{('We could not locate the address you entered. Status: '+status);}
      dest =new google.maps.Marker({
        position:results[0].geometry.location,
        title: 'Destination',
        draggable:false
      });
      dest.setMap(map);
      map.setCenter(results[0].geometry.location);
      console.log("pUp From dest: "+pickUpLoc)
      console.log("Dloc from dest: "+destLoc)
      request(pickUpLoc,destLoc);
      drawRoute();
    });
  });
}
/*-----Draw route between two points-----
@param: pickUp: pick up coordinates
        dest: destination coordinates*/
function drawRoute(){
  var directionsService = new google.maps.DirectionsService;
  var directionsDisplay = new google.maps.DirectionsRenderer;
  directionsDisplay.setMap(map);
  //document.getElementById(/*Search/Request*/).addEventListener('click',function(){
    directionsService.route({
    origin:$("#pickup").val(),
    destination: $("#dest").val(),
    //waypoints: ['656 Hope Rd Kingston'],
    travelMode: 'DRIVING'
    },function(response,status){
        if(status=='OK'){
          distance();
          // console.log("RESPONSE: "+JSON.stringify(response));
          directionsDisplay.setDirections(response);
          //destLoc.setMap(null);
        }else{console.log("directions failed: "+status);}
    // });console.log("Route");
});
}
function distance(){
  var service = new google.maps.DistanceMatrixService();
  service.getDistanceMatrix(
    {
      origins: [$("#pickup").val()],
      destinations: [$("#dest").val()],
      travelMode: 'DRIVING',
      avoidHighways: false,
      avoidTolls: false,
    }, function(response, status){
      if (status == 'OK') {
    var origins = response.originAddresses;
    var destinations = response.destinationAddresses;

    for (var i = 0; i < origins.length; i++) {
      var results = response.rows[i].elements;
      for (var j = 0; j < results.length; j++) {
        var element = results[j];
        var distance = element.distance.text;
        var duration = element.duration.text;
        var from = origins[i];
        var to = destinations[j];
        console.log("DURATION: "+duration);
        console.log("PICKUP: "+JSON.stringify(pickUpLoc))

      }
    }
  }
    });
}
function request(pickUpLoc,destLoc){
  console.log("request");
  $('#request').click(function(e){
    e.preventDefault();
    url='/request';
    console.log("pickup REQ: "+pickUpLoc);
    console.log("dest REQ: "+destLoc);
    seat=$('#seat').val();
    console.log("SEATING: "+seat);
    vehicle=$('#type').val();
    console.log("vehicle: "+vehicle);
    wfac=$('#wfac').val();
    console.log("wfac: "+wfac);
    dname=$('#driverN').val();
    console.log("dname: "+dname);
    $.ajax({url,
     data: {
       pickup: pickUpLoc,
       dest: destLoc,
       seat:seat,
       vehicle:vehicle,
       wfac:wfac,
       dname:dname
      },
     method: 'POST'
   }).done(function(status){
     console.log("RESPONSE: "+status);
   });
  });
}
var source = new EventSource("{{ url_for('sse.stream')}}");
source.addEventListener('text',function(e){
  var data = JSON.parse(e.data);
  console.log("data: "+data);
}, false);

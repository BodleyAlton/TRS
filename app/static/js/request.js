var duration;
var allDrivers;
url= '/suggested_drivers';

var df=$.Deferred()

function pdrivers(driver,pickup){
  allDrivers=driver
  console.log("Here")
  for(y=0; y < driver.length; y++){
    drivers=driver[y][2][0]+","+driver[y][2][1];

    dist(drivers,pickup,driver,y)
  }
}

function dist(driver,pickup,drivers,y){
  var service = new google.maps.DistanceMatrixService();
  service.getDistanceMatrix(
    {
      origins: [driver],
      destinations: [pickup],
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
        duration = element.duration.value;
        var from = origins[i];
        var to = destinations[j];
        drivers[y].push(duration);
        insertionSort(y);
        console.log("final")
        console.log(allDrivers)
        df.resolve()
        }
    }
  }
  });
}


function insertionSort(y){
  for(x = 0; x < allDrivers.length; x++){
    if (allDrivers[x][3] != 'undifined'){
      if (allDrivers[x][3] > allDrivers[y][3]){
      temp=allDrivers[y]
      allDrivers[y]=allDrivers[x]
      allDrivers[x]=temp
      }
    }
  }
}
  df.done (function(){
    url= '/suggested_drivers';
      console.log("AJAX")
      console.log(allDrivers[0][1])
      console.log("AJA")

  $.ajax({ url,
        data:{
        suggDrivers: allDrivers[0][1] },
        method:"POST"
      }).done(function(status){
        console.log(status)
      })
  })

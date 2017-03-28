var duration;
var driver;
function pdrivers(driver,pickup){
  for(y=0; y < driver.length; y++){
    drivers=driver[y][2][0]+","+driver[y][2][1];
    dist(drivers,pickup,driver,y);
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
        insertionSort(drivers);
        console.log("Drivers sorted")
        console.log(drivers)
        return duration;
      }
    }
  }
  });
}
function mergeSort(arr){
 var len = arr.length;
 if(len <2)
    return arr;
 var mid = Math.floor(len/2),
     left = arr.slice(0,mid),
     right =arr.slice(mid);
 //send left and right to the mergeSort to broke it down into pieces
 //then merge those
 return merge(mergeSort(left),mergeSort(right));
}
function merge(left, right){
  var result = [],
      lLen = left.length,
      rLen = right.length,
      l = 0,
      r = 0;
  while(l < lLen && r < rLen){
     if(left[l][3] < right[r][3]){
       result.push(left[l++]);
     }
     else{
       result.push(right[r++]);
    }
  }
  //remaining part needs to be addred to the result
  return result.concat(left.slice(l)).concat(right.slice(r));
}

function insertionSort(arr){
  var i, len = arr.length, el, j;
  for(i = 1; i<len; i++){
    el = arr[i];
    j = i;
    while(j>0 && arr[j-1][3] > arr[j][3]){
      //console.log("to insert: "+toInsert)
      arr[j] = arr[j-1];
      j--;
   }

   arr[j] = el;
  }

  return arr;
}

var run;
var intv= 15000;
var dpos;
var lat;
var lng;
var status;
var url= '/dloc-update'
$(document).ready(function(){
  w3.hide('#stop')
  $('#start').on('click',function(){
    w3.toggleShow('#stop')
    console.log("start")
    run= setInterval(function(){
          if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(function(position){
              dpos = {
                lat: position.coords.latitude,
                lng: position.coords.longitude
              };
            console.log("current pos; lat:"+dpos.lat+" lng:"+dpos.lng);
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
          //   $.ajax({url,
          //   data:JSON.stringify({
          //     dlat: lat,
          //     dlng: lng
          //   }),
          //   method: 'POST'
          // }).done(function(status){
          //     console.log("DONE")
          //   })},
            ,function() {}
            ;
        },intv);

  $('#stop').on('click',function(){
    w3.toggleShow('#start')
    console.log("Stop")
    clearInterval(run);
  });
});
});
// $(document).ready(function(){
//   checkStat();
//  });
//
// function checkStat(){
//   $('#status').on('click',function(){
//     if($('#status').val()!='Offline'){
//       active();
//       // stat();
//     }
//     else {
//       inactive();
//       // stop();
//     }
//   });
// }
//
// function inactive(){
//   status = "inactive";
//   console.log("stat: "+status)
//   // clearInterval(run);
//   stat(status);
//   // stop();
// }
//
// function active(){
//   status="active";
//   console.log("stat: "+status)
//   stat(status);
// }
//
// function stat(status){
//   console.log("MY STAT: "+status)
//   if (status =='active'){
//     run= setInterval(function(){
//       // console.log("STAT:")
//       // console.log(run)
//       if (navigator.geolocation) {
//         navigator.geolocation.getCurrentPosition(function(position) {
//           dpos = {
//             lat: position.coords.latitude,
//             lng: position.coords.longitude
//           };
//         console.log("current pos; lat:"+dpos.lat+" lng:"+dpos.lng);},
//         function() {
//         });
//       }
//     },3000);
//   }
//   else {//console.log("ELSE B4:")
//   // console.log(run)
//   clearInterval(run);
//   // console.log("ELSE Aftr:")
//   //   console.log(run)
//   //   // console.log("STOP")
//   //   console.log("STATF: "+status)
//   }
// }
// function stop(){
//   console.log('OFFLINE')
//   clearInterval(run);
// }

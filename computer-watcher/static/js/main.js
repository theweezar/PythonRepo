window.onload = function(){
  const screen = document.getElementById("screenCpt")
  const webcam = document.getElementById("webcamCpt")
  const socket = io()
  
  webcam.addEventListener("click", function(){
    socket.emit("start_webcam")
  })

  socket.emit("request_to_connect")
  socket.on("connected_to_server", function(res){
    console.log(res);
  })

  // socket.on("recording", function(p){
  //   console.log(p);
  // })
}
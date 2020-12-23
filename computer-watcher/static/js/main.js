window.onload = function(){
  const screen = document.getElementById("screenCpt")
  const webcam = document.getElementById("webcamCpt")
  const frame = document.getElementById("frame")
  const stop = document.getElementById("stopBtn")
  const socket = io()
  
  webcam.addEventListener("click", function(){
    alert("Camera is starting...")
    socket.emit("start_webcam")
    stop.classList.toggle("d-none")
  })

  stop.addEventListener("click", function(){
    alert("Stop....")
    socket.emit("stop_webcam")
    stop.classList.toggle("d-none")
  })

  socket.on("recording", function(arrayBuffer){
    const base64_img = "data:image/jpeg;base64,"+arrayBuffer
    const img = new Image(400, 300)
    img.src = base64_img
    img.style.border = "2px solid black"
    // console.log(base64_img);
    frame.innerHTML = img.outerHTML
  })

  socket.on("connect", function(){
    console.log("Connection is established")
    alert("Connection is established")
  })

  socket.on("disconnect", function(){
    this.close()
  })
}


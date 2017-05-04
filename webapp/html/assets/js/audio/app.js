function restore(){
  $("#record").removeClass("disabled");
  $("#pause").html("Pause");
  $("#pause").removeClass("resume");
  
  if($(".one").is( "button" )) {
    $(".one").prop('disabled', true);
  }
    
  $(".one").addClass("disabled");

  Fr.voice.stop();
}

function makeWaveform(){
  var analyser = Fr.voice.recorder.analyser;

  var bufferLength = analyser.frequencyBinCount;
  var dataArray = new Uint8Array(bufferLength);

  /**
   * The Waveform canvas
   */
  var WIDTH = 500,
      HEIGHT = 200;

  var canvasCtx = $("#level")[0].getContext("2d");
  canvasCtx.clearRect(0, 0, WIDTH, HEIGHT);

  function draw() {
    var drawVisual = requestAnimationFrame(draw);

    analyser.getByteTimeDomainData(dataArray);

    canvasCtx.clearRect(0, 0, WIDTH, HEIGHT);
    canvasCtx.lineWidth = 2;
    canvasCtx.strokeStyle = 'rgb(255, 255, 255)';

    canvasCtx.beginPath();

    var sliceWidth = WIDTH * 1.0 / bufferLength;
    var x = 0;
    for(var i = 0; i < bufferLength; i++) {
      var v = dataArray[i] / 128.0;
      var y = v * HEIGHT/2;

      if(i === 0) {
        canvasCtx.moveTo(x, y);
      } else {
        canvasCtx.lineTo(x, y);
      }

      x += sliceWidth;
    }
    canvasCtx.lineTo(WIDTH, HEIGHT/2);
    canvasCtx.stroke();
  };
  draw();
}

$(document).ready(function(){
  $(document).on("click", "#record:not(.disabled)", function(){
    Fr.voice.record($("#live").is(":checked"), function(){
      $(".recordButton").addClass("disabled");

      $("#live").addClass("disabled");

      if($(".one").is("button")) {
        $(".one").prop('disabled', false);
      }
      $(".one").removeClass("disabled");

      makeWaveform();
    });
  });

  $(document).on("click", "#recordFor5:not(.disabled)", function(){
    Fr.voice.record($("#live").is(":checked"), function(){
      $(".recordButton").addClass("disabled");

      $("#live").addClass("disabled");
      $(".one").removeClass("disabled");

      makeWaveform();
    });

    Fr.voice.stopRecordingAfter(5000, function(){
      alert("Recording stopped after 5 seconds");
    });
  });

  $(document).on("click", "#pause:not(.disabled)", function(){
    if($(this).hasClass("resume")){
      Fr.voice.resume();
      $(this).html("Pause");
      $(this).removeClass("resume");
    }else{
      Fr.voice.pause();
      $(this).html("Resume");
      $(this).addClass("resume");
    }
  });

  $(document).on("click", "#stop:not(.disabled)", function(){
    restore();
  });

  $(document).on("click", "#play:not(.disabled)", function(){
    if($(this).parent().data("type") === "mp3"){
      Fr.voice.exportMP3(function(url){
        $("#audio").attr("src", url);
        $("#audio")[0].play();
      }, "URL");
    }else{
      Fr.voice.export(function(url){
        $("#audio").attr("src", url);
        $("#audio")[0].play();
      }, "URL");
    }
    restore();
  });

  $(document).on("click", "#download:not(.disabled)", function(){
    if($(this).parent().data("type") === "mp3"){
      Fr.voice.exportMP3(function(url){
        $("<a href='" + url + "' download='MyRecording.mp3'></a>")[0].click();
      }, "URL");
    }else{
      Fr.voice.export(function(url){
        $("<a href='" + url + "' download='MyRecording.wav'></a>")[0].click();
      }, "URL");
    }
    restore();
  });

  $(document).on("click", "#base64:not(.disabled)", function(){
    if($(this).parent().data("type") === "mp3"){
      Fr.voice.exportMP3(function(url){
        console.log("Here is the base64 URL : " + url);
        alert("Check the web console for the URL");

        $("<a href='"+ url +"' target='_blank'></a>")[0].click();
      }, "base64");
    }else{
      Fr.voice.export(function(url){
        console.log("Here is the base64 URL : " + url);
        alert("Check the web console for the URL");

        $("<a href='"+ url +"' target='_blank'></a>")[0].click();
      }, "base64");
    }
    restore();
  });

  $(document).on("click", "#search:not(.disabled)", function(){

    $("#match").css("display", "block");
    $("#match").html("Please wait while we retrieve your results.");

    if(isTest) {
      $("#match").css("display", "block");
      $("#match").html("No Results Found.");
    } else {
      function upload(base64){
        // var formData = new FormData();
        base64 = base64.slice( base64.indexOf("base64,") + 7)
        // formData.append('music_buffer', base64);
        var data_JSON = { "music_buf" : base64 }

        var url = musicURL;
        $.ajax({
          url: url,
          type: 'POST',
          dataType: "json",
          //crossDomain: true, //for local testing
          // crossDomain: false,
          // contentType: false,
          // processData: false,
          // data: formData,
          data: JSON.stringify(data_JSON),
          success: function(result) {
            $("#match").css("display", "block");
            $("#match").html("Your Match: " + result.title + " by " + result.artists[0].artist);
          },
          error: function() {
            $("#match").css("display", "block");
            $("#match").html("No Results Found.");
          }
        });
      }
      if($(this).parent().data("type") === "mp3"){
        Fr.voice.exportMP3(upload, "base64");
      }else{
        Fr.voice.export(upload, "base64");
      }
    }

    restore();
  });
});

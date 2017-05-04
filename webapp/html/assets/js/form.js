//JQuery handling the control of the recommendation form

//when the add artists is clicked, more fields are added.
$(document).ready(function() {
	//allows the user to add artists to the form, up to 5 artists

	var artistList = [
		"<input type=\"text\" name=\"artist-1\" id=\"artist-1\" value=\"\" placeholder=\"e.g. Van Morrison\" />",
		"<input type=\"text\" name=\"artist-2\" id=\"artist-2\" value=\"\" placeholder=\"e.g. Van Stephensen\" />",
		"<input type=\"text\" name=\"artist-3\" id=\"artist-3\" value=\"\" placeholder=\"e.g. Van Craven\" />",
		"<input type=\"text\" name=\"artist-4\" id=\"artist-4\" value=\"\" placeholder=\"e.g. Van Williams\" />",
		"<input type=\"text\" name=\"artist-5\" id=\"artist-5\" value=\"\" placeholder=\"e.g. Van Wilder\" />"
	];

	var artistCounter = 0;

	$("#addArtist").click(function() {

		//we will check to see how many artists are on screen
		if(artistCounter < 6) {
			//if less than 5, another artist is added
			$("#field").append(artistList[artistCounter]);
			artistCounter++;
		}
		
		if(artistCounter == 5) {
			//we disable the button at 5 presses
			  if($("#addArtist").is( "button" )) {
			    $("#addArtist").prop('disabled', true);
			  }
			$("#addArtist").addClass("disabled");
		}

	});

	$("#recommendationForm").submit(function(e) {

		//if the input is empty
		if($("#artist-0").val().length == 0) {
			$("#recommendationMatch").css("display", "block");
       		$("#recommendationMatch").html("Please input an artist into the first field.");
		} else {

			var url = artistURL + encodeURIComponent($("#artist-0").val());

			$("#recommendationSpinner").css("display", "block");
			$("#recommendationMatch").css("display", "block");
          	$("#recommendationMatch").html("Please wait while we retrieve your results.");

			$.ajax({
	           type: "GET",
	           crossDomain: false,
	           headers: { 'Accept': 'application/json' },
	           url: url,
	           data: $("#idForm").serialize(), // serializes the form's elements.
	           success: function(result)
	           {
	           		//filter out the best response
	           		artists = result.artists;
	           		var bestArtist = "";
	           		var bestArtistScore = -1;

	           		for(var i = 0; i < artists.length; i++) {
	           			if (artists[i].score > bestArtistScore) {
	           				bestArtistScore = artists[i].score;
	           				bestArtist = artists[i].name;
	           			}
	           		}

	           		$("#recommendationSpinner").css("display", "none");
	       			$("#recommendationMatch").css("display", "block");
	              	$("#recommendationMatch").html("We recommend " + bestArtist);
	           },
	           error: function(xhr, status, error) {
  				var err = eval("(" + xhr.responseText + ")");
  				alert(err.Message);
			   	$("#recommendationSpinner").css("display", "none");
	           		$("#recommendationMatch").css("display", "block");
	           		$("#recommendationMatch").html("Sorry, we don't have any recommendations from your query.");
	           }
	         });
		}

	    e.preventDefault(); // avoid to execute the actual submit of the form.

	});
});

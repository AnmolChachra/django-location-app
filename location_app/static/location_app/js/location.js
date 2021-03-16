var longitude, latitude, place_name, place_id, autocomplete;
// var defaultLatLng = {lat:40.7127753, lng:-74.0059728}; //Default latitude and longitude of New York

var aliases = {
	locality: 'id_city',
	administrative_area_level_1: 'id_state',
	country: 'id_country',
};
var componentForm = {
	locality: 'long_name',
	administrative_area_level_1: 'long_name',
	country: 'long_name',
};

function fillInAddress() {
	// Get the place details from the autocomplete object.
	var place = autocomplete.getPlace();
	for (var component in aliases) {
		document.getElementById(aliases[component]).value = ''; //reseting the value
  	}

	// Get each component of the address from the place details
	// and fill the corresponding field on the form.
	for (var i = 0; i < place.address_components.length; i++) {
		var addressType = place.address_components[i].types[0];
    	if (componentForm[addressType]) {
    		var val = place.address_components[i][componentForm[addressType]];
      		document.getElementById(aliases[addressType]).value = val;
    	}
  	}
}

// This function will be called when the window first loads
function initAutocomplete() {

	//Disable the inputs that you dont need users to modify
	document.getElementById("id_place").disabled=true;
  document.getElementById("id_latitude").disabled=true;
  document.getElementById("id_longitude").disabled=true;
  document.getElementById("id_city").disabled=true;
  document.getElementById("id_state").disabled=true;
  document.getElementById("id_country").disabled=true;
  document.getElementById("id_place_id").disabled=true;

  //Get location widget values
  var widget = document.getElementById("location");
  console.log(widget.dataset);
  var mapOptions, markerOptions;
  
  mapOptions = JSON.parse(widget.dataset.mapOptions);
  markerOptions = JSON.parse(widget.dataset.markerOptions);

  console.log(mapOptions);
  console.log(markerOptions);

	//Setting the map
	var map = new google.maps.Map(document.getElementById('map'), mapOptions);	

	// var drop_button = (document.getElementById('drop_pin'));

	//Pushing the autocomplete field at the left of the map screen
	// map.controls[google.maps.ControlPosition.TOP_CENTER].push(input);

	var mymarker = new google.maps.Marker(markerOptions);
  mymarker.setMap(map);
  mymarker.setPosition(mapOptions.center);
  mymarker.setAnimation(google.maps.Animation.DROP);

	// Adding event listener 'click' on map, to place marker
	// map.addListener('click', function(event){addMarker(event.latLng, map)});


	// Handling marker events
	//function handleEvent(event){} - Edit this to handle marker dragged event

	// Setting the marker
	function addMarker(latLng, map){
  	// Initialize the marker
  	var marker = new google.maps.Marker({
     	map: map,
    	position:latLng,
    	animation: google.maps.Animation.DROP,
    	draggable: false,
    	});

		return marker;
  	}

	var input = (document.getElementById('id_location')); // Getting the autocomplete field

	// Create the autocomplete object -- Restricting it to use business establishments only
	autocomplete = new google.maps.places.Autocomplete(input, {
    	type:'establishment' //returns the addresses of the establishments
    });

	// Binding autocomplete to map
	autocomplete.bindTo('bound', map);


	// Handling the event
	google.maps.event.addListener(autocomplete, 'place_changed', function() {
    	var place = autocomplete.getPlace();
    	place_name = place.name;
    	place_id = place.place_id;

    	if (!place.geometry){
    		window.alert("Autocomplete's returned place contains no geometry");
      		return;
    	}

    	// If the place has geometry, then present it on the map
    	if (place.geometry.viewport) {
     		map.fitBounds(place.geometry.viewport);
    	}
    	else {
      		map.setCenter(place.geometry.location);
      		map.setZoom(17);
		}

    	longitude = place.geometry.location.lng();
    	latitude = place.geometry.location.lat();

		mymarker.setMap(null);
    	mymarker = addMarker({lat:latitude,lng:longitude}, map);

    	//Setting the form fields
    	document.getElementById('id_place').value = place_name;
  		document.getElementById('id_place_id').value = place_id;
    	document.getElementById('id_latitude').value = latitude;
    	document.getElementById('id_longitude').value = longitude;

    	fillInAddress(); // Set City State and Country

    document.getElementById("location_details").style.display="initial";
  	});
}


function enable_and_submit(){
  document.getElementById("id_place").disabled=false;
  document.getElementById("id_latitude").disabled=false;
  document.getElementById("id_longitude").disabled=false;
  document.getElementById("id_city").disabled=false;
  document.getElementById("id_state").disabled=false;
  document.getElementById("id_country").disabled=false;
  document.getElementById("id_place_id").disabled=false;
	return True;
}

google.maps.event.addDomListener(window, 'load', initAutocomplete); // Function that will be called when the window first loads
// function onRetrieveClick() {
//
//   var xhttp = new XMLHttpRequest();
//    xhttp.onreadystatechange = function() {
//      if (this.readyState == 4 && this.status == 200) { // Thisis the callback function
//          // Get the string data that the server sent us.
//          if (this.readyState == 4 && this.status == 200) {
//
//            document.getElementById('temp_avg').innerHTML = this.responseText;
//
//          }
//        }
//      }
//        xhttp.open('POST', "{% url 'sensor_retrieve_page' %}", true);
//        xhttp.setRequestHeader("content-type", "application/x-www-form-urlencoded");
//        xhttp.send();
//
// }
//


function onBackClick() {
    window.location.href = "{% url 'dashboard_page' %}";
}

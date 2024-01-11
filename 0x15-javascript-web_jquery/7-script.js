$(document).ready(function () {
  fetch('https://swapi-api.alx-tools.com/api/people/5/?format=json')
    .then(response => {
      return response.json();
    })
    .then(data => {
      $('div#character').text(data.name);
    });
});

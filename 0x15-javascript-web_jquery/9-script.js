$(document).ready(function () {
  fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
    .then(response => {
      return response.json();
    })
    .then(data => {
      $('DIV#hello').text(data.hello);
    });
});

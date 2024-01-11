$(document).ready(function () {
// ###both working well
//   fetch('https://swapi-api.alx-tools.com/api/films/?format=json')
//     .then(response => {
//       return response.json();
//     })
//     .then(data => {
//       data.results.forEach(movie => {
//         $('ul#list_movies').append(`<li>${movie.title}</li>`);
//       });
//     });
// });

  $.ajax({
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    dataType: 'json',
    success: function (data) {
      data.results.forEach(function (movie) {
        $('ul#list_movies').append(`<li>${movie.title}</li>`);
      });
    }
  });
});

#!/usr/bin/node
const $ = window.$;
$(function () {
  const $movies = $('UL#list_movies');
  $.ajax({
    type: 'GET',
    url: 'https://swapi-api.hbtn.io/api/films/?format=json',
    success: function (movies) {
      $.each(movies.results, function (i, movie) {
        $movies.append('<li>' + movie.title + '</li>');
      });
    }
  });
});

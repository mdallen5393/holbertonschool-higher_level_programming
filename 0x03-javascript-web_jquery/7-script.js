#!/usr/bin/node
const $ = window.$;
$(function () {
  $.get('https://swapi-api.hbtn.io/api/people/5/?format=json', function (data, status) {
    $('DIV#character').text(data.name);
  });
});

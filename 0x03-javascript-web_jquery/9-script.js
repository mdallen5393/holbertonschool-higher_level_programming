#!/usr/bin/node
const $ = window.$;
$(function () {
  $.ajax({
    type: 'GET',
    url: 'https://stefanbohacek.com/hellosalut/?lang=fr',
    success: ((data) => $('DIV#hello').text(data.hello))
  });
});

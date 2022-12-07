#!/usr/bin/node
const $ = window.$;
$('DIV#update_header').click(function () {
  $(this).text('New Header!!!');
});

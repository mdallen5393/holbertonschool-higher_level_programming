#!/usr/bin/node
const $ = window.$;
$('DIV#red_header').click(function () {
  $(this).css('color', '#F00');
});

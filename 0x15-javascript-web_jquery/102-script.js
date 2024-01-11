window.onload = function () {
  $('INPUT#btn_translate').click(function () {
    const Code = $('INPUT#language_code').val().trim().toLowerCase();
    $.ajax({
      url: `https://www.fourtonfish.com/hellosalut/hello/${Code}`,
      dataType: 'json',
      success: function (data) {
        if (data && data.hello) {
          $('DIV#hello').text(data.hello);
        }
      }
    });
  });
};

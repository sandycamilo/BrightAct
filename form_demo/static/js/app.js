var $form = $('form#test-form'),
    url = 'https://script.google.com/macros/s/AKfycbyeHW_N7ECGWuHb0CB5TBNICs_zy_O8KIeLwVuvBnBPEXZo6FE/exec'

$('#submit-form').on('click', function(e) {
  e.preventDefault();
  var jqxhr = $.ajax({
    url: url,
    method: "GET",
    dataType: "json",
    data: $form.serializeObject()
  }).success(
    // do something
  );
})

// request = $.ajax({
//   url: "https://script.google.com/macros/s/AKfycbyeHW_N7ECGWuHb0CB5TBNICs_zy_O8KIeLwVuvBnBPEXZo6FE/exec",
//   type: "post",
//   data: serializedData
// });

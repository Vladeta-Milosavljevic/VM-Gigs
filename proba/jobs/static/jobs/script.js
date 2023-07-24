function getPage(url) {
  $.ajax({
    url: url,
    type: "get",
    success: function (result, status, xhr) {
      $("#data_point").html(result);
    },
    error: function (xhr, status, error) {
      console.log(error);
    },
  });
}

function deleteData(deleteUrl, successUrl) {
  $.ajax({
    url: deleteUrl,
    type: "post",
    data: {
      csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val(),
    },
    success: function (result, status, xhr) {
      console.log("Deleted.");
      getPage(successUrl);
    },
    error: function (xhr, status, error) {
      console.log(error);
    },
  });
}

function removeClassActive() {
  $("#carousel").removeClass("active");
}

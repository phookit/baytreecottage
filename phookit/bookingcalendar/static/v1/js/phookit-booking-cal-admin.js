
var bookings = {
  api_root_feed: "/api/bc/feed/",  
  api_root_admin: "/api/bc/admin/",
  api_root_admin_price: "/api/bc/admin/price/",
  mkRequestPOST: function(data, args) {
    var result = "csrfmiddlewaretoken="+$.cookie('csrftoken')+"&_content_type=application%2Fjson";
    if( data ) {
      var r = JSON.stringify(data, function (key, value) {
        return value;
      });
      result = result + "&_content=" + encodeURIComponent(r);
    }
    if(args) {
      var first = true;
      $.each(args, function (k, v) {
        var sep = "&";      
        if(first) {
          sep = "?";
          first = false;
        }
        result = result + sep + k + "=" + v;
      });
    }
    return result;
  },
  mkRequestPUT: function(data) {
    return "_method=PUT&" + bookings.mkRequestPOST(data);         
  },
  mkApiBookingData: function() {
    return {
      start: moment( $("#startDateInput").datepicker("getDate") ).format("YYYY-MM-DD"),
      end: moment( $("#endDateInput").datepicker("getDate") ).format("YYYY-MM-DD"),
      name: $("#nameInput").val(),
      email: $("#emailInput").val(),
      tel: $("#telInput").val(),
      info: $("#infoInput").val(),
      status: $("#statusInput").val()
    };
  },
  mkApiBookingPriceData: function() {
    return {
      start: moment( $("#bpStartDateInput").datepicker("getDate") ).format("YYYY-MM-DD"),
      end: moment( $("#bpEndDateInput").datepicker("getDate") ).format("YYYY-MM-DD"),
      price: $("#bpPriceInput").val()
    };
  },
  ajax_error: function(xhr, textStatus, errorThrown) {
    if(xhr.status) {
      alert(xhr.status + ": " + xhr.responseText + " TStatus:"+textStatus+" error:"+errorThrown);
    }
    else {
      alert("Could not connect to server. Please try again later");  
    }
  },
  api_booking_upload: function() {
    if( bookings.validate_booking() ) {  
        var data = bookings.mkApiBookingData();              
        $.ajax({
          url: bookings.api_root_admin,
          type: "POST",
          data: bookings.mkRequestPOST(data),
          success: function(data, textStatus, xhr) {
            $('#calendar').fullCalendar('refetchEvents');
            $('#calendar').fullCalendar('unselect');
            $('#eventInfoModal').modal('hide');
          },
          error: function(xhr, textStatus, errorThrown) {
            bookings.ajax_error(xhr, textStatus, errorThrown);
            $("#eventInfoStatus").empty();
            $('#eventInfoStatus').append('<p>Failed</p>');
          }
        });
    }
  },
  api_booking_update: function(event) {
    if( bookings.validate_booking() ) {  
        var data = bookings.mkApiBookingData();              
        $.ajax({
          url: bookings.api_root_admin+event.id+"/",
          type: "POST",
          data: bookings.mkRequestPUT(data),
          success: function(data, textStatus, xhr) {
            $('#calendar').fullCalendar('refetchEvents');
            $('#calendar').fullCalendar('unselect');
            $('#eventInfoModal').modal('hide');
          },
          error: function(xhr, textStatus, errorThrown) {
            bookings.ajax_error(xhr, textStatus, errorThrown);
            $("#eventInfoStatus").empty();
            $('#eventInfoStatus').append('<p>Failed</p>');
          }
        });
    }
  },
  api_booking_price_upload: function() {
    if( bookings.validate_booking_price() ) {  
        var data = bookings.mkApiBookingPriceData();              
        $.ajax({
          url: bookings.api_root_admin_price,
          type: "POST",
          data: bookings.mkRequestPOST(data),
          success: function(data, textStatus, xhr) {
            var s = moment( $("#bpStartDateInput").datepicker("getDate") ).format("MMM. D, YYYY");
            var e = moment( $("#bpEndDateInput").datepicker("getDate") ).format("MMM. D, YYYY");
            var p = $("#bpPriceInput").val();
            $('.pricelist-table').append("<tr><td class=\"date-cell\">" + s + " - " + e + "</td><td class=\"price-cell\">&pound;"+p+"</td><tr>");
            $('#bpModal').modal('hide');
          },
          error: function(xhr, textStatus, errorThrown) {
            bookings.ajax_error(xhr, textStatus, errorThrown);
          }
        });
    }
  },

  add_booking: function(start, end) {
    $("#eventInfoModal h4.modal-title").text('Add New Booking');
    $("#eventInfoButton").text('Add');
    $("#eventInfoStatus").empty();
    /* init the form by clearing any previous values.
     * Use the start and end dates from the calendar selection */
    $("#startDateInput").datepicker({
      dateFormat: "yy-mm-dd"
    });
    $("#endDateInput").datepicker({
      dateFormat: "yy-mm-dd",
      onClose: function(dateText, inst) {
        var s = moment( $("#startDateInput").datepicker("getDate") );
        var e = moment(dateText);
        if( e <= s ) {
          $("#endDateInput").addClass("invalidPattern");
        }
      }
    });
    $("#startDateInput").datepicker( "setDate", start.format("YYYY-MM-DD"));
    $("#endDateInput").datepicker( "setDate", end.format("YYYY-MM-DD"));
    $("#nameInput").val('');
    $("#emailInput").val('');
    $("#telInput").val('');
    $("#infoInput").val('');
    $('[name=statusInput] option').filter(function() { 
      return ($(this).text() == 'Booked');
    }).prop('selected', true); 

    /* remove any other click handler and add our update click event handler */
    $("#eventInfoButton").off('click');
    $("#eventInfoButton").click(function() {
      bookings.api_booking_upload();
      return false;
    });
    $("#eventInfoModal").modal('show');
  },
  update_booking: function(event) {
      /* init dialog text */              
      $("#eventInfoModal h4.modal-title").text('Booking');
      $("#eventInfoButton").text('Update');
      /* init the form with the selected event data */              
      $("#startDateInput").datepicker({
        dateFormat: "yy-mm-dd"
      });
      $("#endDateInput").datepicker({
        dateFormat: "yy-mm-dd"
      });
      $("#startDateInput").datepicker( "setDate", event.start.format("YYYY-MM-DD"));
      $("#endDateInput").datepicker( "setDate", event.end.format("YYYY-MM-DD"));
      $("#nameInput").val(event.name);
      $("#emailInput").val(event.email);
      $("#telInput").val(event.tel);
      $("#infoInput").val(event.info);
      $('[name=statusInput] option').filter(function() { 
        return ($(this).text() == event.status);
      }).prop('selected', true); 
      /* remove any other click handler and add our update click event handler */
      $("#eventInfoButton").off('click');
      $("#eventInfoButton").click(function() {
        bookings.api_booking_update(event);
        return false;
      });
      $("#eventInfoModal").modal('show');
  },
  escapeRegex: function(s) {
    return s.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
  },
  dateRe:/^[0-9]{4}-[0-9]{2}-[0-9]{2}$/,
  emailRe:/^([\w-]+(?:\.[\w-]+)*)@((?:[\w-]+\.)*\w[\w-]{0,66})\.([a-z]{2,6}(?:\.[a-z]{2})?)$/i,
  telRe:/^[0-9 -]{7,32}$/,
  priceRe:/^[1-9]{1}[0-9]{0,3}(\.[0-9]{2})$/,
  validate_booking_price: function() {
    var s = moment( $("#bpStartDateInput").datepicker("getDate") ).format("YYYY-MM-DD");
    var e = moment( $("#bpEndDateInput").datepicker("getDate") ).format("YYYY-MM-DD");
    var p = $("#bpPriceInput").val();
    var result = true;
    $('#bpEventInfoStatus').empty();
    if(!bookings.dateRe.test(s)) {
      $('#bpEventInfoStatus').append('<p>Invalid start date</p>');
      result = false;
    }
    if(!bookings.dateRe.test(e)) {
      $('#bpEventInfoStatus').append('<p>Invalid end date</p>');
      result = false;
    }
    if(!bookings.priceRe.test(p)) {
      $('#bpEventInfoStatus').append('<p>Invalid price</p>');
      result = false;
    }
    return result;
  },
  validate_booking: function() {
    var s = moment( $("#startDateInput").datepicker("getDate") ).format("YYYY-MM-DD");
    var e = moment( $("#endDateInput").datepicker("getDate") ).format("YYYY-MM-DD");
    var name = $("#nameInput").val();
    var email = $("#emailInput").val();
    var tel = $("#telInput").val();
    //var info = $("#infoInput").val();

    var result = true;
    $("#eventInfoStatus").empty();
    if(!bookings.dateRe.test(s)) {
      $('#eventInfoStatus').append('<p>Invalid start date</p>');
      result = false;
    }
    if(!bookings.dateRe.test(e)) {
      $('#eventInfoStatus').append('<p>Invalid end date</p>');
      result = false;
    }
    if(!name) {
      $('#eventInfoStatus').append('<p>Invalid name</p>');
      result = false;
    }
    if(!bookings.emailRe.test(email)) {
      $('#eventInfoStatus').append('<p>Invalid email address</p>');
      result = false;
    }
    if(!bookings.telRe.test(tel)) {
      $('#eventInfoStatus').append('<p>Invalid telephone number</p>');
      result = false;
    }
    return result;
  }
}


$(document).ready(function() {
  $('#calendar').fullCalendar({
    header: {
      left: 'prev,next today',
      center: 'title',
    },
    aspectRatio: 2.0,
    eventLimit: false,
    editable: true,
    selectable: true,
    selectHelper: false,
    select: bookings.add_booking,
    eventClick: bookings.update_booking,
    eventSources: [{
      url: bookings.api_root_admin
    }]
  });

  $(".staff-add-price").click(function(){
    $("#bpModal h4.modal-title").text('Add Price');
    $("#addPriceButton").text('Save');

    $("#bpStartDateInput").datepicker({
      dateFormat: "yy-mm-dd"
    });
    $("#bpEndDateInput").datepicker({
      dateFormat: "yy-mm-dd"
    });
    $("#bpStartDateInput").datepicker( "setDate", moment().format("YYYY-MM-DD"));
    $("#bpEndDateInput").datepicker( "setDate", moment().add(1, 'months').format("YYYY-MM-DD"));
    $("#bpPriceInput").val('');

    /* fetch the start date from server... */  
    $.ajax({
      url: "/api/bc/admin/price/",
      type: "GET",
      data: {last: true},
      success: function(data, textStatus, xhr) {
        var end_date = moment(data[0].end);
        $("#bpStartDateInput").datepicker( "setDate", end_date.add(1, 'days').format("YYYY-MM-DD"));
        $("#bpEndDateInput").datepicker( "setDate", end_date.add(1, 'months').format("YYYY-MM-DD"));
        $("#bpModal").modal('show');
      },
      error: function(xhr, textStatus, errorThrown) {
        alert(xhr.status + ": " + xhr.responseText + " ERROR:"+textStatus+" err:"+errorThrown);
      }
    });
  });
  $("#addPriceButton").click(function() {
    /* save start, end dates and price */
    bookings.api_booking_price_upload();
  });
});



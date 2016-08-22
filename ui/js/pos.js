CONFIG = {
  BASE_URL:'http://127.0.0.1:8000',
  CUSTOMERS_URL:'/customers/',
  INVOICES_URL:'/invoices/'
}

$( document ).bind( 'pageinit',  load_page );

function load_page() {

  // $.get(CONFIG.BASE_URL + CONFIG.CUSTOMERS_URL, function(data, e) {
  //   $.each(data, function(index, item) {
  //     $('ul#customer-list').append(
  //       $('<li>').text(item.identifier));
  //   });
  // });
  
  $('#form-customer').validate({
    rules: {
      email: {
        required: true,
        email: true
      }
    },
    messages: {
      email: {
        required: "Please enter an email.",
        email: "Please enter a valid email."
      }
    },
    errorPlacement: function (error, element) {
        error.appendTo(element.parent().prev());
    },
    submitHandler: function(form) {
      submit_customer_form();
      return false;
    }    
  });  
  
  $('#add-customer').click(function(i) {
    $.mobile.changePage(CONFIG.CUSTOMERS_URL + '#customer-create');
  });
  
  function submit_customer_form() {
    $.post(CONFIG.BASE_URL + CONFIG.CUSTOMERS_URL, 
          $('#form-customer').serialize()
    );
    $.mobile.changePage('/customers/#customer-invoices-view');
  }
}


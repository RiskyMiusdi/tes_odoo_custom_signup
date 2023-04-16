odoo.define('account_sign_up_details.account_sign_up_details', function(require) {
    "use strict";

    var ajax = require('web.ajax');
    $(document).ready(function() {
        $('#datepickerinput ').datepicker({
          dateFormat: 'yy-mm-dd',
          yearRange: "-100:+0",
          showButtonPanel: true,
          changeMonth: true,
          changeYear: true,
          showOtherMonths: true,
          selectOtherMonths: true 
        });
    });
});

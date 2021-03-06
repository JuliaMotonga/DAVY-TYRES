$(function() {
    var cal = JSON.parse(servicesCalendar);
    var DAY_LOOKUPS = {'sunday': 0, 'monday': 1, 'tuesday': 2, 'wednesday': 3, 'thursday': 4, 'friday': 5, 'saturday': 6};
    var getUnavailableDays = function(service_id){
        var unavailableDays = [];
        for (var service in cal) {
            if (service_id != cal[service]['id']){
                continue;
            }
            cal[service]['days_of_week'].forEach(function (day){
                for (var key in day){
                    if (!day[key]){
                        unavailableDays.push(DAY_LOOKUPS[key]);
                    }
                }
            });
        }
        return unavailableDays;
    };

    // Initialise datepicker.
    $('#id_booking_day').datepicker({
        beforeShowDay: function(date){
            var day = date.getDay();
            return [(getUnavailableDays($('#id_service').val()).indexOf(day) < 0), date.getDate()];
        },
        minDate: '+1D'
    });

    var setupTimeSlots = function () {
        var $hiddenTimeField = $('#id_booking_time').parent().parent(),
            $slots = $('#service_slots div[data-time]');

        $slots.click(function (){
            var time = $(this).data('time');
            $(this).css({'background-color': '#000000'});
            $(this).siblings().css({'background-color': '#008000'});
            $('#id_booking_time').val(time);
        });
        $('#service_slots').detach().appendTo($hiddenTimeField);
        $('div[data-service]').hide();
    };
    setupTimeSlots();

    $('#id_booking_day').change(function(){
        if ($('#id_service').val() && $('#id_booking_day').val()) {
            var service_id = $('#id_service').val();
            console.log('service_id');
            console.log($('div[data-service=service_id]'));
            $('div[data-service='+service_id+']').show();
        }
    });

    $('#id_service').change(function(){
        $('#service_slots').children().hide();
        setupTimeSlots();
        $('#id_booking_day').trigger('change');
    });
});










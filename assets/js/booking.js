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

    $('#id_booking_time').timepicker({
        onHourShow: function(hour) {

            //for (var service in cal) {
            //    if (service_id == cal[service]['id']){
            //        for (var day in cal[service]['availability']){
            //            if (day == date.getUTCDay()){
            //                var start = cal[service]['availability'][day]['start'],
            //                end = cal[service]['availability'][day]['end'];
            //            }
            //        }
            //    }
            //}

            var selectedDate = $('#id_booking_day').val();
            $('#id_booking_day').val();
        },
        timeFormat: 'hh:mm tt',
        interval: 60,
        minTime: '8:00am',
        maxTime: '6:00pm',
        stepMinute: 30,
        dynamic: true,
        dropdown: true,
        scrollbar: true
    });

});










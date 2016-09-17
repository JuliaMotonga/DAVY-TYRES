$(function() {
    var cal = JSON.parse(servicesCalendar);
    var DAY_LOOKUPS = {'sunday': 0, 'monday': 1, 'tuesday': 2, 'wednesday': 3, 'thursday': 4, 'friday': 5, 'saturday': 6};
    var getUnavailableDays = function(service_id){
        var unavailableDays = [];
        for (var service in cal) {
            if (service_id != cal[service]['id']){
                continue;
            }
            for (var day in cal[service]['availability']){
                var start = cal[service]['availability'][day]['start'],
                    end = cal[service]['availability'][day]['end'],
                    name = cal[service]['availability'][day]['name'];
                if (start == end){
                    unavailableDays.push(DAY_LOOKUPS[name]);
                }
            }
        }
        return unavailableDays;
    };
    $('#id_booking_time').datetimepicker({
        onSelect: function(dateText, inst) {
            var service_id = $('#id_service').val();
            var date = $(this).datepicker('getDate');
            for (var service in cal) {
                if (service_id == cal[service]['id']){
                    for (var day in cal[service]['availability']){
                        if (day == date.getUTCDay()){
                            var start = cal[service]['availability'][day]['start'],
                            end = cal[service]['availability'][day]['end'];
                            console.log(start);
                            console.log(end);
                            //$(this).datetimepicker('option', 'hourMin', start);
                            //$(this).datetimepicker('option', 'hourMax', end);
                        }
                    }
                }
            }
        },
        beforeShowDay: function(date){
            var day = date.getDay();
            return [(getUnavailableDays($('#id_service').val()).indexOf(day) < 0), date.getDate()];
        },
        minDate: '+1D',
        hourMin: 8,
        hourMax: 20,
        stepMinute: 30
    });

});










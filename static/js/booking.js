$(function() {
    var cal = JSON.parse(servicesCalendar);
    var DAY_LOOKUPS = {'sunday': 0, 'monday': 1, 'tuesday': 2, 'wednesday': 3, 'thursday': 4, 'friday': 5, 'saturday': 6};
    var getUnavailableDays = function(service_id){
        var unavailableDays = [];
        var dayOfWeek = date.getUTCDay();

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
            console.log('selected!');
            var date = $(this).datepicker('getDate');
            for (var service in cal) {
                if (service_id == cal[service]['id']){
                    for (var day in cal[service]['availability']){
                        if (day == date.getUTCDay()){
                            $(this).datetimepicker('option', 'hourMin', day);
                            $(this).datetimepicker('option', 'hourMax', day + 1);
                            var start = cal[service]['availability'][day]['start'],
                            end = cal[service]['availability'][day]['end'];
                        }
                    }
                }
            }
        },
        beforeShowDay: function(date){
            var day = date.getDay();
            return [(getUnavailableDays($('#id_service').val()).indexOf(day) < 0), date.getDate()];
        },
        hourMin: 8,
        hourMax: 18,
        stepMinute: 30
    });

});










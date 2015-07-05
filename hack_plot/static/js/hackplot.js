$(document).ready(function(){
    $.getJSON('{% url "hackplot_api:list" %}', function(data){
        console.log('got data');
        $('#hackplot_chart').mapael({
            map : {
                name : "world_countries"
            }
        });
    });
});

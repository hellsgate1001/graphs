$(document).ready(function(){
    $.getJSON($('#hackplot_chart').attr('data-url'), function(data){
        geoPlots = {};
        $.each(data.results, function(index, result){
            newPlot = {
                type: 'circle',
                size: 5,
                latitude: result.latitude,
                longitude: result.longitude,
                attrs: {
                    opacity: 1
                },
                tooltip: {
                    content: '<span style="font-weight: bold;">' + result.ip_address + '</span><br/>' + result.attempts.length
                }
            }
            geoPlots[result.ip_address] = newPlot
        });

        $('#hackplot_chart').mapael({
            map : {
                name : "world_countries"
            },
            plots: geoPlots
        });
    });
});

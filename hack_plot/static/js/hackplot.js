$(document).ready(function(){
    $.getJSON($('#hackplot_chart').attr('data-url'), function(data){
        geoPlots = {};
        $.each(data.results, function(index, result){
            newPlot = {
                latitude: result.latitude,
                longitude: result.longitude,
                tooltip: {
                    content: '<span style="font-weight: bold;">' + result.ip_address + '</span><br/>' + result.attempts.length
                }
            }
            geoPlots[result.ip_address] = newPlot
        });

        $('#hackplot_chart').mapael({
            map : {
                name : "world_countries",
                defaultPlot: {
                    type: 'circle',
                    size: 5,
                    attrs: {
                        opacity: 1
                    },
                    attrsHover: {
                            'stroke-width': 0,
                        fill: '#8ABEDE'
                    }
                },
                defaultArea: {
                    attrsHover: {
                        fill: '#343434'
                    }
                }
            },
            plots: geoPlots
        });
    });
});
// $('#hackplot_chart').trigger('update', [{}, {new_plt}, {}, {}]

function getIpDiv(ip_address) {
    ipDiv = $('<div>').addClass('ipinfo');
    ipSpan = $('<p>').text(ip_address.ip_address).css('font-weight','bold');
    totalSpan = $('<p>').text(ip_address.attempts.length + ' attempts');
    $(ipDiv).append(ipSpan, totalSpan);
    return ipDiv;
}

function getLocationTitle(location) {
    if (location.city != '') {
        locationTitle = location.city;
    } else if (location.region_name != '') {
        locationTitle = location.region_name;
    } else {
        locationTitle = 'N/A';
    }
    locationTitle += ', ' + location.country_name;

    return locationTitle;
}

$(document).ready(function(){
    $('#hackplot_chart').mapael({
        map : {
            name : "world_countries",
            defaultPlot: {
                type: 'circle',
                size: 8,
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
            },
            afterInit : function(container, paper, areas, plots, options) {
                $('#hackplot_chart').resize();
            }
        }
    });

    $.getJSON($('#hackplot_chart').attr('data-url'), function(data){
        geoPlots = {};
        $.each(data, function(index, result){
            var ipinfo = $('<div>').append(
                $('<h5>').text(getLocationTitle(result))
            );
            $.each(result.ip_addresses, function(idx, ip_address){
                ipinfo.append(getIpDiv(ip_address));
            });

            newPlot = {
                latitude: result.latitude,
                longitude: result.longitude,
                tooltip: {
                    content: ipinfo
                }
            }
            geoPlots[result.longitude + ',' + result.latitude] = newPlot
        });

        // Add the plots to the map
        $('#hackplot_chart').trigger('update', [{}, geoPlots, {}, {}]);
    });
});

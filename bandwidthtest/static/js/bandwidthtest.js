function getDownloads(days) {
    num = days.length;
    dls = []
    for (i = 0; i < num; ++i) {
        dls.push(parseFloat(days[i].dlspeed__avg));
    }
    return dls;
}

function getUploads(days) {
    num = days.length;
    uls = []
    for (i = 0; i < num; ++i) {
        uls.push(parseFloat(days[i].ulspeed__avg));
    }
    return uls;
}

$().ready(function(){
    $.getJSON($('#bandwidth_chart').attr('data-url'), function(data){
        downloads = getDownloads(data.results);
        uploads = getUploads(data.results);

        chart = new Highcharts.Chart({
            chart: {
                renderTo: 'bandwidth_chart',
                type: 'area'
            },
            title: {
                text: 'Bandwidth Available'
            },
            xAxis: {
                categories: ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
                tickInterval: 1
            },
            yAxis: {
                title: {
                    text: 'Usage MB'
                },
                min: 0,
                max: 15
            },
            series: [{
                name: 'Download',
                data: downloads
            }, {
                name: 'Upload',
                data: uploads
            }]
        });
    });



});

$().ready(function(){
    $('#bandwidth_chart').highcharts({
        chart: {
            type: 'area-basic'
        },
        title: {
            text: 'Bandwidth Use'
        },
        xAxis: {
            labels: {
                format: '{value}MB'
            }
        },
        yAxis: {
            title: {
                text: 'Day'
            },
            labels: {
                ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
            }
        },
        plotOptions: {
            area: {
                pointStart: 'Monday',
                marker: {
                    enabled: false,
                    symbol: 'circle',
                    radius: 2,
                    states: {
                        hover: {
                            enabled: true
                        }
                    }
                }
            }
        },
        series: [
            {
                name: 'Download',
                data: [12.75, 10.15, 11.95, 12.15, 12.8, 9.1, 10.95]
            },
            {
                name: 'Upload',
                data: [0.85, 0.8, 0.85, 0.75, 0.8, 0.75, 0.85]
            }
        ]
    });
});

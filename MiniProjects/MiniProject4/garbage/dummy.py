import * as echarts from 'echarts';

var chartDom = document.getElementById('main');
var myChart = echarts.init(chartDom);
var option;

option = {
    series: [
    ],
};

setInterval(function() {
    let random = (Math.random() * 60).toFixed(2) - 0;
    option.series[0].data[0].value = random;
    option.series[1].data[0].value = random;
    myChart.setOption(option, true);
}, 2000);

option && myChart.setOption(option);

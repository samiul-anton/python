
       let received_data = null;
       
        CPUChart = echarts.init(document.getElementById('cpu'));

        cpu_chart = {
            legend:{
                show:true,
                data:[]
            },
            title:{
                text:"CPU"
            },
            xAxis: {
                type: 'category',
                data: []
            },
            yAxis: {
                type: 'value',
                min:0,
                max:100
            },
            series: []
        };

        LoadChart = echarts.init(document.getElementById('load'));

        load_chart = {
            legend:{
                show:true,
                data:[]
            },
            title:{
                text:"Load Averages"
            },
            xAxis: {
                type: 'category',
                data: []
            },
            yAxis: {
                type: 'value',
                min:0,
                max:100
            },
            series: []
        };


        MemoryChart = echarts.init(document.getElementById('memory'));
        memory_chart = {
            title:{
                text:"Memory Utilization"
            },
            xAxis: {
                type: 'category',
                data: []
            },
            yAxis: {
                min:0,
                max:100,
                type: 'value'
            },
            series: [{
                data: [],
                type: 'bar',
                showBackground: true,
                backgroundStyle: {
                    color: 'rgba(220, 220, 220, 0.8)'
                }
            }]
        };

        DiskChart = echarts.init(document.getElementById('disk'));
        disk_chart = {
            title:{
                text:"Disk Utilization"
            },
            xAxis: {
                type: 'category',
                data: []
            },
            yAxis: {
                min:0,
                max:100,
                type: 'value'
            },
            series: [{
                data: [],
                type: 'bar',
                showBackground: true,
                backgroundStyle: {
                    color: 'rgba(220, 220, 220, 0.8)'
                }
            }]
        };

        SignalChart = echarts.init(document.getElementById('signal'));
        signal_chart = {
            legend:{
                show:true,
                data:[]
            },
            title:{
                text:"SIGNAL_Strength"
            },
            xAxis: {
                type: 'category',
                data: []
            },
            yAxis: {
                type: 'value',
                min:0,
                max:100
            },
            series: []
        };

        TrafficChart = echarts.init(document.getElementById('traffic'));

        traffic_chart = {
            legend:{
                show:true,
                data:[]
            },
            title:{
                text:"Network_Traffic"
            },
            xAxis: {
                type: 'category',
                data: []
            },
            yAxis: {
                type: 'value',
                min:0,
                max:20
            },
            series: []
        };
        Faren_Chart = echarts.init(document.getElementById('faren'));
        var option;
        option = {
            series: [{
                    type: 'gauge',
                    center: ["50%", "60%"],
                    startAngle: 200,
                    endAngle: -20,
                    min: 0,
                    max: 60,
                    splitNumber: 12,
                    itemStyle: {
                        color: '#FFAB91'
                    },
                    progress: {
                        show: true,
                        width: 30
                    },

                    pointer: {
                        show: false,
                    },
                    axisLine: {
                        lineStyle: {
                            width: 30
                        }
                    },
                    axisTick: {
                        distance: -45,
                        splitNumber: 5,
                        lineStyle: {
                            width: 2,
                            color: '#999'
                        }
                    },
                    splitLine: {
                        distance: -52,
                        length: 14,
                        lineStyle: {
                            width: 3,
                            color: '#999'
                        }
                    },
                    axisLabel: {
                        distance: -20,
                        color: '#999',
                        fontSize: 20
                    },
                    anchor: {
                        show: true
                    },
                    title: {
                        show: false
                    },
                    detail: {
                        valueAnimation: true,
                        width: '70%',
                        lineHeight: 40,
                        height: '15%',
                        borderRadius: 8,
                        offsetCenter: [0, '-15%'],
                        fontSize: 60,
                        fontWeight: 'bolder',
                        formatter: '{value} °C',
                        color: 'auto'
                    },
                    data: [{
                        value: 79
                    }]
            }]
        };

        function populateData(received_data){
            if(received_data == null){return;}

            if(disk_chart.xAxis.data.length == 0){
                disk_chart.xAxis.data.push(received_data["time"]);
                disk_chart.series[0].data.push(received_data["disk_utilized"]);
            }
            else{
                disk_chart.xAxis.data[0] = received_data["time"];
                disk_chart.series[0].data[0] = received_data["disk_utilized"];
            }

            DiskChart.setOption(disk_chart);

            if(memory_chart.xAxis.data.length == 0){
                memory_chart.xAxis.data.push(received_data["time"]);
                memory_chart.series[0].data.push(received_data["virtual_memory_utilized"]);
            }
            else{
                memory_chart.xAxis.data[0] = received_data["time"];
                memory_chart.series[0].data[0] = received_data["virtual_memory_utilized"];
            }

            MemoryChart.setOption(memory_chart);

            cpu_chart.xAxis.data.push(received_data["time"]);
            series_created = false
            if(cpu_chart.series.length > 0){
                series_created = true
            }
            for (const [key, value] of Object.entries(received_data["cpu"])) {
                if(!series_created){
                    temp_obj = {'name':key, 'type': 'line', 'data':[value]};
                    cpu_chart.series.push(temp_obj);
                    new_val = key;
                    cpu_chart.legend.data.push(new_val);
                }
                else{
                    for(i = 0; i < cpu_chart.series.length; ++i){
                        if(cpu_chart.series[i]["name"] == key){
                            cpu_chart.series[i].data.push(value);
                            break;
                        }
                    }
                }
            }
            CPUChart.setOption(cpu_chart);

            load_chart.xAxis.data.push(received_data["time"]);
            series_created = false
            if(load_chart.series.length > 0){
                series_created = true
            }
            for (const [key, value] of Object.entries(received_data["load_avg"])) {
                if(!series_created){
                    temp_obj = {'name':key, 'type': 'line', 'data':[value]};
                    load_chart.series.push(temp_obj);
                    new_val = key;
                    load_chart.legend.data.push(new_val);
                }
                else{
                    for(i = 0; i < load_chart.series.length; ++i){
                        if(load_chart.series[i]["name"] == key){
                            load_chart.series[i].data.push(value);
                            break;
                        }
                    }
                }
            }
            LoadChart.setOption(load_chart);

            signal_chart.xAxis.data.push(received_data["time"]);
            series_created = false
            if(signal_chart.series.length > 0){
                series_created = true
            }
            for (const [key, value] of Object.entries(received_data["signal"])) {
                 if(!series_created){
                     temp_obj = {'name':key, 'type': 'line', 'data':[value]};
                     signal_chart.series.push(temp_obj);
                     new_val = key;
                     signal_chart.legend.data.push(new_val);
                 }
                 else{
                      for(i = 0; i < signal_chart.series.length; ++i){
                          if(signal_chart.series[i]["name"] == key){
                              signal_chart.series[i].data.push(value);
                              break;
                          }
                      }
                 }
            }
            SignalChart.setOption(signal_chart);

            traffic_chart.xAxis.data.push(received_data["time"]);
            series_created = false
            if(traffic_chart.series.length > 0){
                series_created = true
            }
            for (const [key, value] of Object.entries(received_data["traffic"])) {
                if(!series_created){
                    temp_obj = {'name':key, 'type': 'line', 'data':[value]};
                    traffic_chart.series.push(temp_obj);
                    new_val = key;
                    traffic_chart.legend.data.push(new_val);
                }
                else{
                    for(i = 0; i < traffic_chart.series.length; ++i){
                        if(traffic_chart.series[i]["name"] == key){
                            traffic_chart.series[i].data.push(value);
                            break;
                        }
                    }
                }
            }
            TrafficChart.setOption(traffic_chart);

            setInterval(function() {
                let random = (Math.random() * 60).toFixed(2) - 0;
                option.series[0].data[0].value = random;
                Faren_Chart.setOption(option, true);
            }, 2000);
        }

        window.setInterval(function () {
            socket = new WebSocket("ws://localhost:8765");
            socket.onmessage = function(event) {
              populateData(JSON.parse(event.data));
            };
            socket.onopen = function(event){
                socket.send("");
            }
        }, 1000);

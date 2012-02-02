function updatedatalist(graph, metadata){
    $.getJSON("/metadata.json", function(entries){
        datalist = $("#datalist>tbody");
        datalist.empty("");
        
        entries.forEach(function(entry){
            var tr = $(document.createElement("tr"));
            var td0 = $(document.createElement("td"));
            var td1 = $(document.createElement("td"));
            var td2 = $(document.createElement("td"));
            var td3 = $(document.createElement("td"));
            var td4 = $(document.createElement("td"));
            var td5 = $(document.createElement("td"));
            var td6 = $(document.createElement("td"));

            tr.append(td0);
            tr.append(td1);
            tr.append(td2);
            tr.append(td3);
            tr.append(td4);
            tr.append(td5);
            tr.append(td6);
            
            td0.text(entry.host);
            td1.text(entry.plugin);
            td2.text(entry.plugin_instance);
            td3.text(entry.type);
            td4.text(entry.type_instance);
            td5.text(entry.dsname);
            td6.text(entry.dstype);

            tr.css("cursor", "pointer");
            
            var active = false;
            tr.click(function(){
                if(active){
                    active = false;
                    delete metadata[entry.id];
                    tr.css("background-color", "transparent");
                    updategraph(graph, metadata);
                } else {
                    active = true;
                    metadata[entry.id] = entry;
                    tr.css("background-color", "#CCA");
                    updategraph(graph, metadata);
                }
                
            });

            datalist.append(tr);
        });
    });
};




function updategraph(graph, metadata, start, end){
    var id_list = Array();
    var labels = Array();
    for(id in metadata){
        labels.push(String(metadata[id].id));
        id_list.push(metadata[id].id);
    }
    var getparams = {};
    getparams["id"] = id_list.join(",");
    
    if (typeof start !== "undefined")
        getparams["start"] = String(start);
    
    if (typeof end !== "undefined")
        getparams["end"] = String(end);


    $.getJSON("/data.json", getparams, function(data){
        var gdata = Array();
        data.forEach(function(v){
            gdata.push({label: "test", data: v});
        });
        var options = {
            series: {
                lines: { show: true },
                points: { show: false }
            },
            legend: { noColumns: 2 },
            xaxis: { mode: "time", ticks: 5 },
            selection: { mode: "x", color: "#00A" },
        }
        var plot = $.plot(graph, gdata, options);
    });
}


$(function(){
    var graph = $("#graph");
    var metadata = Object();

    graph.bind("plotselected", function (event, ranges) {
        updategraph(graph, metadata, ranges.xaxis.from, ranges.xaxis.to);
    });
    updategraph(graph, metadata);
    updatedatalist(graph, metadata);
});


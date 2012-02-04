(function($){
    
    var by_host = new Object();
    
    $.bind("del_metadata", function(event){
        
    });
    $.bind("new_metadata", function(event){
        var m = event.metadata;
        if(m.plugin !== "load")
            return;

        if(m.dsname !== "longterm")
        if(m.dsname !== "midterm")
        if(m.dsname !== "shortterm")
            return;

        console.log(m);
    });
})(jQuery);

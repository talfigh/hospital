$(function(){
   $(".table-expandable").on("click", "tbody tr:not(.expandable)", function(){
       var next_tr = $(this).next("tr");
       var is_expanded = next_tr.hasClass("expanded");
       $(".table-expandable").find(".expandable").removeClass("expanded");

       if (next_tr.hasClass("expandable")) {
           if (is_expanded) {
               next_tr.removeClass("expanded");
           } else {
               next_tr.addClass("expanded");
           }
       }
   })
});
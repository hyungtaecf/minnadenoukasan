$(document).ready(function () {
    resize_to_fit();
});

function resize_to_fit($element=null){
  if($element==null){
    $('div.outer h1').each(function(){
      $element=$(this)
      if($element.height()>$element.closest(".outer").height()){
        var fontsize = $element.css('font-size');
        $element.first().css('fontSize', parseFloat(fontsize) - 1);
        resize_to_fit($element);
      }
    })
  }
  else{
    if($element.height()>$element.closest(".outer").height()){
      var fontsize = $element.css('font-size');
      $element.first().css('fontSize', parseFloat(fontsize) - 1);
      resize_to_fit($element);
    }
  }
}

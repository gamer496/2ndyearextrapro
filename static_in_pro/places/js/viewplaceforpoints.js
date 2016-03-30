$(document).ready(function(){
  $(".mark-right").click(function(event){
    var ele=this
    event.preventDefault()
    var mark_type='right'
    function getCookie(c_name) {
    if(document.cookie.length > 0) {
        c_start = document.cookie.indexOf(c_name + "=");
        if(c_start != -1) {
            c_start = c_start + c_name.length + 1;
            c_end = document.cookie.indexOf(";", c_start);
            if(c_end == -1) c_end = document.cookie.length;
            return unescape(document.cookie.substring(c_start,c_end));
        }
    }
    return "";
}

$(function () {
    $.ajaxSetup({
        headers: {
            "X-CSRFToken": getCookie("csrftoken")
        }
    });
});
    var url=$("a.mark-right").attr('href')
  if($(this).hasClass('selected')){
      var vote_action='recall-vote';
      elem=$(this)
      $.ajax({
        url : url,
        type: 'POST',
        contentType: 'application/json; charset=utf-8',
        dataType:'text',
        data: JSON.stringify({type:mark_type,action:vote_action}),
        success:function(result){
            // alert(result)
          if($.isNumeric(result)){
            $(elem).removeClass('selected');
            $(elem).addClass('not-selected');
            $(elem).html("Mark as right "+result);
          }
        }
      });
    }
    else {
      var vote_action='vote';
      elem=$(this)
      $.ajax({
        url : url,
        type: 'POST',
        contentType:   'application/json; charset=utf-8',
        dataType:  'text',
        data: JSON.stringify({type:mark_type,action:vote_action}),
        success:  function(result){
            // alert(result);
          if($.isNumeric(result)){
            $(elem).removeClass('not-selected');
            $(elem).addClass('selected');
            $(elem).html("Marked as right "+result);
          }
        }
      });
    }
  });

$(".mark-wrong").click(function(event){
    var ele=this
    event.preventDefault();
    var mark_type='wrong';
    var url=$(ele).attr('href')
    function getCookie(c_name) {
    if(document.cookie.length > 0) {
        c_start = document.cookie.indexOf(c_name + "=");
        if(c_start != -1) {
            c_start = c_start + c_name.length + 1;
            c_end = document.cookie.indexOf(";", c_start);
            if(c_end == -1) c_end = document.cookie.length;
            return unescape(document.cookie.substring(c_start,c_end));
        }
    }
    return "";
}

$(function () {
    $.ajaxSetup({
        headers: {
            "X-CSRFToken": getCookie("csrftoken")
        }
    });
});
    if($(this).hasClass('selected')){
      var vote_action='recall-vote';
      elem=$(this)
      $.ajax({
        url : url,
        type: 'POST',
        contentType: 'application/json; charset=utf-8',
        dataType:'text',
        data: JSON.stringify({type:mark_type,action:vote_action}),
        success:function(result){
            // alert(result);
          if($.isNumeric(result)){
            $(elem).removeClass('selected')
            $(elem).addClass('not-selected')
            $(elem).html("Mark as wrong "+result);
          }
        }
      });
    }
    else {
      var vote_action='vote';
      elem=$(this)
      $.ajax({
        url : url,
        type: 'POST',
        contentType:   'application/json; charset=utf-8',
        dataType:  'text',
        data: JSON.stringify({type:mark_type,action:vote_action}),
        success:  function(result){
            // alert(result)
          if($.isNumeric(result)){
            $(elem).removeClass('not-selected');
            $(elem).addClass('selected');
            $(elem).html("Marked as wrong "+result);
          }
        }
      });
    }
  });
});

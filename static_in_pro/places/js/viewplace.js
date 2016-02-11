$(document).ready(function(){
  $(".vote-up").click(function(){
    var ele=this
    $(ele).parent().addClass("bump");
    var id=place_id;
    var vote_type='up'
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
        data: JSON.stringify({id:id,type:vote_type,action:vote_action}),
        success:function(result){
          if($.isNumeric(result)){
            $(elem).removeClass('selected').removeClass('incremented');
            $(elem).addClass('increment');
            $('div.count').html(result);
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
        data: JSON.stringify({id:id,type:vote_type,action:vote_action}),
        success:  function(result){
          if($.isNumeric(result)){
            $(elem).removeClass('increment');
            $(elem).addClass('incremented').addClass('selected');
            $('div.count').html(result);
          }
        }
      });
    }

    setTimeout(function(){
      $(ele).parent().removeClass("bump");
    }, 400);
  });

  $(".vote-down").click(function(){
    var ele=this
    $(ele).parent().addClass("bump");
    var id=place_id;
    var vote_type='down'
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
        data: JSON.stringify({id:id,type:vote_type,action:vote_action}),
        success:function(result){
          if($.isNumeric(result)){
            $(elem).removeClass('selected').removeClass('incremented');
            $(elem).addClass('increment');
            $('div.count').html(result);
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
        data: JSON.stringify({id:id,type:vote_type,action:vote_action}),
        success:  function(result){
          if($.isNumeric(result)){
            $(elem).removeClass('increment');
            $(elem).addClass('incremented').addClass('selected');
            $('div.count').html(result);
          }
        }
      });
    }

    setTimeout(function(){
      $(ele).parent().removeClass("bump");
    }, 400);
  });
});

$(function(){

  $('.strong').hover(
    function(){
      $(this).find('p').slideDown();
    },
    function(){
      $(this).find('p').slideUp();
    }
  );

  $('.btn').hover(
    function(){
      $(this).css('font-size','20px');
    },
    function(){
      $(this).css('font-size','15px');
    }
  );

  $('.btn2').hover(
    function(){
      $(this).css('font-size','20px');
    },
    function(){
      $(this).css('font-size','15px');
    }
  );

  $('.btn').click(function(){
    $('.modal').show(1000);
  });

  $('.fa-times').click(function(){
    $('.modal').hide(1000);
  });

  $('.fa-arrow-up').click(function(){
    $('html,body').animate({
      'scrollTop':0
    },500);
  });

  $('.fa-arrow-up').hover(
    function(){
      $('#scroll').fadeIn();
    },
    function(){
      $('#scroll').fadeOut();
    }
  );



});
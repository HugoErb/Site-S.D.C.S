
/* jQuery Pre loader
 -----------------------------------------------*/
$(window).load(function () {
  $('.preloader').fadeOut(1000); // set duration in brackets    
});


/* HTML document is loaded. DOM is ready. 
-------------------------------------------*/
$(document).ready(function () {

  /* template navigation
  -----------------------------------------------*/
  var navHeight = $('.navbar-fixed-top').outerHeight();
  $('.main-navigation').onePageNav({
    scrollThreshold: 0.2,
    scrollOffset: navHeight,
    filter: ':not(.external)',
    changeHash: true
  });

  /* Navigation visible on Scroll */
  mainNav();
  $(window).scroll(function () {
    mainNav();
  });

  function mainNav() {
    var top = (document.documentElement && document.documentElement.scrollTop) || document.body.scrollTop;
    if (top > 40) $('.sticky-navigation').stop().animate({
      "opacity": '1',
      "top": '0'
    });
    else $('.sticky-navigation').stop().animate({
      "opacity": '0',
      "top": '-75'
    });
  }


  /* Hide mobile menu after clicking on a link
   -----------------------------------------------*/
  $('.navbar-collapse a').click(function () {
    $(".navbar-collapse").collapse('hide');
  });


  /*  smoothscroll
  ----------------------------------------------*/
  $(function () {
    $('.navbar-default a, #home a, #overview a').bind('click', function (event) {
      var $anchor = $(this);
      $('html, body').stop().animate({
        scrollTop: $($anchor.attr('href')).offset().top - 49
      }, 1000);
      event.preventDefault();
    });
  });


  /* Parallax section
     -----------------------------------------------*/
  function initParallax() {
    $('#home').parallax("100%", 0.1);
    $('#overview').parallax("100%", 0.3);
    $('#team').parallax("100%", 0.2);
    $('#adhesion').parallax("100%", 0.3);
    $('#calendar').parallax("100%", 0.1);
    $('#contact').parallax("100%", 0.2);
    $('#testimonial').parallax("100%", 0.2);

  }
  initParallax();


  /* home slider section
 -----------------------------------------------*/
 $(function () {
    const imagePaths = [
      "images/home-bg-slider-img1.jpg",
      "images/home-bg-slider-img2.jpg",
      "images/home-bg-slider-img3.jpg"
    ];
  
    const imageAlts = imagePaths.map(path => {
      const fileName = path.split('/').pop();
      return fileName.replace(/\.[^/.]+$/, ''); // supprime l'extension
    });
  
    $('#home').backstretch(imagePaths, {
      duration: 5000,
      fade: 750,
      before: function (index, $img) {
        // Si une image est déjà dans le DOM, modifie son alt
        $(".backstretch img").attr("alt", imageAlts[index]);
      },
      after: function () {
        // S'assurer que l'alt est bien appliqué à la première image
        $(".backstretch img").attr("alt", imageAlts[0]);
      }
    });
  });


  /* Owl Carousel
  -----------------------------------------------*/
  $(document).ready(function () {
    $("#owl-testimonial").owlCarousel({
      autoPlay: 6000,
      items: 1,
      itemsDesktop: [1199, 1],
      itemsDesktopSmall: [979, 1],
      itemsTablet: [768, 1],
      itemsTabletSmall: false,
      itemsMobile: [479, 1],
    });
  });


  /* wow
  -------------------------------*/
  new WOW({ mobile: false,
    offset: 50 }).init();

});


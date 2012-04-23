(function() {

  jQuery(function($) {
    var currentTab, interval, pitch, tabs, timer;
    $(".carousel").not(".inactive").carousel({
      interval: 7500
    });
    tabs = $('a[data-toggle="tab"]').on('show', function(e) {
      var link, slideNumber;
      link = $(this);
      if (link.attr("data-slide-number") != null) {
        slideNumber = parseInt(link.attr("data-slide-number"), 10);
        if (slideNumber != null) {
          return $(".carousel").first().carousel(slideNumber).carousel('pause');
        }
      }
    });
    currentTab = 0;
    timer = function() {
      currentTab += 1;
      if (currentTab >= tabs.length) currentTab = 0;
      return tabs.slice(currentTab, currentTab + 1).trigger("click");
    };
    interval = setInterval(timer, 7500);
    pitch = $("#tabbed-pitch");
    pitch.on("mouseenter", function() {
      return interval = clearInterval(interval);
    });
    return pitch.on("mouseleave", function() {
      return interval = setInterval(timer, 7500);
    });
  });

}).call(this);

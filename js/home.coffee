jQuery(($) ->
  $(".carousel").not(".inactive").carousel(interval: 7500)
  tabs = $('a[data-toggle="tab"]').on('show', (e) ->
    link = $(this)
    if link.attr("data-slide-number")?
      slideNumber = parseInt(link.attr("data-slide-number"), 10)
      if slideNumber?
        $(".carousel").first().carousel(slideNumber).carousel('pause')
  )

  currentTab = 0
  timer = ->
    currentTab += 1
    if currentTab >= tabs.length
      currentTab = 0
    tabs.slice(currentTab, currentTab + 1).trigger("click")

  interval = setInterval(timer, 7500)

  pitch = $("#tabbed-pitch")
  pitch.on("mouseenter", ->
    interval = clearInterval(interval)
  )
  pitch.on("mouseleave", ->
    interval = setInterval(timer, 7500)
  )
)

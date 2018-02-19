---
layout: default
title: Projects
tagline: "None"
permalink: "/projects/"
cover: /media/homepage_banner.jpg
---

<h1 class="top-text">The YTEditor</h1>

<center>
    <img class="imageSlide" src="/assets/images/yteditor_scene_blue.png">
    <img class="imageSlide" src="/assets/images/yteditor_scene_mixed.png">
    <img class="imageSlide" src="/assets/images/yteditor_particles.png">
</center>

<script>
    var slideIndex = 1;
    carousel();

    function carousel() {
        var i;
        var x = document.getElementsByClassName("imageSlide");
        for (i = 0; i < x.length; i++) {
            x[i].style.display = "none";
        }
        slideIndex++;
        if (slideIndex > x.length) { slideIndex = 1 }
        x[slideIndex - 1].style.display = "block";
        setTimeout(carousel, 2000); // Change image every 2 seconds
    }
</script>


<!-- please do not remove this line -->
<div style='display:none;'>
<a href='http://www.commercekitchen.com'>ipsum generator</a>
</div>
<!-- end whedon ipsum code -->
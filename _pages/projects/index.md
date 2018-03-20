---
layout: default
title: Projects
tagline: "None"
permalink: "/projects/"
cover: /media/homepage_banner.jpg
---

<h1 font-size="28px" margin-bottom="8px" margin-top="30px" align="left">
    <a>
        The YTEditor
    </a>
</h1>

<iframe width="800px" height="600px">
  src="https://www.youtube.com/embed/pLOTF1rBFBo">
</iframe>

<center>
    <img class="imageSlide" src="/media/yteditor_scene_blue.png">
    <img class="imageSlide" src="/media/yteditor_scene_mixed.png">
    <img class="imageSlide" src="/media/yteditor_particles.png">
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

<p>Built with <a href="https://www.qt.io/">Qt</a>, the YTEditor is a level editor built for a 3D component-based game engine.</p>


<h1 font-size="28px" margin-bottom="8px" margin-top="130px" align="left">Perforce GUI</h1>
<p>An application that streamlines the use of Perforce for content creators.</p>

<h1 font-size="28px" margin-bottom="8px" margin-top="130px" align="left">Lamb Planet</h1>
<p>A 3D sailing game focused on exploration and narrative.</p>

<!-- please do not remove this line -->
<div style='display:none;'>
<a href='http://www.commercekitchen.com'>ipsum generator</a>
</div>
<!-- end whedon ipsum code -->
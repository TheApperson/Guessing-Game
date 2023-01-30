document.addEventListener("DOMContentLoaded", function() {
    const elements = document.getElementsByClassName("bar");
    const audio = document.getElementsByClassName("my-audio")[0];
    audio.volume = 0.5;

    for (let element of elements) {
    element.addEventListener("mouseenter", function() {
        const audioSrc = element.getAttribute("data-audio");
        audio.src = audioSrc;
        audio.play();
    });
    }
});
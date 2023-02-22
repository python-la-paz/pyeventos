function pauseButton(slug) {
	var vid = document.getElementById("bgvid-" + slug);
	var pauseButton = document.querySelector("#polina-" + slug + " button");
	vid.classList.toggle("stopfade");
	vid.addEventListener('ended', function () {
		// only functional if "loop" is removed 
		vid.pause();
		// to capture IE10
		vid.classList.add("stopfade");
	});
	if (vid.paused) {
		vid.play();
		pauseButton.innerHTML = "<i class='lni lni-pause'></i>";
	} else {
		vid.pause();
		pauseButton.innerHTML = "<i class='lni lni-play'></i>";
	}
}
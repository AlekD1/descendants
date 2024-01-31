new Swiper(".swiper", {
	navigation: {
		nextEl: ".swiper-prev",
		prevEl: ".swiper-next",
	},
	pagination: {
		el: ".swiper-pag",
		type: "fraction",
		renderBullet: function (currentClass, totalClass) {
			return `<span class="'${currentClass}'"></span> из <span class="'${totalClass}'"></span>`;
		},
	},
	simulateTouch: false,
	slidesPerView: 3,
	spaceBetween: 20,
	loop: true,
	breakpoints: {
		320: {
			slidesPerView: 1,
		},
		800: {
			slidesPerView: 2,
		},
		900: {
			spaceBetween: 20,
			slidesPerView: 3,
		},
		2300: {
			slidesPerView: 1,
		},
	},
});

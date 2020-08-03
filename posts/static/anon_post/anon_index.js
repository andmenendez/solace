// window.addEventListener('scroll', function(e)
// {	
// 	if (window.scrollY !== 0)
// 	{
// 		document.querySelector("#solace_title").style.fontSize = "72px"
// 	}
// 	else
// 	{
// 		document.querySelector("#solace_title").style.fontSize = "144px"
// 	}
// });

document.querySelector(".nav_button").addEventListener("click", function() 
{
	if (this.classList.contains("nav_button_active"))
	{
		closeNavMenu();
	} else {
		openNavMenu();
	}
});

function openNavMenu()
{	
	document.querySelector(".nav_button").classList.add("nav_button_active");
	document.querySelectorAll(".nav_button_bar")[1].classList.add("nav_button_bar_active");
	let nav_menu_items = document.querySelectorAll(".nav_menu_item");
	for (let i = 0; i < nav_menu_items.length; i++)
	{
		nav_menu_items[i].classList.add("nav_menu_item_active");
	}
}

function closeNavMenu()
{	
	document.querySelector(".nav_button").classList.remove("nav_button_active");
	document.querySelectorAll(".nav_button_bar")[1].classList.remove("nav_button_bar_active");
	let nav_menu_items = document.querySelectorAll(".nav_menu_item");
	for (let i = 0; i < nav_menu_items.length; i++)
	{
		nav_menu_items[i].classList.remove("nav_menu_item_active");
	}
}
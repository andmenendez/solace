window.onload = function() 
{
	document.querySelector(".nav_button").addEventListener("click", function() 
	{
		if (this.classList.contains("nav_button_active"))
		{
			closeNavMenu();
		} else {
			openNavMenu();
		}
	});

	document.querySelector("#anon_button").addEventListener("click", function() 
	{
		if (document.querySelector("#anon_post_body").value == "")
		{
			document.querySelector("#anon_post_body").focus();
		}
		else if (document.querySelector("#anon_post_contactid").value == "")
		{
			document.querySelector("#anon_post_contactid").focus();
		}
		else
		{
			console.log("FORM COMPLETE")
			document.querySelector("#anon_post_form").submit();
		}
	})

	document.addEventListener("keypress", function(e){
		if (e.code == "Enter") 
		{
			if (document.querySelector("#anon_post_body").value == "")
			{
				document.querySelector("#anon_post_body").focus();
			}
			else if (document.querySelector("#anon_post_contactid").value == "")
			{
				document.querySelector("#anon_post_contactid").focus();
			}
			else
			{
				console.log("FORM COMPLETE")
				document.querySelector("#anon_post_form").submit();
			}
		}

	})
}

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
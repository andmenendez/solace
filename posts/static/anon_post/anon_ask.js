
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

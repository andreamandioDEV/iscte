
var page = location.pathname.substring(1);

if (page == ''){
	document.getElementById('index').className += " a-active";
}else{
	document.getElementById(page).className += " a-active";
}


/*var collapse = $('button.navbar-toggle')
collapse.click(function(){
	menu = document.getElementById("bs-example-navbar-collapse-1")
	if (menu.className == "navbar-collapse collapse in"){
		menu.className = 'navbar-collapse collapse';
		menu.setAttribute("aria-expanded", 'false');
		collapse.attr("aria-expanded","false");
		collapse.css("navbar-toggle collapsed")
	}else{
		menu.className = 'navbar-collapse collapse in';
		menu.setAttribute("aria-expanded", 'true');
		collapse.attr("aria-expanded","true");
		collapse.css("navbar-toggle")
	}
});
*/
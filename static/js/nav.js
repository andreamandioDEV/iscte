var page = location.pathname.substring(1);

if (page == ''){
	document.getElementById('index').className += " a-active";
}else{
	document.getElementById(page).className += " a-active";
}

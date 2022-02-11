



function showBar(div_id) {
    console.log('Clicked!')
    console.log(div_id)
    const x = document.getElementById(div_id);
    console.log(x)
    if (x.style.display == "none")
        {
            x.style.display = "block";
            
        }
    else 
        {
        x.style.display = "none";
        }
}
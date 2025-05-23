function changeScore()
{
    var text = document.getElementById("skore").innerText;
    let skore = parseInt(text, 10);  // Convert to integer
    skore += 1;
    document.getElementById("skore").innerText = skore;
}

document.getElementById("klikatko").addEventListener("click",changeScore);
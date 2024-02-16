const paletteList = document.getElementById("palettes");
const colorArea = document.getElementById("color-area");
const colorPicker = document.getElementById("color-picker");
const maxPaletteSize = 5;

colorPicker.addEventListener("input", ()=>{
    colorArea.style.background = colorPicker.value;
})

function addListItem()
{
    var currentPaletteSize = paletteList.getElementsByTagName("li").length;

    if(currentPaletteSize >= maxPaletteSize)
    {
        return;
    }

    var newListItem = document.createElement("li");

    newListItem.innerHTML += 
        `
        <div class="color-area" id="color-area"></div>
        <input type="color" class="color-picker" id="color-picker">
        `;
            
    newListItem.setAttribute("id", "palette");
    paletteList.append(newListItem);
}

function removeListItem()
{
    var currentPaletteSize = paletteList.getElementsByTagName("li").length;

    if(currentPaletteSize <= 1)
    {
        return;
    }

    paletteList.removeChild(paletteList.childNodes[paletteList.childNodes.length - 1])
}
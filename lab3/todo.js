const button = document.querySelector(".btn");
const input = document.querySelector(".firstinput");
const listitems = document.querySelector(".listitems");

button.addEventListener("click", actions);
listitems.addEventListener("click",DeleteFunc);

function actions() {
  const block = document.createElement("div");
  block.classList.add("mydiv");
  const firstbutton = document.createElement("input");
  firstbutton.type = "checkbox";
  firstbutton.classList.add("check");
  block.appendChild(firstbutton);
  const firstlist = document.createElement("li");
  firstlist.innerHTML = input.value;
  firstlist.classList.add("list");
  if(input.value.trim()==""){
      return;
  }else{
    block.appendChild(firstlist);
  }
  LocalStorage(input.value);
  const secondbutton = document.createElement("button");
  secondbutton.innerHTML = '<i class="fas fa-trash-alt"></i>';
  secondbutton.classList.add("trash");
  block.appendChild(secondbutton);

  listitems.appendChild(block);
  input.value = "";
}
function DeleteFunc(e){//deleting and cheking function
    const del=e.target;
    if(del.classList[0]==='trash'){
        const mydiv=del.parentElement;
        mydiv.remove();
    }
    if(del.classList[0]==='check'){
        const mydiv=del.parentElement;
        mydiv.classList.toggle('line');
    }

}
function LocalStorage(mydiv){//saving to local storage
    let item;
    if(localStorage.getItem('item')==null){
        item=[];
    }
    else{
        item=JSON.parse(localStorage.getItem('item'));
    }
    item.push(mydiv);
    localStorage.setItem('item',JSON.stringify(item))//into string
}

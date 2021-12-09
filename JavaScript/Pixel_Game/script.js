var arrowLeft = 65, arrowUp = 87, arrowRight = 68, arrowDown = 83;   //a, w, d, s
//var arrowLeft = 37, arrowUp = 38, arrowRight = 39, arrowDown = 40; //arrow
var moveLeft = false, moveUp = false, moveRight = false, moveDown = false;
var cnv = document.querySelector("canvas");
var ctx = cnv.getContext("2d");
var size = 50;
var speed = 3;
var obj = {
  x: 10,
  y: cnv.height - size,
  speedX: 0,
  speedY: 0,
  w: size,
  h: size,
  edgeLeft: 10,
  edgeUp: cnv.height - size,
  edgeRight: 10 + size,
  edgeDown: cnv.height
};
var ready = false;

var obs = {
  x: 10,
  y: 20,
  w: 20,
  h: 20,
  speed: 50
}

update();

window.addEventListener("keydown",keydownHandler);
window.addEventListener("keyup",keyupHandler);

function keydownHandler(e){
  var key = e.keyCode;
  if(key == arrowLeft && key != arrowRight){
    moveLeft = true;
  }
  if(key == arrowUp && key != arrowDown){
    moveUp = true;
  }
  if(key == arrowRight && key != arrowLeft){
    moveRight = true;
  }
  if(key == arrowDown && key != arrowUp){
    moveDown = true;
  }
}

function keyupHandler(e){
  var key = e.keyCode;
  if(key == arrowLeft && key != arrowRight){
    moveLeft = false;
  }
  if(key == arrowUp && key != arrowDown){
    moveUp = false;
  }
  if(key == arrowRight && key != arrowLeft){
    moveRight = false;
  }
  if(key == arrowDown && key != arrowUp){
    moveDown = false;
  }
}

function move(){
  if(moveLeft){
    if(obj.x - speed < 0){
      obj.x = 0;
    }else{
      obj.x = obj.x - speed;
    }
    body();
  }
  if(moveUp){
    if (obj.y - speed < 0) {
      obj.y = 0;
    }else{
      obj.y = obj.y - speed;
    }
    body();
  }
  if(moveRight){
    if (obj.x + size + speed > cnv.width) {
      obj.x = cnv.width - size;
    }else{
      obj.x = obj.x + speed;
    }
    body(); 
  }
  if(moveDown){
    if (obj.y + size + speed > cnv.height) {
      obj.y = cnv.height - size;
    }else{
      obj.y = obj.y + speed;
    }
    body();
  }
  //console.log(obj.x,obj.y,"borda esquerda->",obj.edgeLeft,"borda direita->",obj.edgeRight,"borda de cima->",obj.edgeUp,"borda de baixo->",obj.edgeDown);
}


//Start
function Start(){
  if(ready == false){
    ready = true;
    GerarObstaculo();
  }
}

function render_obj(){
  ctx.clearRect(0,0,cnv.width,cnv.height);
  ctx.fillRect(obj.x,obj.y,obj.w,obj.h);
  ctx.fillStyle = "#000000";
}

function update(){
  requestAnimationFrame(update, cnv);
  limit();
  move();
  render_obj();
  obs_mov();
  if(obs.y > cnv.height){
    GerarObstaculo();
  }
}

function body(){
  obj.edgeLeft = obj.x;
  obj.edgeUp = obj.y;
  obj.edgeRight = obj.x + obj.w;
  obj.edgeDown = obj.y + obj.h;
}

function limit(){
  if (obj.edgeLeft <= 0){
    moveLeft = false;
    ctx.fillStyle = "#fff000";
  }
  if (obj.edgeUp <= 0){
    moveUp = false;
    ctx.fillStyle = "#fff000";
  }
  if (obj.edgeRight >= cnv.width){
    moveRight = false;
    ctx.fillStyle = "#fff000";
  }
  if (obj.edgeDown >= cnv.height){
    moveDown = false;
    ctx.fillStyle = "#fff000";
  }
}

//Físca
function physic(){
  this.gravity = 0.1;
  this.gravitySpeed = 0;
  this.newMotion = function(){
    this.gravitySpeed += this.gravity;
    obj.x += obj.speedX;
    obj.y += obj.speedY + this.gravitySpeed;
  }
}

//Obstáculos

function render_obs(){
  ctx.fillRect(obs.x,obs.y,obs.w,obs.h);
  ctx.fillStyle = "#000000";  
}

function GerarObstaculo() {
  //ready = false;
  obs.y = 20;
  let obstaculo_pos = (num) => Math.random() * num;
  obs.x = obstaculo_pos(cnv.width-obs.w);
  //setInterval(obs_mov, obs.speed);
}

function obs_mov(){
  if(obs.x != 10 && ready != false){
    render_obs();
    obs.y = obs.y + obs.speed/10;
    console.log(obs);
  }
}

function GameOver(){
  ready = false;
}
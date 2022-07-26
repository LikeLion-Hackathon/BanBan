//메뉴 선택시 표시
const menu = document.querySelector("#menu");
const url = window.location.href;
let getAr0 = url.indexOf("coBuying");
let getAr1 = url.indexOf("delivery");
let getAr2 = url.indexOf("community");
let menuPage = new Array();

menuPage = document.getElementById("menu").children;

if (getAr0 != -1) {
  menuPage[0].classList.add("on");
  menuPage[1].classList.remove("on");
  menuPage[2].classList.remove("on");
}
if (getAr1 != -1) {
  menuPage[1].classList.add("on");
  menuPage[0].classList.remove("on");
  menuPage[2].classList.remove("on");
}
if (getAr2 != -1) {
  menuPage[2].classList.add("on");
  menuPage[0].classList.remove("on");
  menuPage[1].classList.remove("on");
}
const goToPage = (url) => {
  window.location.href = `${url}`;
};

//프로필 모달창 토글
const modal = document.querySelector("#profile-modal");
const profileIcon = document.querySelector("#profile-icon");
profileIcon.addEventListener("click", () => {
  modal.classList.toggle("show");
});

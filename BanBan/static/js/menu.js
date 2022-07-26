//메뉴 선택시 표시
const selectMenu = (url) => {
  $("#main-container").load(url);
  let menuPage = new Array();

  var getAr0 = url.indexOf("coBuying");
  var getAr1 = url.indexOf("delivery");
  var getAr2 = url.indexOf("2");

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
};

//프로필 모달창 토글
const modal = document.querySelector("#profile-modal");
const profileIcon = document.querySelector("#profile-icon");
profileIcon.addEventListener("click", () => {
  modal.classList.toggle("show");
});

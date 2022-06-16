const dom = {
  userMenuToggle: document.querySelector('[data-menu-toggle]'),
  userMenu: document.querySelector('[data-user-menu]'),
  mobileMenuToggle: document.querySelector('[data-mobile-menu-toggle]'),
  mobileMenu: document.querySelector('[data-mobile-menu]'),
  wiiCups: document.getElementById("wii-cups"),
  toTopButton: document.getElementById("to-top"),
  loader: document.getElementById("loader"),
};

function gotoWii() {
  dom.wiiCups.scrollIntoView({ behavior: "smooth" });
}

function toTop() {
  dom.scoreboard.scrollIntoView({ behavior: "smooth" });
}

function toggleLoader(boolean) {
  if (boolean) {
    dom.loader.style.display = "flex";
  } else {
    dom.loader.style.display = "none";
  }
}

function toggleUserMenu() {
  dom.userMenu.classList.toggle('veil')
}

function toggleMobileMenu() {
  dom.mobileMenu.classList.toggle('offscreen-left')
}

function closeUserMenu() {
  if (dom.userMenu.classList.contains('veil') ){
    return
  } else {
    toggleUserMenu()
  }
}
function closeMobileMenu() {
  if(dom.mobileMenu.classList.contains('offscreen-left')) {
    return
  } else {
    toggleMobileMenu()
  }
}

const handleClick = function (event) {
  const targetElement = event.target;
  if (dom.userMenu && targetElement !== dom.userMenu && targetElement !== dom.userMenuToggle) {
    closeUserMenu()
  }
  if (dom.mobileMenu && targetElement  !== dom.mobileMenuToggle) {
    closeMobileMenu()
  }

  switch (targetElement) {
    case "goto_wii":
      gotoWii();
      break;
      case "to-top":
        toTop();
        break;
      case dom.userMenuToggle:
      toggleUserMenu()
      break;
      case dom.mobileMenuToggle:
      toggleMobileMenu()
      break;
    default:
      console.log("case default click");
  }
};

document.addEventListener("click", handleClick);
document.body.addEventListener("scroll", () => {
  setTimeout(() => {
    if (document.body.scrollTop === 0) {
      dom.toTopButton.style.display = "none";
    } else {
      dom.toTopButton.style.display = "block";
    }
  }, 400);
});

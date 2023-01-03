/* jshint esversion: 8, jquery: true, scripturl: true */
const profileMenu = document.getElementById("dropdown-profile");
const menu = document.querySelectorAll(".dropdown");
const loginSignup = document.getElementById("dropdown-enter");
const dropdown = document.querySelectorAll(".account__options");
const openProjectTypes = document.getElementById("add-new-project");
const addNewProject = document.getElementById("add__project");
const projectOptions = document.getElementById("project__options");
const addProjectIcon = document.getElementById("add-project-icon");

// On load
document.addEventListener("DOMContentLoaded", function () {
  // Close dropdown when the target is outside of the navbar container
  document.addEventListener("click", (e) => {
    if (document.getElementById("dropdown-profile")) {
      if (
        e.target !== dropdown &&
        e.target !== profileMenu &&
        profileMenu.classList.contains("open")
      ) {
        profileMenu.classList.remove("open");
      }
    } else {
      if (
        e.target !== dropdown &&
        e.target !== loginSignup &&
        loginSignup.classList.contains("open")
      ) {
        loginSignup.classList.remove("open");
      }
    }

    //Open New Projects' options
    if (e.target === openProjectTypes || e.target === addProjectIcon) {
      projectTypes(e);
    }
  });

  // Close open navbar menu
  menu.forEach((m) =>
    m.addEventListener("click", () => {
      m.classList.toggle("open");
    })
  );
});

/**
 * Open options for a new project
 */
const projectTypes = function (e) {
  e.preventDefault();
  projectOptions.classList.remove("project__options--hidden");
  addNewProject.classList.add("add__project--hidden");
};

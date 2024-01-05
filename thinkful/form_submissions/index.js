function validateForm(data) {
    return data.get("searchTerm").trim() !== "";
  }
  
  const form = document.querySelector("#searchForm");
  let error = document.querySelector("#searchError"); // Attempt to find an existing error element
  
  form.addEventListener("submit", function (event) {
    event.preventDefault();
  
    const formData = new FormData(form);
    const searchTerm = formData.get("searchTerm").trim();
    
    if (!validateForm(formData)) {
      if (!error) {
        // Create the error element only if it doesn't exist
        error = document.createElement("div");
        error.classList.add("error");
        error.id = "searchError";
        error.textContent = "Please enter a search term";
        form.appendChild(error);
      }
      error.style.display = "block"; // Show the error message
    } else {
      if (error) {
        error.style.display = "none"; // Hide the error message
      }
      filterArticlesBySearchTerm(searchTerm.toLowerCase());
    }
  });
  
  function filterArticlesBySearchTerm(searchTerm) {
    const articles = document.querySelectorAll("article");
  
    articles.forEach(article => {
      const title = article.querySelector("h2").textContent.toLowerCase();
      const isVisible = title.includes(searchTerm);
      article.classList.toggle("hidden", !isVisible);
    });
  }
  

/*
function validateForm(data) {
  return data.get("searchTerm").trim() !== "";
}


const form = document.querySelector("#searchForm");
form.addEventListener("submit", function (event) {
  event.preventDefault();

  let error = document.querySelector("#searchError");
  if (!error) {
    error = document.createElement("div");
    error.classList.add("error");
    error.id = "searchError";
    error.innerHTML = "Please enter a search term";
  } else {
    form.removeChild(error);
  }
  const formData = new FormData(form);
  if (!validateForm(formData)) {
    form.appendChild(error);
  } else {
    const searchTerm = formData.get("searchTerm").trim().toLowerCase();
    const titles = document.querySelectorAll("article > h2");
    for (let title of titles) {
      if (!title.innerHTML.toLowerCase().includes(searchTerm)) {
        title.parentNode.classList.add("hidden");
      } else {
        title.parentNode.classList.remove("hidden");
      }
    }
  }
});
*/
import "./styles.css";

/*
Add event listeners to the `.expand_button` buttons
*/
function expandArticleBody() {
    const expandButtons = document.querySelectorAll(".expand_button");
    for (let button of expandButtons){
        button.addEventListener("click", function (event) {
            const currentButton = event.target;
            const article = currentButton.closest(".article");
            const articleBody = article.querySelector(".article_body");

            if (currentButton.innerText === "V"){
                articleBody.style.display = "none";
                event.target.innerText = ">";
            } else {
                articleBody.style.display = "block";
                event.target.innerText = "V";
            }
        })
    }
}


function highlightArticle() {
  const highlightBtns = document.querySelectorAll(".highlightBtn");
  for (let btn of highlightBtns) {
    btn.addEventListener("click", function (event) {
      const currentBtn = event.target;
      const article = currentBtn.closest(".article");
      if (currentBtn.innerText === "+") {
        article.classList.add("highlight");
        currentBtn.innerText = "-";
      } else {
        article.classList.remove("highlight");
        currentBtn.innerText = "+";
      }
    });
  }
}

function main() {
  expandArticleBody();
  highlightArticle();
}

main();

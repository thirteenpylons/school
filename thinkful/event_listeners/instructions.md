JSDOM: Event listeners
Instructions

Your local newspaper is creating a website to move all of their content online. They wish to display a list of headlines and allow users to click to expand each news story to read the full story. They also wish to give the user the option to highlight any news story on the page. The HTML and CSS for the web page have already been written, and they want you to add the event handler code for the buttons.

Note: If you are working on an external editor, don't forget to run npm install and npm start.

Existing files

File	Description
test/solution.test.js	Contains test code. You are welcome to look at this file but do not modify it.
index.html	The HTML code for the website. Examine this code carefully to understand the DOM and target the necessary elements. You should not modify this file.
src/index.js	The JavaScript code for the web page. Write your solutions in this file.
src/styles.css	The CSS code for the web page. There is no need to edit this file.
Tasks

Write the following functions in the src/index.js file.

expandArticleBody()

In this function, first select all the buttons with the class .expand_button. On each button, add a click event listener that does the following:

Find the article in which the button that was clicked belongs.
If the text on the button that was clicked is a V, then set the display property of the article's body to none. Also set the text on the button to >.
If the text on the button that was clicked is not a V, then set the display property of the article's body to block. Also set the text on the button to V.
Hint: Iterate over the expand buttons:

  const expandBtns = document.querySelectorAll(".expand_button");
  for (let btn of expandBtns) {


  }
Hint: Add the event listeners for each btn

    btn.addEventListener("click", function (event) {




    });
Hint: The logic insidebtn.addEventListener should look something like this:

      const currentBtn = event.target;
      const article = currentBtn.closest(".article");
      const articleBody = article.querySelector(".article_body");
      if (currentBtn.innerText === "V") {
        articleBody.style.display = "none";
        event.target.innerText = ">";
      } else {
        articleBody.style.display = "block";
        event.target.innerText = "V";
      }
highlightArticle()

You don't need to do anything to this function but studying it will help you write the other function.
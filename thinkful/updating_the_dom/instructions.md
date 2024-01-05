JSDOM: Updating the DOM
Instructions

You are being asked to write a few functions to support a typical web page that updates the DOM. When the page loads, these functions will add structural and style constructs to the DOM.

Note: Initially, the web preview may appear broken because the code isn't complete. As you complete the code, the web preview will display correctly and your tests will pass.
Note: If you are working in an external editor, don't forget to run npm install and npm start.

Existing files

File	Description
test/solution.test.js	Contains test code. You are welcome to look at this file but do not modify it.
index.html	The HTML code for the website. Examine this code carefully to understand the DOM and target the necessary elements. You should not modify this file.
src/index.js	The JavaScript code for the web page. Write your solutions in this file.
src/styles.css	The CSS code for the web page. There is no need to edit this file.
Tasks

Write the following functions in the src/index.js file.

Note: These methods don't need to return any values.

addHeadings()

On the HTML, the article elements contain only text. Update all articles so they contain h2 headings. For example, the <article>Article 1</article> should become <article><h2>Article 1</h2></article>.

hint: Use querySelectorAll to select all the articles:
const articles = document.querySelectorAll("article");

hint: Use a for loop to add the headings:

  for (let article of articles) {
    const content = article.innerHTML;
    article.innerHTML = `<h2>${content}</h2>`;
  }
styleTutorialsAndArticles()

Some of the articles on the HTML are actually tutorials. You want these to be styled differently from the other articles. For all article elements on the HTML, add a class. If the article contain the word "Tutorial," add the class tutorial. Otherwise, add the class article. For example, this HTML:

<article>Article 3</article>
<article>Tutorial 1</article>
should become this:

<article class="article">Article 3</article>
<article class="tutorial">Tutorial 1</article>
hint: Use a for loop to iterate over the articles and use conditional statements to check if the innerHTML is either an Article or a Tutorial. Add the corresponding class to the article. A potential solution could look something like this:

  for (let article of articles) {
    if (article.innerHTML.includes("Article")) {
      article.classList.add("article");
    }
    if (article.innerHTML.includes("Tutorial")) {
      article.classList.add("tutorial");
    }
  }
separateAllTutorials()

This is already implemented for you. You only need to study it. This function removes all tutorials from the set of articles in the section with the class articles. Creates a new section element with the class tutorials and adds the tutorials to that new section. The new section is appended to the div with class container. If there are no tutorials, then don't create the new section.
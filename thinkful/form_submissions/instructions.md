JSDOM: Form submission
Instructions

You are working on a web application that includes a search form to help users filter the list of articles displayed on the page. For this challenge, you will be completing writing an event listener to perform the search on a form submission.

Note: Because the index.js file is incomplete, some of your tests will fail immediately. These failures will revert back to normal test failures once you have the basic app structure up and running.
Note: If you are working on an external editor, don't forget to run npm install and npm start.

Existing files

file path	description
index.html	Contains a form and a list of articles. The form contains a single input field. When the form is submitted the articles are filtered by the search term entered on the form. You should not edit the HTML file in any way.
index.css	A few basic styles. This challenge does not focus on style. You may ignore this file.
index.js	You need to write your JavaScript code in this file. This is the only file that you need to edit.
test/submit.test.js	The tests your code will run against. You do not need to edit this file.
Tasks

Form Submit Handler

Attach an event listener to the search form on the HTML. You may create additional supporting functions if you wish. On submission of the form, the following must occur:

Validate the form

Ensure that the form is not blank. Here, blank means an empty string or a string containing only spaces. If the form is blank, display an error message by creating and appending a new error element to the end of the form. The error element must take the following form:

<div class="error" id="searchError">Please enter a search term</div>
If the form is not blank, the error element should not be on the form.

Perform the search

Perform a case-insensitive search of the titles of the articles (that is, the innerHTML values of the h2 elements). If the search term matches any part of the title, the article should be displayed. If the search term doesn't match any part of the title, the article should be hidden.

To hide an article, add the class hidden to the article element. To make it visible again, remove the class hidden from the article element.

If a second search is conducted, articles hidden by any previous searches should be made visible again.
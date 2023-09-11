---
toc: true
comments: true
layout: post
title: JS Output w/jquery
description: 
courses: { compsci: {week: 2} }
type: hacks
---

## Article overview
- The article focuses on creating tables using various techniques, including Markdown, HTML, and JavaScript/jQuery.
It demonstrates the integration of third-party code for interactive tables and provides examples of HTML and JavaScript-based tables.
Readers are encouraged to experiment with table creation and explore styling HTML tables using resources like w3schools.
The article also discusses key differences between HTML and JavaScript and highlights the advantages of using JavaScript for interactive tables.

## Markdown Table
- A markdown table is presented, showcasing data with columns for Make, Model, Year, Color, and Price.

## HTML Table
- An HTML table is provided with a structured layout using <table>, <thead>, and <tbody> elements.
It includes data rows with information on various vehicle makes, models, years, colors, and prices.

## JavaScript/jQuery Table:
- The article introduces JavaScript and CSS code snippets integrated into the HTML document to create an interactive table.
Third-party code is used to enhance table interactivity.
JavaScript generates an interactive table using the data from the HTML <table id="demo"> within the <body>.

## Hacks requirement to answer
- Describe a benefit of a markdown table.
Markdown tables are a simple way to format and organize data in a plain text format. They are easy to write and read, making them useful for quick documentation and simple data representation.

- Describe the difference between HTML and JavaScript.
HTML structures web content, while JavaScript adds interactivity and dynamic features, enhancing web page functionality.

- Describe a benefit of a table that uses JavaScript.
Tables that use JavaScript can provide interactive features such as sorting, filtering, and dynamic updates without requiring a full page reload. This enhances the user experience by allowing users to interact with and explore data more effectively.

## make my own table by styling the HTML Table (with W3Schools as a rerousce). 

<!DOCTYPE html>
<html>
<head>
<style>
table {
  font-family: Arial, Helvetica, sans-serif;
  border-collapse: collapse;
  width: 50%;
  margin: auto;
}

table, th, td {
  border: 1px solid black;
}

th, td {
  padding: 8px;
  text-align: left;
}

th {
  background-color: #000;
}
</style>
</head>
<body>

<table>
    <tr>
        <th>Product</th>
        <th>Price</th>
    </tr>
    <tr>
        <td>Laptop</td>
        <td>$800</td>
    </tr>
    <tr>
        <td>Smartphone</td>
        <td>$400</td>
    </tr>
    <tr>
        <td>Headphones</td>
        <td>$50</td>
    </tr>
</table>

</body>
</html>

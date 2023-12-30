// Wait for the HTML document to be fully loaded
document.addEventListener("DOMContentLoaded", function () {
    // Get the table of contents (TOC) list element
    let tocList = document.getElementById('toc-list');

    // Define the selector for the headings to be included in the TOC
    const headingSelector = "h1, h2, h3, h4, h5";

    // Get all the heading elements within the .toc-content-area element
    let headings = document.querySelectorAll(".toc-content-area " + headingSelector);

    // Function to update the highlighting of the active TOC item
    function updateTocHighlight() {
        // Variable to keep track if an active TOC item is found
        let foundActive = false;

        // Iterate over each heading element
        headings.forEach(function (node) {
            // Check if the heading element should be excluded from the TOC
            if (node.closest('.toc-exclude')) {
                return;
            }

            // Get the ID of the heading element
            let id = node.id;

            // Get the bounding rectangle of the heading element
            let bounding = node.getBoundingClientRect();

            // Define the classes for the active TOC item
            let activeClass = ['text-rose-300', 'font-bold'];

            // Check if the heading element is within the visible portion of the page
            if (bounding.top <= window.innerHeight * 0.2 && bounding.bottom >= 0) {
                // Iterate over each TOC link
                document.querySelectorAll('#toc-list a').forEach(function (a) {
                    // Remove the active classes from the TOC link
                    a.classList.remove(...activeClass);

                    // Check if the TOC link corresponds to the current heading element
                    if (a.getAttribute('href') === '#' + id) {
                        // Add the active classes to the TOC link
                        a.classList.add(...activeClass);

                        // Set the foundActive flag to true
                        foundActive = true;
                    }
                });
            }
        });
    }

    // Iterate over each heading element
    headings.forEach(function (node) {
        // Check if the heading element should be excluded from the TOC
        if (node.closest('.toc-exclude')) {
            return;
        }

        // Get the ID of the heading element or generate one if it doesn't exist
        let id = node.id || node.innerText.trim().toLowerCase().replace(/\s+/g, '-');
        node.id = id;

        // Calculate the level of the heading element
        let level = parseInt(node.nodeName.substring(1)) - 1;

        // Calculate the padding class for the TOC item
        let paddingLeftClass = `pl-${level * 2 + 4}`;

        // Create a new list item element for the TOC
        let listItem = document.createElement('li');

        // Set the HTML content of the list item with a link to the heading element
        listItem.innerHTML = `<a href="#${id}" class="block text-gray-500 hover:text-gray-700 ${paddingLeftClass}">${node.innerText}</a>`;

        // Add an event listener to the TOC link for smooth scrolling
        listItem.querySelector('a').addEventListener('click', function (e) {
            e.preventDefault();
            document.getElementById(id).scrollIntoView({ behavior: 'smooth' });
            setTimeout(updateTocHighlight, 0);
        });

        // Append the list item to the TOC list
        tocList.appendChild(listItem);
    });

    // Add a scroll event listener to update the TOC highlighting
    window.addEventListener('scroll', updateTocHighlight);
});
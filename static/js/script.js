document.addEventListener("DOMContentLoaded", function () {
    let tocList = document.getElementById('toc-list');
    const headingSelector = "h1, h2, h3, h4, h5";
    let headings = document.querySelectorAll(".toc-content-area " + headingSelector);

    function updateTocHighlight() {
        let foundActive = false;
        headings.forEach(function (node) {
            if (node.closest('.toc-exclude')) {
                return;
            }

            let id = node.id;
            let bounding = node.getBoundingClientRect();
            let activeClass = ['text-rose-300', 'font-bold'];

            if (bounding.top <= window.innerHeight * 0.2 && bounding.bottom >= 0) {
                document.querySelectorAll('#toc-list a').forEach(function (a) {
                    a.classList.remove(...activeClass);
                    if (a.getAttribute('href') === '#' + id) {
                        a.classList.add(...activeClass);
                        foundActive = true;
                    }
                });
            }
        });
    }

    headings.forEach(function (node) {
        if (node.closest('.toc-exclude')) {
            return;
        }

        let id = node.id || node.innerText.trim().toLowerCase().replace(/\s+/g, '-');
        node.id = id;

        let level = parseInt(node.nodeName.substring(1)) - 1;
        let paddingLeftClass = `pl-${level * 2 + 4}`; // 使用padding-left替代margin-left

        let listItem = document.createElement('li');
        listItem.innerHTML = `<a href="#${id}" class="block text-gray-500 hover:text-gray-700 ${paddingLeftClass}">${node.innerText}</a>`;

        listItem.querySelector('a').addEventListener('click', function (e) {
            e.preventDefault();
            document.getElementById(id).scrollIntoView({ behavior: 'smooth' });
            setTimeout(updateTocHighlight, 0);
        });

        tocList.appendChild(listItem);
    });

    window.addEventListener('scroll', updateTocHighlight);
});

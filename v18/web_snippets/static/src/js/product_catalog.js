/** @odoo-module **/

import publicWidget from '@web/legacy/js/public/public_widget';
import { rpc } from "@web/core/network/rpc";

publicWidget.registry.Products = publicWidget.Widget.extend({
    selector : ".product-catalog",

    async start(){
        const productData = await rpc("/product/catalog")
        console.log("Inside catalog js.............")
        const productList = this.el.querySelector("#productCarousel");
        const prevBtn = this.el.querySelector("#prevBtn");
        const nextBtn = this.el.querySelector("#nextBtn");

        productList.innerHTML = ""; // Clear existing content

        // Build product items
        productData.forEach(product => {
            const li = document.createElement("li");
            li.className = "product-item";

            const img = document.createElement("img");
            img.src = `data:image/png;base64,${product.image}`;
            img.alt = product.name;
            img.style.width = "368px";  // maintain card width

            const divContent = document.createElement("div");
            divContent.className = "p-3";

            // Product Title
            const pTitle = document.createElement("p");
            pTitle.className = "product-title";
            pTitle.innerHTML = product.name;
            divContent.appendChild(pTitle);

            // Price
            const divPrice = document.createElement("div");
            divPrice.className = "mb-1";

            const sMRP = document.createElement("s");
            sMRP.className = "product-old-price";
            sMRP.innerHTML = `₹${product.mrp}`;
            divPrice.appendChild(sMRP);

            const strongPrice = document.createElement("strong");
            strongPrice.className = "product-price";
            strongPrice.innerHTML = `₹${product.selling_price}`;
            divPrice.appendChild(strongPrice);

            divContent.appendChild(divPrice);

            // Tag / Rating
            const spanTag = document.createElement("span");
            if (product.tag) {
                spanTag.className = "delivery-badge";
                spanTag.style.backgroundColor = product.tag_color;
                spanTag.style.color = product.text_color;
                spanTag.innerHTML = product.tag;
            } else {
                spanTag.innerHTML = `<img src='https://www.fnp.com/icons/vector-rating.svg'><small> ${product.rating}</small>`;
            }
            divContent.appendChild(spanTag);

            // Delivery
            const pDelivery = document.createElement("p");
            pDelivery.className = "delivery-text";
            pDelivery.innerHTML = `Earliest Delivery: ${product.delivery}`;
            divContent.appendChild(pDelivery);

            li.appendChild(img);
            li.appendChild(divContent);

            productList.appendChild(li);
        });

        // Calculate items after rendering
        const productItems = productList.querySelectorAll("li");
        const totalItems = productItems.length;
        const itemWidth = productItems[0].getBoundingClientRect().width + 16; // card width + gap
        const visibleCount = 4;
        let currentIndex = 0;

        function updateCarousel() {
            productList.style.transform = `translateX(-${currentIndex * itemWidth}px)`;
            prevBtn.style.display = currentIndex === 0 ? "none" : "block";
            nextBtn.style.display = currentIndex >= totalItems - visibleCount ? "none" : "block";
        }

        nextBtn.addEventListener("click", () => {
            if (currentIndex < totalItems - visibleCount) {
                currentIndex++;
                updateCarousel();
            }
        });

        prevBtn.addEventListener("click", () => {
            if (currentIndex > 0) {
                currentIndex--;
                updateCarousel();
            }
        });

        updateCarousel(); // Initial update
    },
});

export default publicWidget.registry.Products;
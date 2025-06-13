document.addEventListener("DOMContentLoaded", function () {
  const csrfToken = window.CSRF_TOKEN;
  const openModalBtn = document.getElementById("openModalBtn");
  const closeModalBtn = document.getElementById("closeModalBtn");
  const modal = document.getElementById("addressModal");

  openModalBtn.addEventListener("click", () => modal.classList.remove("hidden"));
  closeModalBtn.addEventListener("click", () => modal.classList.add("hidden"));

  function updateCartCount() {
    fetch("/cart/count/")
      .then((response) => response.json())
      .then((data) => {
        const cartCountElement = document.querySelector("#cart-count");
        if (cartCountElement) {
          cartCountElement.textContent = data.cart_count;
        }
      })
      .catch((error) => console.error("Erro ao atualizar o contador do carrinho:", error));
  }

  function updateCartTotals() {
    let subtotal = 0;
    document.querySelectorAll(".cart-item").forEach((item) => {
      const price = parseFloat(item.querySelector(".price").textContent.replace("R$", "").trim());
      const quantity = parseInt(item.querySelector(".qty-input").value);
      subtotal += price * quantity;
    });

    document.getElementById("subtotal").textContent = `R$ ${subtotal.toFixed(2)}`;
    const shipping = 4.99;
    document.getElementById("shipping").textContent = `R$ ${shipping.toFixed(2)}`;
    document.getElementById("total").textContent = `R$ ${(subtotal + shipping).toFixed(2)}`;

    document.getElementById("total_input").value = subtotal + shipping;
  }

  document.querySelectorAll(".cart-item").forEach((item) => {
    const productId = item.dataset.productId;
    const decreaseBtn = item.querySelector(".decrease-qty");
    const increaseBtn = item.querySelector(".increase-qty");
    const qtyInput = item.querySelector(".qty-input");
    const removeBtn = item.querySelector(".remove-item");

    increaseBtn.addEventListener("click", function (event) {
      event.preventDefault();
      fetch(`/add/${productId}/`, {
        method: "POST",
        headers: {
          "X-CSRFToken": csrfToken,
          "Content-Type": "application/json",
        },
      })
        .then((response) => response.json())
        .then((data) => {
          qtyInput.value = data.quantity;
          updateCartCount();
          updateCartTotals();
        });
    });

    decreaseBtn.addEventListener("click", function (event) {
      event.preventDefault();
      fetch(`/remove/${productId}/`, {
        method: "POST",
        headers: {
          "X-CSRFToken": csrfToken,
          "Content-Type": "application/json",
        },
      })
        .then((response) => response.json())
        .then((data) => {
          if (data.removed) {
            item.remove();
          } else {
            qtyInput.value = data.quantity;
          }
          updateCartCount();
          updateCartTotals();
        });
    });

    removeBtn.addEventListener("click", function (event) {
      event.preventDefault();
      fetch(`/delete/${productId}/`, {
        method: "POST",
        headers: {
          "X-CSRFToken": csrfToken,
          "Content-Type": "application/json",
        },
      })
        .then((response) => response.json())
        .then((data) => {
          if (data.removed) {
            item.remove();
            updateCartTotals();
            updateCartCount();
          }
        });
    });
  });

  updateCartTotals();
});

from pyscript import document, display


def make_receipt(e):
    # dessert items
    cake = document.getElementById("cake")
    donut = document.getElementById("donut")
    cupcake = document.getElementById("cupcake")
    icecream = document.getElementById("icecream")
    brownie = document.getElementById("brownie")

    # calculate subtotal
    subtotal = (
        float(cake.value) * cake.checked +
        float(donut.value) * donut.checked +
        float(cupcake.value) * cupcake.checked +
        float(icecream.value) * icecream.checked +
        float(brownie.value) * brownie.checked
    )

    # calculate VAT
    vat = subtotal * 0.12

    # calculate total
    total = subtotal + vat

    # display receipt
    display(
        f"Subtotal: ₱ {subtotal:.2f}",
        target="receipt_subtotal"
    )

    display(
        f"VAT (12%): ₱ {vat:.2f}",
        target="receipt_vat"
    )

    display(
        f"Total Amount: ₱ {total:.2f}",
        target="receipt_total"
    )
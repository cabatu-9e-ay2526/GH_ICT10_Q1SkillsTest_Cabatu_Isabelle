from pyscript import document, display


def make_receipt(e):
    # Get customer information
    customer_name = document.getElementById("customer_name").value
    customer_contact = document.getElementById("customer_contact").value

    # Get dessert choices
    cake = document.getElementById("cake")
    donut = document.getElementById("donut")
    cupcake = document.getElementById("cupcake")
    icecream = document.getElementById("icecream")
    brownie = document.getElementById("brownie")

    # Store all desserts in a list
    desserts = [cake, donut, cupcake, icecream, brownie]

    # Set the starting subtotal
    subtotal = 0

    # Store the selected desserts
    selected_desserts = []

    # Loop through the desserts
    for dessert in desserts:
        if dessert.checked:
            subtotal += float(dessert.value)
            selected_desserts.append(dessert.id)

    # Check if at least one dessert was selected
    if subtotal == 0:
        display(
            "Please select at least one dessert.",
            target="receipt_items"
        )
        return

    # Calculate 12% VAT
    vat = subtotal * 0.12

    # Calculate total amount
    total = subtotal + vat

    # Display customer information
    display(
        f"Customer: {customer_name}",
        target="receipt_customer"
    )

    display(
        f"Contact Number: {customer_contact}",
        target="receipt_customer"
    )

    # Display selected desserts
    display(
        f"Selected Desserts: {', '.join(selected_desserts)}",
        target="receipt_items"
    )

    # Display subtotal
    display(
        f"Subtotal: ₱{subtotal:.2f}",
        target="receipt_subtotal"
    )

    # Display VAT
    display(
        f"VAT (12%): ₱{vat:.2f}",
        target="receipt_vat"
    )

    # Display total amount
    display(
        f"Total Amount: ₱{total:.2f}",
        target="receipt_total"
    )

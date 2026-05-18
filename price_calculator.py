# ---- Funciones provistas (NO modificar) ----

def apply_discount(price, discount_pct):
    return price * (1 - discount_pct / 100)

def apply_tax(price, tax_pct):
    return price * (1 + tax_pct / 100)

def final_price(price, quantity, discount_pct, tax_pct):
    subtotal_uno = price * quantity
    subtotal_dos  = apply_discount(subtotal_uno,discount_pct)
    subtotal_tres = apply_tax(subtotal_dos, tax_pct)
    return round(subtotal_tres,2)

def best_deal(price_a, qty_a, disc_a, price_b, qty_b, disc_b, tax_pct):
    producto_a = final_price(price_a, qty_a, disc_a, tax_pct)
    producto_b = final_price(price_b, qty_b, disc_b, tax_pct)
    if producto_a > producto_b:
        return "B"
    return "A"

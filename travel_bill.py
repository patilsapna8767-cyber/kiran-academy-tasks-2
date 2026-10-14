def calculateFlightGST(a, b):
    total = a + b
    gst = total * 0.18
    return total + gst

def calculateHotelGST(c, d):
    total = c + d
    gst = total * 0.12
    return total + gst

def calculateFoodGST(e):
    gst = e * 0.05
    return e + gst

def totalBill(a, b, c, d, e):
    flight = calculateFlightGST(a, b)
    hotel = calculateHotelGST(c, d)
    food = calculateFoodGST(e)
    return flight + hotel + food

def calculateDiscountedBill(a, b, c, d, e):
    total = totalBill(a, b, c, d, e)
    discount = total * 0.15
    return total - discount

def main():
    a = 100
    b = 100
    c = 100
    d = 100
    e = 100
    total_after_gst = totalBill(a, b, c, d, e)
    discount = total_after_gst * 0.15
    final = calculateDiscountedBill(a, b, c, d, e)
    print(f"Total after GST = {total_after_gst:.2f} | Discount = {discount:.2f} | Final payable amount = {final:.2f}")
    return final

if __name__ == "__main__":
    main()

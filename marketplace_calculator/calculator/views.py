from django.shortcuts import render

def calculate_cost(request):
    if request.method == "POST":
        cost_price = float(request.POST["cost_price"])
        sale_price = float(request.POST["sale_price"])
        marketplace_fee_percent = float(request.POST["marketplace_fee_percent"])
        marketplace_fixed_fee = float(request.POST["marketplace_fixed_fee"])
        tax_percent = float(request.POST["tax_percent"])

        revenue = sale_price - (sale_price * (marketplace_fee_percent / 100)) - marketplace_fixed_fee - (sale_price * (tax_percent / 100))
        profit = revenue - cost_price
        profit_margin = (profit / cost_price) * 100 if cost_price > 0 else 0

        return render(request, "calculator/result.html", {
            "revenue": revenue,
            "profit": profit,
            "profit_margin": profit_margin
        })

    return render(request, "calculator/calculate.html")
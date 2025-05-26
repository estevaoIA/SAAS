from django.db import models

class Sale(models.Model):
    product_name = models.CharField(max_length=100)
    cost_price = models.DecimalField(max_digits=10, decimal_places=2)  # Preço de custo
    sale_price = models.DecimalField(max_digits=10, decimal_places=2)  # Preço de venda
    marketplace_fee_percent = models.DecimalField(max_digits=5, decimal_places=2)  # Taxa percentual
    marketplace_fixed_fee = models.DecimalField(max_digits=10, decimal_places=2)  # Taxa fixa
    tax_percent = models.DecimalField(max_digits=5, decimal_places=2)  # Imposto %

    def revenue(self):
        return self.sale_price - (self.sale_price * self.marketplace_fee_percent / 100) - self.marketplace_fixed_fee - (self.sale_price * self.tax_percent / 100)

    def profit(self):
        return self.revenue() - self.marketplace_fixed_fee

    def profit_margin(self):
        return (self.profit() / self.marketplace_fixed_fee) * 100 if self.marketplace_fixed_fee > 0 else 0
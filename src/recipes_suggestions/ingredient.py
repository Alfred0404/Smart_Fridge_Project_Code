class Ingredient:
    def __init__(self, name, amount=None, unit=None):
        self.name = name
        self.amount = amount
        self.unit = unit

    def __str__(self):
        if self.amount and self.unit:
            return f"{self.amount} {self.unit} of {self.name}"
        elif self.amount:
            return f"{self.amount} of {self.name}"
        else:
            return self.name

    def to_dict(self):
        return {
            "ingredient": self.name,
            "amount": (
                f"{self.amount} {self.unit}" if self.amount and self.unit else None
            ),
        }

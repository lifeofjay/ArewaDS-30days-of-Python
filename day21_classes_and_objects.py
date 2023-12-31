class StatisticalAnalysis:
    def __init__(self, data):
        self.dataset = data

    def get_count(self):
        return len(self.dataset)

    def get_sum(self):
        return sum(self.dataset)

    def get_min(self):
        return min(self.dataset)

    def get_max(self):
        return max(self.dataset)

    def get_range(self):
        return max(self.dataset) - min(self.dataset)

    def get_mean(self):
        return sum(self.dataset) / len(self.dataset)

    def get_median(self):
        sorted_data = sorted(self.dataset)
        n = len(self.dataset)
        return (sorted_data[n // 2] + sorted_data[n // 2 - 1]) / 2 if n % 2 == 0 else sorted_data[n // 2]

    def get_mode(self):
        frequency_dict = {item: self.dataset.count(item) for item in set(self.dataset)}
        mode_value = max(frequency_dict, key=frequency_dict.get)
        return {'mode': mode_value, 'count': frequency_dict[mode_value]}

    def get_standard_deviation(self):
        mean_value = self.get_mean()
        variance = sum((x - mean_value) ** 2 for x in self.dataset) / len(self.dataset)
        return variance ** 0.5

    def get_variance(self):
        mean_value = self.get_mean()
        return sum((x - mean_value) ** 2 for x in self.dataset) / len(self.dataset)

    def get_frequency_distribution(self):
        frequency_dict = {item: self.dataset.count(item) for item in set(self.dataset)}
        return sorted([(count, value) for value, count in frequency_dict.items()], reverse=True)


# Example data
ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]

# Creating an instance of StatisticalAnalysis
data_analysis = StatisticalAnalysis(ages)

# Output the results
print('Count:', data_analysis.get_count())
print('Sum: ', data_analysis.get_sum())
print('Min: ', data_analysis.get_min())
print('Max: ', data_analysis.get_max())
print('Range: ', data_analysis.get_range())
print('Mean: ', data_analysis.get_mean())
print('Median: ', data_analysis.get_median())
print('Mode: ', data_analysis.get_mode())
print('Standard Deviation: ', data_analysis.get_standard_deviation())
print('Variance: ', data_analysis.get_variance())
print('Frequency Distribution: ', data_analysis.get_frequency_distribution())


#Exercise two
class PersonalAccount:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.income_records = []
        self.expense_records = []

    def record_income(self, amount, desc):
        self.income_records.append({'amount': amount, 'description': desc})

    def record_expense(self, amount, desc):
        self.expense_records.append({'amount': amount, 'description': desc})

    def total_income(self):
        return sum(record['amount'] for record in self.income_records)

    def total_expense(self):
        return sum(record['amount'] for record in self.expense_records)

    def balance(self):
        return self.total_income() - self.total_expense()

    def account_info(self):
        info = {
            'first': self.first,
            'last': self.last,
            'total_income': self.total_income(),
            'total_expense': self.total_expense(),
            'balance': self.balance(),
            'income_records': self.income_records,
            'expense_records': self.expense_records
        }
        return info


# Example usage:
account_holder = PersonalAccount("Jamal", "Deen")
account_holder.record_income(1000, "Bills payment")
account_holder.record_income(500, "Part bills ")
account_holder.record_expense(300, "Food shopping")
account_holder.record_expense(150, "Utility bills")

print("Account Information:")
print(account_holder.account_info())

# Import all the files
import analysis.py
import coupon_analysis.py
import peak.py
import rewards_percents.py
import Total_sales.py

print('Welcome to Miami Enterprises. Here is an in-depth breakdown of the data for the past fiscal year.')
print()
print(f'Total Revenue: {Total_sales.total_sales}')
print(f'Average Revenue per Transaction: {Total_sales.average_transaction}')
peak.peak_hours()
print(f'Percentage of Purchases Using Rewards Numbers: {rewards_percents.percentage_with_rewards_number}')
print(f'Percentage of Purchases With Memberships: {rewards_percents.percentage_with_both}')
print(f'{c}')
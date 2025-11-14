# Import all the files
import analysis
import coupon_analysis
import peak
import rewards_percents
import total_sales

print('Welcome to Miami Enterprises. Here is an in-depth breakdown of the data for the past fiscal year.')
print()
print(f'Total Revenue: {total_sales.total_sales}')
print(f'Average Revenue per Transaction: {total_sales.average_transaction}')
peak.peak_hours()
print(f'Percentage of Purchases Using Rewards Numbers: {rewards_percents.percentage_with_rewards_number}')
print(f'Percentage of Purchases With Memberships: {rewards_percents.percentage_with_both}')
print(f'{coupon_analysis.count} transactions used coupons, resulting in {coupon_analysis.lost_revenue} of savings')
print(f'Coupon sales also acount for ${coupon_analysis.revenue_from_coupons} of revenue')
print('Most of our sales came from 5 large companies:')
analysis.analysis()

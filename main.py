# Import all the files
import analysis
import coupon_analysis
import peak
import rewards_percents
import total_sales
import revenue_by_state

print('Welcome to Miami Enterprises. Here is an in-depth breakdown of the data for the past fiscal year.')
print()
print(f'\nTotal Revenue: ${total_sales.total_sales:.2f}')
print(f'\nAverage Revenue per Transaction: ${total_sales.average_transaction:.2f}')
peak.peak_hours()
peak.revenue_per_month()
print(f'\nPercentage of Purchases Using Rewards Numbers: {rewards_percents.percentage_with_rewards_number:.1%}')
print(f'\nPercentage of Purchases With Memberships: {rewards_percents.percentage_with_both:.1%}')
print(f'\nThe maximum revenue acheived by a single state is: ${revenue_by_state.max_state_revenue}')
print(f'\nThe maximum number of transactions acheived by a single state is: {revenue_by_state.max_state_transactions}')
print(f'\n{coupon_analysis.count} transactions used coupons, resulting in ${coupon_analysis.lost_revenue:.2f} of savings')
print(f'\nCoupon sales also acount for ${coupon_analysis.revenue_from_coupons:.2f} of revenue')
print('\nMost of our sales came from 5 large companies: Google, Apple, Microsoft, Amazon, and Toyota')
analysis.analysis(True)

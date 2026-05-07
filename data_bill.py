# constant values are set here:
TIER_1_DATA_LIMIT_GB = 10
TIER_2_DATA_LIMIT_GB = 20
PREMIUM_USER_OVERAGE_RATE_TIER_2 = 1
REGULAR_USER_OVERAGE_RATE_TIER_2 = 2
PREMIUM_USER_OVERAGE_RATE_TIER_3 = 2
REGULAR_USER_OVERAGE_RATE_TIER_3 = 3


# Your code goes here:
#Ask the user fot the following inputs
data_used = int(input("Enter the amount of data used: "))
monthy_cost = float(input("Enter the monthly cost: "))
premium_user = input("Do you have a premium plan? (yes/no): ")

if data_used <= TIER_1_DATA_LIMIT_GB:
    total_cost = monthy_cost
    print 
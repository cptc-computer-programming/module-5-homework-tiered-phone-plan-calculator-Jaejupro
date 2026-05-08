# constant values are set here:
TIER_1_DATA_LIMIT_GB = 10
TIER_2_DATA_LIMIT_GB = 20
PREMIUM_USER_OVERAGE_RATE_TIER_2 = 1
REGULAR_USER_OVERAGE_RATE_TIER_2 = 2
PREMIUM_USER_OVERAGE_RATE_TIER_3 = 2
REGULAR_USER_OVERAGE_RATE_TIER_3 = 3


# Your code goes here:
#Ask the user fot the following inputs
data_used = float(input("Enter the amount of data used: "))
monthy_cost = float(input("Enter the monthly cost: "))
premium_user = input("Do you have a premium plan? (yes/no): ")


has_premium = (premium_user == "yes")

if data_used <= TIER_1_DATA_LIMIT_GB:
   
    overage_gb = 0
    overage_rate = 0
    overage_cost = 0
    print("You are within your data limit.")

elif data_used > TIER_1_DATA_LIMIT_GB and data_used <= TIER_2_DATA_LIMIT_GB:
    overage_gb = data_used - TIER_1_DATA_LIMIT_GB
    
    if has_premium:
        overage_rate = PREMIUM_USER_OVERAGE_RATE_TIER_2
    else:
        overage_rate = REGULAR_USER_OVERAGE_RATE_TIER_2

    overage_cost = overage_gb * overage_rate
    print(f"You are {overage_gb} GB over your limit.")

else:
    overage_gb = data_used - TIER_1_DATA_LIMIT_GB
    
    if has_premium:
        overage_rate = PREMIUM_USER_OVERAGE_RATE_TIER_3
    else:
        overage_rate = REGULAR_USER_OVERAGE_RATE_TIER_3

    overage_cost = overage_gb * overage_rate
    print(f"You are {overage_gb} GB over your limit.")

# Total bill
total_bill = monthy_cost + overage_cost

# Output
print(f"GB over limit: {overage_gb}")
print(f"Overage rate: ${overage_rate} per GB")
print(f"Overage cost: ${overage_cost:.2f}")
print(f"Total bill: ${total_bill:.2f}")


           
# T3 - Fraud Detection

total_transactions = 10000
fraudulent_transactions = 100

true_positive = 90
false_positive = 500

# 1. Probability of fraud
p_fraud = fraudulent_transactions / total_transactions

# Actual genuine transactions
genuine_transactions = total_transactions - fraudulent_transactions

# 2. False Positive Rate
false_positive_rate = false_positive / genuine_transactions

# 3. Precision
precision = true_positive / (true_positive + false_positive)

print("Probability of Fraud:", p_fraud)
print("False Positive Rate:", false_positive_rate)
print("Precision:", precision)

print("\nPercentage Results:")
print("Probability of Fraud:", p_fraud * 100, "%")
print("False Positive Rate:", false_positive_rate * 100, "%")
print("Precision:", precision * 100, "%")

#!/bin/bash

# Prompt the user to enter principal amount
read -p "Enter the principal amount: " principal

# Prompt the user to enter rate of interest
read -p "Enter the rate of interest (in percentage): " rate

# Prompt the user to enter time period
read -p "Enter the time period (in years): " time

# Calculate simple interest
interest=$(echo "scale=2; $principal * $rate * $time / 100" | bc)

# Display the result
echo "Simple interest for principal amount $principal at an interest rate of $rate% for $time years is: $interest"

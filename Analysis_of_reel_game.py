import numpy as np
import matplotlib.pyplot as plt
import pandas as pd # For better table formatting

# --- Game Parameters ---
# Reel strip symbol counts
reel1_counts = {'7': 8, 'CHERRY': 10, 'BAR': 9, 'BLANK': 3}
reel2_counts = {'7': 6, 'CHERRY': 12, 'BAR': 10, 'BLANK': 4}
reel3_counts = {'7': 5, 'CHERRY': 15, 'BAR': 12, 'BLANK': 3}

# Define possible symbols for random selection (based on counts)
reel1_symbols = [symbol for symbol, count in reel1_counts.items() for _ in range(count)]
reel2_symbols = [symbol for symbol, count in reel2_counts.items() for _ in range(count)]
reel3_symbols = [symbol for symbol, count in reel3_counts.items() for _ in range(count)]

# Payout table
payouts = {
    ('7', '7', '7'): 100,
    ('BAR', 'BAR', 'BAR'): 5,
    ('CHERRY', 'CHERRY', 'CHERRY'): 1,
    # All other combinations implicitly pay 0
}


num_simulations = 1000000 # Increased simulations for better statistical stability

# --- Simulation ---
payoff_results = []
for _ in range(num_simulations):
    result_r1 = np.random.choice(reel1_symbols)
    result_r2 = np.random.choice(reel2_symbols)
    result_r3 = np.random.choice(reel3_symbols)
    current_combination = (result_r1, result_r2, result_r3)
    payoff = payouts.get(current_combination, 0)
    payoff_results.append(payoff)

# --- Analysis & Data Preparation ---
total_wagered = num_simulations * 1 # 1 coin bet per spin
total_returned = sum(payoff_results)
simulated_rtp = (total_returned / total_wagered) * 100
print(f"Simulated RTP: {simulated_rtp:.2f}%")
print(f"Number of simulated spins: {num_simulations}\n")

# Count frequencies of each payoff amount
payoff_counts = pd.Series(payoff_results).value_counts().sort_index()

# Create a DataFrame for summary table
summary_df = pd.DataFrame(index=payoff_counts.index)
summary_df['Frequency'] = payoff_counts
summary_df['Probability (%)'] = (payoff_counts / num_simulations * 100).round(4)
summary_df['Total Payout (Coins)'] = summary_df.index * summary_df['Frequency']
summary_df['Contribution to RTP (%)'] = (summary_df['Total Payout (Coins)'] / total_wagered * 100).round(4)

# Add a row for total RTP
total_row = pd.DataFrame({
    'Frequency': summary_df['Frequency'].sum(),
    'Probability (%)': summary_df['Probability (%)'].sum(),
    'Total Payout (Coins)': summary_df['Total Payout (Coins)'].sum(),
    'Contribution to RTP (%)': simulated_rtp
}, index=['TOTAL'])
summary_df = pd.concat([summary_df, total_row])

print("--- Payoff Summary Table ---")
print(summary_df.to_string(float_format="%.2f")) # Format to 2 decimal places

# --- Visualizations ---

# 1. Bar Chart: Winning Payoffs Only
winning_payoffs_counts = payoff_counts[payoff_counts.index > 0]
if not winning_payoffs_counts.empty:
    plt.figure(figsize=(8, 6))
    plt.bar(winning_payoffs_counts.index.astype(str), winning_payoffs_counts.values,
            color='skyblue', edgecolor='black', width=0.6)
    plt.title('Frequency of Winning Payoffs')
    plt.xlabel('Payoff Amount (Coins)')
    plt.ylabel('Frequency (Number of Occurrences)')
    plt.xticks(winning_payoffs_counts.index.astype(str))
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()


plt.figure(figsize=(10, 7))
all_payoffs_labels = payoff_counts.index.astype(str)
plt.bar(all_payoffs_labels, payoff_counts.values,
        color=['lightcoral' if p == '0' else 'lightgreen' for p in all_payoffs_labels],
        edgecolor='black', width=0.7)
plt.title(f'Frequency of All Payoffs (Total Spins: {num_simulations})')
plt.xlabel('Payoff Amount (Coins)')
plt.ylabel('Frequency (Log Scale)')
plt.xticks(all_payoffs_labels)
plt.yscale('log') # Logarithmic scale for y-axis
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Add RTP text
plt.text(0.95, 0.95, f'Simulated RTP: {simulated_rtp:.2f}%',
         transform=plt.gca().transAxes, horizontalalignment='right', verticalalignment='top',
         bbox=dict(boxstyle="round,pad=0.3", fc="wheat", ec="black", lw=1))

plt.show()


# --- Game Parameters ---
# Reel strip symbol counts
reel1_counts = {'7': 8, 'CHERRY': 10, 'BAR': 9, 'BLANK': 3}
reel2_counts = {'7': 6, 'CHERRY': 12, 'BAR': 10, 'BLANK': 4}
reel3_counts = {'7': 5, 'CHERRY': 15, 'BAR': 12, 'BLANK': 3}

# Define possible symbols for random selection (based on counts)
reel1_symbols = [symbol for symbol, count in reel1_counts.items() for _ in range(count)]
reel2_symbols = [symbol for symbol, count in reel2_counts.items() for _ in range(count)]
reel3_symbols = [symbol for symbol, count in reel3_counts.items() for _ in range(count)]

# Payout table
payouts = {
    ('7', '7', '7'): 100,
    ('BAR', 'BAR', 'BAR'): 5,
    ('CHERRY', 'CHERRY', 'CHERRY'): 1,
    # All other combinations implicitly pay 0
}

# --- Simulation Settings ---
num_simulations = 5000000 # Number of spins to simulate for robust data

# --- Simulation ---
print(f"Starting simulation of {num_simulations} spins...")
payoff_results = []
for _ in range(num_simulations):
    result_r1 = np.random.choice(reel1_symbols)
    result_r2 = np.random.choice(reel2_symbols)
    result_r3 = np.random.choice(reel3_symbols)
    current_combination = (result_r1, result_r2, result_r3)
    payoff = payouts.get(current_combination, 0)
    payoff_results.append(payoff)
print("Simulation complete.")

# --- Analysis & Data Preparation ---
total_wagered = num_simulations * 1 # 1 coin bet per spin
total_returned = sum(payoff_results)
simulated_rtp = (total_returned / total_wagered) * 100

# Count frequencies of each payoff amount
payoff_counts = pd.Series(payoff_results).value_counts().sort_index()

# Create a DataFrame for summary table
summary_df = pd.DataFrame(index=payoff_counts.index)
summary_df.index.name = 'Payoff (Coins)' # Name the index column for clarity

summary_df['Frequency'] = payoff_counts
summary_df['Probability (%)'] = (payoff_counts / num_simulations * 100).round(4)
summary_df['Total Payout (Coins)'] = summary_df.index * summary_df['Frequency']
summary_df['Contribution to RTP (%)'] = (summary_df['Total Payout (Coins)'] / total_wagered * 100).round(4)

# Add a row for total RTP
total_row = pd.DataFrame({
    'Frequency': summary_df['Frequency'].sum(),
    'Probability (%)': summary_df['Probability (%)'].sum(),
    'Total Payout (Coins)': summary_df['Total Payout (Coins)'].sum(),
    'Contribution to RTP (%)': simulated_rtp
}, index=['TOTAL'])

# Concatenate the total row, setting the index name for 'TOTAL'
total_row.index.name = 'Payoff (Coins)'
summary_df = pd.concat([summary_df, total_row])

# --- Save to Excel ---
output_filename = 'payoff_summary.xlsx'
summary_df.to_excel(output_filename, sheet_name='Payoff Summary', index=True)

print(f"\nPayoff summary successfully saved to '{output_filename}'")
print(f"Simulated RTP: {simulated_rtp:.2f}%")
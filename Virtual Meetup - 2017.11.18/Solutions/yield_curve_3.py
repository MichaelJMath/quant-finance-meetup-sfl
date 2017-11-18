date = '2016-11'

# Get a subset of the dataframe
df = yields.loc[date]

# Calculate the mean, min, and max for each maturity
mean = df.mean(axis=0)
max_ = df.max(axis=0)
min_ = df.min(axis=0)

# Plotting
fig, ax = plt.subplots()

# Plot the mean
ax.plot(maturities, mean, label='Mean Yields')

# Shade between the min and max values
ax.fill_between(maturities, max_, min_, alpha=0.3, label='Yield Range')

# Format the plot and add a legend
ax.set_xticks(maturities)
ax.set_xticklabels(df.columns, rotation=90);
ax.set_title('Yield Curve Mean and Range %s' % date, fontsize=14)
ax.legend();

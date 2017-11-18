# Setup the grid first
fig = plt.figure(figsize=(10,8))
ax1 = plt.subplot2grid((4,1), (0,0), rowspan=2)
ax2 = plt.subplot2grid((4,1), (2,0), sharex=ax1)
ax3= plt.subplot2grid((4,1), (3,0), sharex=ax1)

# Plot the adjusted close on the main grid
spy['Adj Close'].plot(ax=ax1)
spy['Adj Close'].rolling(window=200, min_periods=200)\
    .mean().plot(ax=ax1, color='r')
ax1.set(ylabel='Price', title='SPY')

# Plot Volume Subplot
ax2.bar(spy.index, spy.Volume)

# Plot Rolling 20 day returns
returns = spy['Adj Close'].pct_change(50)
returns.plot(ax=ax3)
ax3.axhline(0, color='k')

# Draw a Lime Green marker on the plot where returns are greater than 15%
spy['Adj Close'][returns>0.15].plot(ax=ax1, ls='none', marker='o', color='lime');

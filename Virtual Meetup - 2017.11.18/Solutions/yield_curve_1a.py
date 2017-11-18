
fig, ax = plt.subplots(figsize=(8,4))
ax.plot(maturities, yields.loc[date].values)
ax.set_title('Yield Curve: %s' % date)
ax.set_xticks(maturities)
ax.set_xticklabels(yields.columns, rotation=90);

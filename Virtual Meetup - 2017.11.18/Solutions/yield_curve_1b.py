df = yields.copy()
df.columns = maturities
fig, ax = plt.subplots(figsize=(8,4))
df.loc[date].T.plot(ax=ax);
ax.set_title('Yield Curve: %s' % date)
ax.set_xticks(maturities);
ax.set_xticklabels(yields.columns, rotation=90);

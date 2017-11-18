
fig, ax = plt.subplots(figsize=(8,4))

for date in dates:
    ax.plot(maturities, yields.loc[date].values, label=date)
    ax.set_title('Yield Curve: %s' % date)
    ax.set_xticks(maturities)
    ax.set_xticklabels(yields.columns, rotation=90);

ax.legend(loc='upper left', bbox_to_anchor=(1,1));

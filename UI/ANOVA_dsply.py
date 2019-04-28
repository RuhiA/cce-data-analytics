import texttable as tt

tab = tt.Texttable()

headings =['Source','SS','MS']
tab.header(headings)

sse=10
ssr=11
sst=sse+ssr

ss=[sse,ssr,sst]

mse=1
msr=6
mst=mse+msr

ms=[mse,msr,mst]

Text=["Error","Regression","Total"]
for row in zip(Text,ss,ms):
    tab.add_row(row)

ANOVA_table=tab.draw()

print(ANOVA_table)


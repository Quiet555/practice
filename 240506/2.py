def fill_table_2d(list2d):
    rows=len(list2d)
    cols=len(list2d[0])
    html='<style> th {padding: 6px; }</style>' + \
         '<table border=1>' 
    index=0
    for r in range(rows):
        html+=f'\n<tr>'
        for c in range(cols):
            html+=f'<th>{list2d[r][c]}</th>'
        html+='</tr>'
    html+='\n</table>'
    return html

lst1=[]
lst=[]
index=1
for i in range(4):
    for x in range(5):
        lst1.append(str(index))
        index+=1
    lst.append(lst1)
    lst1=[]
print(lst)

msg=fill_table_2d(lst)
fname = "112450053.html"
with open(fname, "w") as fp:
    fp.write(msg)

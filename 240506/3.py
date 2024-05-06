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

fname='112_student-TaipeiTech.csv'
with open(fname, "r") as fp:
    msg=fp.read()

lst=[]
msg=msg.split('\n')
msg.pop(-1)
for i in range(len(msg)):
    lst.append(msg[i].split(','))
print(lst)

result=fill_table_2d(lst)

file='112450053.html'
with open(file, "w") as fp:
    fp.write(result)
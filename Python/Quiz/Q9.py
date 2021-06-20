a = dict()
a['name'] = 'python' 
a[('a',)] = 'python'
a[250] = 'python'
#a[[1]] = 'python' 리스트 in 리스트는 x

print(type(a[('a',)]))

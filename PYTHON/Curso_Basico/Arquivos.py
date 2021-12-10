"""
arquivo = open('Luan.txt', 'w')


w -  write - escreve
r - read - ler
a - append - extender
writelines - escrever algo mais complexo


arquivo.write('Luan Flavio')
arquivo.write('\n')
arquivo.write('Curso de Python')
arquivo.write('\n')
arquivo.writelines(['Luan', 'Flavio'])

arquivo.close()
"""

arquivo = open('Luan.txt', 'r')

x = arquivo.read()
print(x)

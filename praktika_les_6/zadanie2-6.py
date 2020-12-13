students = {'Kozlov', 'Stepanov', 'Vazhov', 'Kolesnikov', 'Peresada'}
group_python = {'Kolesnikov', 'Vazhov', 'Stepanov'}
group_java = {'Peresada', 'Stepanov'}
group_front = {'Kozlov', 'Peresada'}
group_full = {'Kolesnikov', 'Vazhov'}
all_students = students | group_python | group_java | group_front | group_full
two_group = group_full & group_python, group_front & group_java, group_python & group_java
print('Студенты, которые учатся в двух и более группах :', two_group)
not_front = all_students - group_java
print('Студенты, которые не изучают FrontEnd :', not_front)
python_java = group_python & group_java
print('Студенты, которые изучают Python и Java :', python_java)

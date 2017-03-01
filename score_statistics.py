# -*- coding: utf-8 -*-

def import_text(filename):
	with open(filename, 'r') as f:
		text_content = f.readlines()
	return text_content

def calc_score(scores):
	# 统计每名学生总成绩、计算平均并从高到低重新排名
	person_scores = []
	for line in scores:
		temp_line = line.split()
		temp_line.append(sum([int(x) for x in temp_line[1:]]))
		temp_line.append(round(temp_line[-1]/(len(temp_line)-2), 1))
		person_scores.append(temp_line)
	person_scores.sort(key = lambda student: student[10], reverse = True)
	
	# 汇总每一科目的平均分和总平均分
	transposed = [list(row) for row in zip(*person_scores)]
	total_avg = []
	for x in transposed[1:]:
		total_sum = sum([int(element) for element in x])
		total_avg.append(round(total_sum / len(x), 1))
	total_avg.insert(0, '平均')
	total_avg.insert(0, '0')

	# 添加名次
	rank = 1
	for x in person_scores:
		x.insert(0, rank)
		rank += 1
	# 替换60分以下的成绩为“不及格”
		for element in x[2:-2]:
			if int(element) < 60:
				x[x.index(element)] = '不及格'
	
	new_scores = person_scores
	new_scores.insert(0, total_avg)
	new_scores.insert(0, ['名次','姓名','语文','数学','英语','物理','化学','生物','政治','历史','地理','总分','平均分'])
	return new_scores

def write_text(filename, scores):
	with open(filename, 'w') as f:
		for line in scores:
			for index in range(0, len(line)):
				line[index] = str(line[index])
			# 	print line[index].decode('utf-8'.encode('cp936')),
			# print
			text = ' '.join(line) + '\n'
			f.writelines(text)

if __name__ == '__main__':
	scores = import_text('report.txt')
	new_scores = calc_score(scores)
	write_text('new_report.txt', new_scores)
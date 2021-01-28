import pandas
import collections


def make_cv_diff_rate_rate(Dataframe):
	cv_diff_rate_Series = Dataframe["cv_diff_rate"]
	cv_diff_rate_rate_Series = Dataframe["cv_diff_rate_rate"]
	last_index = cv_diff_rate_Series.index[-1]

	for index in Dataframe.index:
		if index == last_index: break
		cv_diff_rate_rate_Series.at[index] = cv_diff_rate_Series.at[index] - cv_diff_rate_Series.at[index + 1]
	return cv_diff_rate_rate_Series

def sum_cv_diff_rate_rate(Dataframe):
	cv_diff_rate_rate_Series = Dataframe["cv_diff_rate_rate"]
	SUM = abs(cv_diff_rate_rate_Series).sum()
	return round(SUM,2)



def cv_diff_rate_compare(Dataframe):
	cv_diff_rate_Series = Dataframe["cv_diff_rate"]
	PLUS = cv_diff_rate_Series[cv_diff_rate_Series > 0].sum()
	MINUS = cv_diff_rate_Series[cv_diff_rate_Series < 0].sum()
	return [round(PLUS/ -MINUS, 2), round(PLUS, 2), round(MINUS, 2)]

TOP5 = []

df = pandas.read_csv("stock_history_add.csv", encoding='CP949')

for name, group in df.groupby("stockname"):

	# cv_diff_rate의 +의총합/ cv_diff_rate의 -의총합 의 비율이 가장 큰 TOP5를 선정
	TOP5.append([name,cv_diff_rate_compare(group),sum_cv_diff_rate_rate(group), len(group)])
	# cv_diff_rate의 변화량의 합이 제일 작은 TOP1을 설정
print ("cv_diff_rate의 +의총합/ cv_diff_rate의 -의총합 의 비율이 가장 큰 TOP5")
sorted_list = sorted(TOP5, key=lambda t: t[1][0], reverse = True)
for i in range(0,5,1):
	print (sorted_list[i])

print ("위의TOP5를 cv_diff_rate_rate의 절대값의 총합이 적은순으로 재배열")
TOP5 = sorted_list[:5]
sorted_list = sorted(TOP5, key=lambda t: t[2])
for i in range(0,5,1):
	print (sorted_list[i])




'''
	result = make_cv_diff_rate_rate(group)
	df.loc[result.index, 'cv_diff_rate_rate'] = result


	print(name)

df.to_csv("stock_history_add.csv", index=False, encoding='ms949')
'''
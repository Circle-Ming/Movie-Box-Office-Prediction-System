import matplotlib

matplotlib.use('Agg')  # 不出现画图的框
import matplotlib.pyplot as plt
from io import BytesIO
import base64

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

t1 = str(time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())))
t2 = str(int(t1) - 1000000)
wea_api_url = 叉叉叉
response = requests.get(wea_api_url).content
content = str(response, encoding="utf-8")
total_result = json.loads(content)
dict = total_result
js = json.dumps(total_result, sort_keys=True, indent=4, separators=(',', ':'))

year = []
for element in (total_result['DS']):
    s = ''
    s = element['Year'] + '年' + element['Mon'] + '月'
    year.append(s)
plt.title(year[0] + '杭州地区实时温度')

date = []
for element in (total_result['DS']):
    s = ''
    s = element['Day'] + 'd\n' + element['Hour'] + 'h'
    date.append(s)

tem1 = []
for element in (total_result['DS']):
    tem1.append(eval(element['TEM_Max']))

tem2 = []
for element in (total_result['DS']):
    tem2.append(eval(element['TEM_Min']))

tem3 = []
for element in (total_result['DS']):
    tem3.append(eval(element['TEM']))
try:
    for t in range(len(tem1)):
        plt.plot(date[t], tem1[t], 'ro')
        plt.plot(date[t], tem2[t], 'bd')
        plt.plot(date[t], tem3[t], 'y*')
        plt.pause(0.001)
except Exception as err:
    print(err)

    # plt.plot(date,tem1,'ro')
    # plt.plot(date,tem2,'bd')
    # plt.plot(date,tem3,'y*')

    # 在绘制时设置lable, 逗号是必须的
l1, = plt.plot(date, tem1, label='parabola', color='red', linewidth=1.0, linestyle='--')
l2, = plt.plot(date, tem2, label='line', linewidth=1.0)

plt.plot(color="blue", linewidth=2.5, linestyle="-", label="cosine")
plt.plot(color="red", linewidth=2.5, linestyle="-", label="sine")
plt.legend(handles=[l1, l2, ], labels=['最高温度', '最低温度'], loc='upper left')

plt.ylabel('温度/℃')
plt.xlabel(year[0] + ' 日(d)/时(h)')

sio = BytesIO()
plt.savefig(sio, format='png')
data = base64.encodebytes(sio.getvalue()).decode()
print(data)
plt.savefig('result_temperature')
html = '''
      <html>
          <body>
              <img src="data:image/png;base64,{}" />
          </body>
       <html>
   '''
plt.close()
#return html.format(data)
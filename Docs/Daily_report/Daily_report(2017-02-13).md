# **Daily_report**

## 2017-07-13 수요

#### 이 문서는 *Accuracy_report* 와는 별도로 가지고 있는 모델중 가장 성능이 높은것을 사용하여 매일 100개의 기업의 다음날 종가를 예측하는 보고서이다.

오늘은 넷마블게임즈, 현대로보틱스, 아이엔지생명의 주가가 오를것이라 예측했다.

Company_id | Stock_code | Company_name | Correction
-----------|------------|--------------|------------
0          | 005930     | 삼성전자       | X
1          | 000660     | SK하이닉스     | O
2|005935|삼성전자우|X
3|005380|현대차|O
4|035420|NAVER|X
5|028260|삼성물산|X
6|017760|한국전력|O
7|005490|POSCO|X
8|032830|삼성생명|O
9|012330|현대모비스|O
10|105560|KB금융|O
11|055550|신한지주|O
12|051910|LG화학|X
13|017670|SK텔레콤|O
14|207940|삼성바이오로직스|O
15|034730|SK|O
16|090430|아모레퍼시픽|X
17|033780|KT&G|O
18|096770|SK이노베이션|O
19|000270|기아차|O
20|051900|LG생활건강|O
21|018260|삼성에스디에스|X
22|000810|삼성화재|X
23|086790|하나금융지주|X
24|034220|LG디스플레이|X
25|000030|우리은행|O
26|003550|LG|X
27|251270|넷마블게임즈|X
28|006400|삼성SDI|X
29|011170|롯데케미칼|O
30|066570|LG전자|X
31|010950|S-OIL|O
32|002790|아모레G|X
33|009540|현대중공업|X
34|023530|롯데쇼핑|O
35|010130|고려아연|X
36|030200|KT|O
37|036570|엔씨소프트|X
38|024110|기업은행|O
39|004020|현대제철|X
40|161390|한국타이어|X
41|009150|삼성전기|X
42|021240|코웨이|
43|006800|미래에셋대우|X
44|035250|강원랜드|O
45|139480|이마트|X
46|035720|카카오|X
47|088350|한화생명|
48|032640|LG유플러스|O
49|078930|GS|O
50|047810|한국항공우주|X
51|004800|효성|X
52|086280|현대글로비스|X
53|001040|CJ|O
54|005830|동부화재|X
55|008930|한미사이언스|O
56|018880|한온시스템|O
57|000720|현대건설|O
58|009830|한화케미칼|X
59|027410|BGF리테일|O
60|267250|현대로보틱스|O
61|097950|CJ제일제당|O
62|036460|한국가스공사|O
63|010140|삼성중공업|X
64|029780|삼성카드|O
65|002380|KCC|O
66|128940|한미약품|O
67|009240|한샘|O
68|069500|KODEX 200|X
69|005387|현대차2우B|O
70|005940|NH투자증권|X
71|000120|CJ대한통운|O
72|001450|현대해상|X
73|071050|한국금융지주|O
74|007070|GS리테일|X
75|011070|LG이노텍|X
76|012750|에스원|X
77|138930|BNK금융지주|O
78|016360|삼성증권|X
79|241560|두산밥캣|O
80|012630|현대산업|O
81|000880|한화|X
82|003490|대한항공|O
83|271560|오리온|O
84|047040|대우건설|O
85|000210|대림산업|X
86|079440|아이엔지생명|O
87|028670|팬오션|X
88|008560|메리츠종금증권|X
89|042660|대우조선해양|O
90|000100|유한양행|
91|088980|맥쿼리인프라|O
92|026960|동서|X
93|004990|롯데제과|O
94|047050|포스코대우|O
95|005385|현대차우|X
96|007310|오뚜기|O
97|069960|현대백화점|
98|006260|LS|X
99|000150|두산|X

- 
    와 오늘 정확도가 정말 처참하다... 총 100개의 테스트중 정확도가 55%밖에 나오지 않았다. 물론 전에 테스트케이스로
    실험할 때도 정확도가 낮게 나와서 어느정도 대비는 하고 있었는데 막상 이렇게보니 정말 처참한것 같다. 이번에는 3개 기업의
    주가가 오를것이라 예측했는데 예측중 2개의 기업이 올랐고 1개의 기업은 오르지는 못했으나 떨어지지도 않았다. 즉 오늘은 떨어진
    기업을 올랐다고 예측한 경우는 없다고 볼수 있다. 종가가 저번과 같은 1개의 경우 빼고 44개의 경우 다 올랐는데 오를거라 판단하지 
    못한것이다. 훈련횟수 자체는 5배 증가시켰으며 테스트케이스 자체의 정답률은 77%로 나왔다. 그래서 더 기대했던것 같다.
    (여기서 테스트케이스는 트레이닝 케이스에 없는 것을 사용했기 때문에 어느정도 신뢰도를 가진다고 생각했다.) 주로 보면 오르는 종목을
    오르지 못할 것이라고 판단하는 경향이 좀 심하게 있는것 같다. 나는 그이유가 2달이라는 긴 기간때문이라고 생각한다. 내일 오를지 말지는 
    오늘로부터 과거로 갈수록 중요도가 떨어질수 있다는 생각이 든다. 물론 장기적으로 이 회사의 주가가 오를것이지 판단하려면 그동안의 동향을
    보는게 중요해서 긴 기간을 관찰해보는 것이 중요하다고 생각되기도 한다. 따라서 내일은 3가지 경우로 나눠서 결과표를 만들어보려고 한다
    60일의 긴기간동안 관찰하면서 판단하는 모델, 30일 한달동안 관찰하면서 판단하는 모델, 그리고 마지막으로 딱 일주일만 보고 내일 오를것인지 아닌지
    판단하는 것이다. 이게 금요일날로 가면 주가가 오르는 경향을 보인다고 하니 일주일만 보고 판단하는 모델이 상당히 기대가 된다.
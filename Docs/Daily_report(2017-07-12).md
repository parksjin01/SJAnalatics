# **Daily_report**

## 2017-07-12 수요

#### 이 문서는 *Accuracy_report* 와는 별도로 가지고 있는 모델중 가장 성능이 높은것을 사용하여 매일 100개의 기업의 다음날 종가를 예측하는 보고서이다.

Company_id | Stock_code | Company_name | Correction
-----------|------------|--------------|------------
0          | 005930     | 삼성전자       | X
1          | 000660     | SK하이닉스     | O
2|005935|삼성전자우|X
3|005380|현대차|X
4|035420|NAVER|O
5|028260|삼성물산|O
6|017760|한국전력|O
7|005490|POSCO|O
8|032830|삼성생명|O
9|012330|현대모비스|O
10|105560|KB금융|O
11|055550|신한지주|O
12|051910|LG화학|O
13|017670|SK텔레콤|O
14|207940|삼성바이오로직스|O
15|034730|SK|O
16|090430|아모레퍼시픽|X
17|033780|KT&G|O
18|096770|SK이노베이션|O
19|000270|기아차|X
20|051900|LG생활건강|O
21|018260|삼성에스디에스|O
22|000810|삼성화재|O
23|086790|하나금융지주|O
24|034220|LG디스플레이|O
25|000030|우리은행|O
26|003550|LG|X
27|251270|넷마블게임즈|X
28|006400|삼성SDI|O
29|011170|롯데케미칼|O
30|066570|LG전자|O
31|010950|S-OIL|O
32|002790|아모레G|X
33|009540|현대중공업|O
34|023530|롯데쇼핑|O
35|010130|고려아연|O
36|030200|KT|O
37|036570|엔씨소프트|O
38|024110|기업은행|O
39|004020|현대제철|O
40|161390|한국타이어|O
41|009150|삼성전기|O
42|021240|코웨이|O
43|006800|미래에셋대우|O
44|035250|강원랜드|O
45|139480|이마트|O
46|035720|카카오|O
47|088350|한화생명|X:start1:
48|032640|LG유플러스|O
49|078930|GS|O
50|047810|한국항공우주|O
51|004800|효성|O
52|086280|현대글로비스|O
53|001040|CJ|O
54|005830|동부화재|X:star1:
55|008930|한미사이언스|O
56|018880|한온시스템|O
57|000720|현대건설|O
58|009830|한화케미칼|O
59|027410|BGF리테일|O
60|267250|현대로보틱스|O
61|097950|CJ제일제당|X
62|036460|한국가스공사|O
63|010140|삼성중공업|O
64|029780|삼성카드|O
65|002380|KCC|O
66|128940|한미약품|X
67|009240|한샘|O
68|069500|KODEX 200|O
69|005387|현대차2우B|X
70|005940|NH투자증권|O
71|000120|CJ대한통운|O
72|001450|현대해상|O
73|071050|한국금융지주|O
74|007070|GS리테일|X
75|011070|LG이노텍|O
76|012750|에스원|O
77|138930|BNK금융지주|O
78|016360|삼성증권|O
79|241560|두산밥캣|O
80|012630|현대산업|O
81|000880|한화|O
82|003490|대한항공|O
83|271560|오리온|X (이경우 상장한지 얼마되지 않아서 데이터 부족으로 틀린것 같다)
84|047040|대우건설|O
85|000210|대림산업|O
86|079440|아이엔지생명|:star2:
87|028670|팬오션|X
88|008560|메리츠종금증권|O
89|042660|대우조선해양|O
90|000100|유한양행|X
91|088980|맥쿼리인프라|O
92|026960|동서|O
93|004990|롯데제과|O
94|047050|포스코대우|X
95|005385|현대차우|X
96|007310|오뚜기|O
97|069960|현대백화점|X
98|006260|LS|O
99|000150|두산|O

- 
    여기서 주목해봐야할점은 X의 종류이다. 뭔뜻인가 하면 과연 저게 전날대비 상승한것을 틀린 것인지
    아니면 전날대비 하락했는데 상승했다고 예측한것인지 그 종류역시 중요하다는 뜻이다. 만약 상승한것을 
    하락했다고 다르게 예측한것은 그냥 팔아버리면 되니까 큰 문제가 되지 않고 얻을수 있는 이익이 조금 줄어들
    뿐이다. 그러나 만약 하락한 것을 상승했다고 틀리게 예측해버리면 문제가 된다. 만약 어떤 회사의 주가가
    실제로는 3%가까이 떨어졌음에도 상승했다고 예측한다면 팔 시기를 놓쳐서 큰 손해를 입게된다. 다행이도 20개의
    틀린 케이스중 떨어진것을 올랐다고 착각하는 것은 `27번 넷마블 게임` 뿐이다. 그리고 틀린 케이스를 보면 대부분
    ![Image of Yaktocat](data:image/jpeg;base64,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)
    이런식으로 가운데만 볼록하다던가, 꾸준히 하락세를 그리다가 잠깐 반등한 경우가 많았다. 또한 :star1:이 표시된
    회사를 보면 상승세중 갑작이 급등했을때도 틀린 결과를 보여주는 것을 알수 있다. 물론 약 3개 정도의 케이스는 특별한
    이유없이 틀린 결과를 내는것 같은데 이는 사용한 모델의 한계라고 생각된다. 반대로 유일하게 상승한 케이스를 제대로 맞힌
    :start2:를 보면 3개월 내내 꾸준히 상승세를 보여왔음을 알수 있다. 앞으로의 결과를 지켜보면서 지금의 가설들이 확실한지
    확인할 수 있을 것이라 생각된다.(사용한 모델은 Simple_Analatics)
    
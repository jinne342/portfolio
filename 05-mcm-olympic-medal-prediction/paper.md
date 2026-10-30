# The Medal Tally: Unraveling the Olympic Champions

> 2025 MCM/ICM Problem C 论文全文（团队编号已脱敏为 XXXXXXX，作者元数据已清空）。
> 原始 PDF 见 [paper.pdf](./paper.pdf)。

**Problem Chosen** C 

**Team Control Number** 

**2025 MCM/ICM Summer Sheet** 

XXXXXXX 

# **The Medal Tally: Unraveling the Olympic Champions Summary** 

Every time the Olympic Games are held, the medal table becomes the focus of the world's delightful conversation. Both sports fans and ordinary spectators pay close attention to the performance of athletes from different countries on the field, expecting to see their supporting countries or players to win honours. This paper establishes a prediction model for the medal table of the Olympic Games based on the historical data of previous Olympic Games. 

_The problem analysis are as follows:_ 

For Problem 1, after the data pre-processing was completed, the level of athletes from each country participating in the 2028 Olympic Games was quantified by the Athlete Quality Evaluation Model. Then, the gradient boosting decision tree model ( **GBDT** ) was used to build a model to predict the medal table of the 2028 Olympic Games. The goodness of fit _R2_ of the model is **0.81** , which shows the effectiveness of the model. 

For Problem 2, we analyzed historical Olympic data to determine the number of countries that winning their first Olympic medals at each Olympic Games. A prediction was made using the established GBDT model, which predicted that **12** countries would win their first Olympic medals in 2028. The odds of this prediction being realized was calculated to be **84%** by normalised mean square error. 

For Problem 3, the sports that contribute the most medals are the country's main strengths. Next, we looked at how adding or removing sports by previous Olympic hosts affects medal distribution. **It's clear that the host country has an advantage when new sports are added, while the non-host country competes fairly. However, when sports are decreased, the host country is less competitive in these sports.** 

For question 4, we analyzed the variations in sport winning rates across past Olympic events, identifying when appear significant discrepancies in winning rates as possible moments when great coaches may have emerged. To validate our findings, we cross-referenced these periods with news reports for further corroboration. Utilizing the AHP model, we created an evaluation model. This model showed that great coach effect can improve performance by **11.51%** . We believe that **Korean diving, Japanese tennis and Philippine swimming** sports could employ great coaches to improve performance. 

This study successfully predicts the number of medals in the 2028 Olympic Games, and examines the contribution of sports and medal counts, as well as the issue of great coach effect. This approach can offer the country Olympic committees a scientifically grounded framework for decision-making, enabling them to strategically focus and intensify the training and financial support for sports with demonstrated strengths and emerging potential. Consequently, this would elevate the overall competitive standards and global prestige of Olympic sports. 

### **Keywords: GBDT, AHP, Mann-Whitney U test, Herfindahl Index** 

```
Page 2of25
```

`Team` <mark>`#`</mark> XXXXXXX 

# **Contents** 

|**1 Introduction ...................................................................................................... 3**<br>1.1 Problem Background ....................................................................................................... 3|
|---|
|1.2 Problem Analysis ............................................................................................................. 3|
|**2 Assumptions and Justifications ....................................................................... 4**|
|**3 Notations ........................................................................................................... 5**|
|**4 Problem 1: Medal table prediction & dynamic ranking analysis ............... 6**<br>4.1 Data Description .............................................................................................................. 6|
|4.2 Model Establishment of Problem 1 .................................................................................. 6|
|4.2.1 Comprehensive Athletes Quality Evaluation Model .............................................. 6|
|4.2.2 Building a GBDT model for 2028 Olympic medals table ...................................... 8|
|**5 Problem 2: Predict the number of first-time Olympic medal-winning**<br>**countries in 2028 ................................................................................................ 11**|
|**6 Problem 3: The impact of sports selection on competition results ............ 12**|
|6.1 Each country's dominant sports ..................................................................................... 12|
|6.2 The impact of host sport selection ................................................................................. 14|
|**7 Problem 4: Looking for evidence of hiring great coaches .......................... 15**<br>7.1 Finding the time of hire great coaches ........................................................................... 15|
|7.2 Evaluation model of great coach contribution ............................................................... 17|
|7.3 Three cases for investing in Great Coaching program identified .................................. 19|
|**8 Originality Suggestions .................................................................................. 20**|
|**9 Sensitivity Analysis ......................................................................................... 21**|
|9.1 Sensitivity Analysis of the 2028 Medal Table Prediction Model ................................... 21|
|9.2 Sensitivity Analysis: First-Time Olympic Medal-Winning Countries Prediction Model<br>.............................................................................................................................................. 22|
|**10 Model Evaluation and Further Discussion ................................................ 22**|
|10.1 Strengths ...................................................................................................................... 22|
|10.2 Weaknesses .................................................................................................................. 23|
|10.3 Further Discussion ....................................................................................................... 23|
|**References .......................................................................................................... 24**|
|**Appendices ......................................................................................................... 25**|



```
Page 3of25
```

`Team` <mark>`#`</mark> XXXXXXX 

# **1 Introduction** 

## **1.1 Problem Background** 

The Olympic Games is one of the largest and most widely influential sporting events in the world, attracting top athletes from all over the world. The medal table is an indispensable part of the Olympic Games, which not only reflects the strength of the participating countries in competitive sports, but also witnesses the gradual development of each country's sports from zero to something. Every time the Olympic Games are held, the medal table will become the focus of the world's delightful conversation. 

## **1.2 Problem Analysis** 

In Problem 1, we first screened and identified accurate datasets, defining the range of data available and the objects to be analysed. Then, a dynamic weight adjustment model was used to assess the athletic qualities of the athletes from each country and to determine the list of athletes from each country to participate in 2028. Next, we chose the gradient boosting decision tree model to build the Olympic medal prediction model because of its high prediction accuracy and resistance to overfitting. Finally, we set the prediction points and intervals, predicted the 2028 Olympic medal table, and dynamically analysed the changes in countries' rankings. 

For question 2, we first sorted out the number of countries that winning their first Olympic medals at each Olympic Games, and inserted the processed data into the GBDT model of question 1 to calculate the number of countries that will winning their first Olympic medals in the 2028 Olympic Games. We then introduced the normalised mean square error to calculate the probability of the corresponding event, and finally evaluated the fit of the model through residual analysis. 

For question 3, as we all know, different countries have different national sporting advantages. In other words, the changes in sports events in each Olympic Games will affect the medal situation of each country. In this question, we need to find out each country's sports advantage, and then count the changes in sport events in previous Olympic Games, as well as the proportion of medals won by each country in these sports events. By introducing the MannWhitney U test, we can test for differences in the data set. By calculating the Herfindahl index, we can determine the impact of the sport events selected by the host on the results of different countries. 

For question 4, To explore the 'great coach' effect, we first calculated the medal-winning rates for each event across countries and first identified possible coaching effects by comparing changes in medal-winning rates between two consecutive Olympic Games. We then verified these changes using relevant news reports. Next, an evaluation model was constructed using AHP model to quantify the contribution of great coach effects. Finally, country-specific circumstances were taken into account to provide recommendations for three countries on whether or not to hire a great coach, and to describe the potential benefits of doing so. 

For question five, the model developed in the first four questions and the conclusions 

```
Page 4of25
```

`Team` <mark>`#`</mark> XXXXXXX 

drawn from the model are combined to provide original insights into the physical quality of the athletes, the relationship between the number of medals and the level of the economy, the relationship between the number of medals and sports policy, the impact of the host effect and the role of great coaches, and finally to provide the NOC with information on the relevant insights. 



**Figure 1: OurWork** 

# **2 Assumptions and Justifications** 

Considering those practical problems always contain many complex factors, first of all, we need to make reasonable assumptions to simplify the model, and each hypothesis is closely followed by its corresponding explanation. 

**Overall assumptions:** 

▼Assumption 1: Assumption that the data given in the dataset is completely accurate 

▲Explanation: The paper is completely based on the given data set for analysis. This assumption helps to simplify the model construction process and avoid the introduction of additional complexity and uncertainty due to data quality issues, allowing this paper to focus more on the model structure and parameter estimation. 

▼Assumption3: The events and sports settings of future Olympic Games will remain basically the same as those of past Olympic Games. 

▲Explanations: While some sports may be added or removed from each Olympics, most of the core sports usually remain the same, so we can assume that the future sports will not change much. 

```
Page 5of25
```

`Team` <mark>`#`</mark> XXXXXXX 

### **Question 1 Assumptions:** 

▼Assumption1: Four years later, the number of athletes from each country participating in the competition will remain unchanged, at the same time, the countries participating in the Paris Olympics in 2024 will also participate in the Los Angeles Olympics in 2028. 

▲Explanations: Although the assumptions may not be fully valid in reality, they provide a great convenience for modelling and forecasting. We do not need to collect additional data on the number of participating countries and athletes in the future. This saves a lot of time and effort. 

▼Assumption 2: all athletes are of a similar age at their first Olympic Games 

▲Explanations: This reduces the number of variables that need to be considered in the model. Age is an important factor as it can affect an athlete's fitness, technical maturity and mental state. Many athletes make their Olympic debut between the ages of 20-25 years old<sup>[1]</sup> and athletes in this age group are usually at the peak of their physical and technical abilities. 

▼Assumption 3: The number of events at the 2028 Los Angeles Olympics is equal to the number of events at the 2024 Paris Olympics. 

▲Explanations: This reduces the number of variables to be considered in the model and facilitates quantitative comparisons of the data. 

# **3 Notations** 

The key mathematical notations used in this paper are listed in Table 1. Other none-frequent-used symbols will be introduced once they are used. 

Table1:Notations used in this paper 

|**Symbol**|**Description**|
|---|---|
|_t_<br>|Data weight in the_t_year|
|_m_<br>_h_|The_m_decision tree|
|0<br>_F_|Initial predicted value|
|_m_<br>|The weight of the_m_tree|
|(<br>)<br>_m_<br>_h_<br>|Tree complexity penalty|
|_m_<br>_T_|The number of_j_leaf node in the_m_tree|
|*<br>_mj_<br>_w_|Leaf node weight|
|,2028<br>ˆ_iy_|Predicted medal count for country_i_in 2028|
||Probability of event occurrence|
|,_i j_<br>_r_|The importance proportion of sports events|
|, ,<br>_i j t_<br>_Y_|The winning rate of the country_i_in the_j_event|
|_ij_<sup>_a_</sup>|The importance of the indicator_i_compared to the indicator_j_|
|_K_|Weight matrix|



```
Page 6of25
```

`Team` <mark>`#`</mark> XXXXXXX 

# **4 Problem 1: Medal table prediction & dynamic ranking analysis** 

In this section, we use a dynamic weight adjustment model to rank athletes from different countries according to their comprehensive strength based on existing data. Under the limit of the number of participants in the Olympic Games, we determine the final participants from each country, and then use the gradient boosting decision tree model to predict the medals won by each country in the next Olympic Games, and then analyze the reasons for the fluctuation of the ranking of individual countries. 

## **4.1 Data Description** 

The availability of data must be ensured before data analysis. 

- After data cleaning and analysis, we accurately counted the number of consecutive Olympic Games athletes from each country and plotted the distribution of athletes' participation accordingly. 



Figure2: Athlete's consecutive Olympic participations 



Figure3: Consecutive Olympic Participation Counts 

These charts show that the vast majority of athletes have competed in up to five consecutive Olympic Games, while the majority have competed in only one. As the level of the athletes as the Olympics approached had a high reliability for medal predictions, we decided to use the athletes who competed for the first time in 2012 as a baseline to filter out those who would be suitable to compete at the 2028 Olympics in Los Angeles. 

- We also counted the type and number of medals won by the athletes during their Olympic career, including gold, silver and bronze medals and the year of the award, in order to fully assess the overall sports level of the athletes. Counting the types and number of medals won by each athlete. Count the number of gold, silver and bronze medals each athlete won during the Olympic Games and the year in which they won the medals, so as to evaluate the overall quality of the athletes. 

## **4.2 Model Establishment of Problem 1** 

### **4.2.1 Comprehensive Athletes Quality Evaluation Model** 

First, we build an athlete quality evaluation model. Olympic medal prediction is characterized by strong timeliness and large individual fluctuations. We introduce a dynamic weight adjustment model to make the prediction more in line with recent trends and key data through 

```
Page 7of25
```

`Team` <mark>`#`</mark> XXXXXXX 

differentiated weighting values. 

The time-decay dynamic weight adjustment model is defined as follows: 



<!-- Start of picture text -->
1<br><br>t = 1 + ( T − t ) (1)<br><!-- End of picture text -->

Where,  _t_ is _t_ yearly data weight, _T_ is the current year,  is the attenuation coefficient, and the attenuation coefficients of the past four sessions are = [1.0,0.8,0.6,0.4] . 

Generally speaking, sports competitions meet the general rule of "extreme concentration of top competition", and the difficulty of winning gold, silver and bronze medals is more consistent with exponential distribution<sup>[2]</sup> . Based on the above analysis, the weight function of the gold medal, silver medal, and bronze medal represented by the athlete can be written as: 

= _j ek k_ = 0.2,0.4,0.6 (2) 

As athletes age, they will be affected by factors such as physiological function failure, accumulated injuries, and increased competitive pressure, and their probability of participating in the Olympics will gradually decrease. The probability change usually conforms to the accelerated failure model in survival analysis, which is specifically manifested as the Weibull distribution<sup>[3]</sup> . 

Career Function _S_ ( _t_ ) present the probability that the athlete can still participate in the competition: 



<!-- Start of picture text -->
− ( 1 ) c<br>S ( t ) = e  (3)<br><!-- End of picture text -->

Where,  0 is a scale parameter used to reflect the intensity of sports life. = 4 represents the span of 4 Olympic Games. _c_  0 is the shape parameter, _c_  1 is the risk increases over time. Taking Chinese swimmer Zhang Yufei as an example, the athlete’s career function is: 



<!-- Start of picture text -->
− (1 ) c<br>S ( t ) = e 3 = 0.83 (4)<br>The athlete's sports strength score after comprehensive weighting is:<br>n n<br>vijt =  t j xijtS ( t ) (5)<br>t j<br><!-- End of picture text -->

The athlete's sports strength score after comprehensive weighting is: 

Where, _xijt_ for the _i_ players in _t_ the _j_ Awards. 

By building an evaluation model, we can then get the comprehensive ranking of each athlete. Taking the American athletes participating in the 2028 Olympics as an example, the top twelve athletes in terms of comprehensive quality are as follows. 



Figure4: The top twelve American athletes in terms of quality assessment The above weighted analysis can determine the participants from each country, but the 

```
Page 8of25
```

`Team` <mark>`#`</mark> XXXXXXX 

weighted analysis does not include athletes participating in the Olympics for the first time. We assume that the athletes participating in the Olympics for the first time in 2028 have a similar athletic level to the athletes who do not continue to participate in the Olympics for some reason, and then conduct further analysis. 

### **4.2.2 Building a GBDT model for 2028 Olympic medals table** 

Gradient boosting decision tree is an ensemble learning method that minimizes the loss function by gradually building multiple decision trees. Each new tree attempts to correct the residual of the previous tree, and finally the weighted sum of the prediction results of all numbers is obtained to obtain the final prediction result. 

We introduced this theory into the specific problem of Olympic medal prediction and established a 2028 medal table prediction model based on gradient boosting decision tree. 

①Gradient boosting decision tree by stacking multiple decision trees _hm_ The prediction 

formula corresponding to the gradual fit target is: 



<!-- Start of picture text -->
M<br>ˆ<br>yi = FM ( xi ) + F 0 +  mhm ( xi ) (6)<br>m = 1<br><!-- End of picture text -->

Where, _F_ 0 is the initial prediction value,  is the learning rate, which is introduced to control the contribution of each tree and prevent overfitting<sup>[4]</sup> ,  _m_ for the _m_ the weight of the lesson tree, _hm_ ( _xi_ ) is _m_ the predicted output of the tree. 

②The loss function is specified as: 



<!-- Start of picture text -->
L = 1  N ( yi − y ˆ i )2 +  M  ( hm ) (7)<br>N i = 1 m = 1<br><!-- End of picture text -->

Where,  ( _hm_ ) is the complexity penalty of the tree, and the corresponding function is: 



<!-- Start of picture text -->
1 Tm 2<br> ( hm ) =  Tm +  wmj (8)<br>2 j = 1<br>j  leaf node tree,  wmjmj  for the  m  tree no  j  the weight of<br> regularization coefficient is used for sparse leaf nodes,    for  L 2<br>the regularization coefficient is used to smooth the leaf node weights.<br>N M<br>ˆ<br>M =  L ( yi , yi ) +  ( hm ) (9)<br>i = 1 m = 1<br><!-- End of picture text -->

Where, _Tm_ for the _m_ the tree _j_ leaf node tree, _wmjmj_ for the _m_ tree no _j_ the weight of a leaf node,  for _L_ 1 regularization coefficient is used for sparse leaf nodes,  for _L_ 2 the regularization coefficient is used to smooth the leaf node weights. 

The corresponding overall objective function is: 

③Training the model 



<!-- Start of picture text -->
N<br>1.initialization, F 0 = argmin r  L ( yi , r ) .<br>i = 1<br><!-- End of picture text -->

2.Iterative training, for each tree _m_ = 1,2, , _m_ , calculate the pseudo residual _rim_ = _yi_ − _Fm_ − 1( _xi_ ) , using pseudo residuals as targets, training decision trees _hm_ ( _x_ ) and op- 



<!-- Start of picture text -->
T<br>timize the leaf node weights wmj * ,in wmj * =  xix  i  j 1 j + im  .<br><!-- End of picture text -->

```
Page 9of25
```

`Team` <mark>`#`</mark> XXXXXXX 



<!-- Start of picture text -->
Tm<br>*<br>3.Update the model, Fm ( x ) = Fm − 1( x ) +  wmj I （ x  Left  node j ).<br>i = 1<br><!-- End of picture text -->

4.The training is terminated after a maximum of ten consecutive <u>error rounds.</u> 

- ④Characterization at the athlete level and at the country level: The individual characteristics of athletes are _xijt_ is the result after weight calculation; Country-level features include historical medal count and host country logo. Historical _n_ 

- medal count is _xc_ = _N_ .At the same time, if the country is a host country, its weight is recorded 

- as 1, and if it is not a host country, its weight is recorded as 0. ⑤Next, we make a prediction. The point prediction is defined as 

ˆ _yi_ ,2028 = _FM_ ( _xijt_ ) (10) 

Using quantile regression prediction, take the 5% and 95% quantiles to find the corresponding number of medals, that is, = 0.05 and = 0.95 Quantile prediction: 



<!-- Start of picture text -->
N<br>ˆ<br>Lr =  ( yi − yi ),  ( u ) = u (  − ( u  0)) (11)<br>i = 1<br><!-- End of picture text -->

⑥The grid search method is used to find the value of the regularization parameter, and the following table is obtained after calculation. 

Table 2:The range of values for model parameters 

|Parameter||n_estimators|||max_depth|
|---|---|---|---|---|---|
|Value Range|[0.01,0.05,0.1]|[100,200,300]|[0.1-1.0]|[0.3-1.0]|[3,5,7]|



Substitute the model to predict the data for 2024, and the fitting of the model is shown in the figure below. 



Figure5:Comparison Chart of GBDT Predictions 



Figure6:Comparison Chart of GBDT Prediction Error 

As can be seen from the figure above, the error between the model prediction value and the true value is small, and the model can be used to estimate the Olympic medal table in 2028. When other parameters are disturbed, the model error is always stable within a certain range, which shows that the model has good robustness, so it can be proved that the medal table prediction we give is effective. 

The gradient boosting decision tree model is applied to learn the historical data of gold 

```
Page 10of25
```

`Team` <mark>`#`</mark> XXXXXXX 

medals in the past three Summer Olympics, and then the predicted data of the medal table of the 2028 Los Angeles Olympics and the corresponding results of the prediction interval are obtained as shown in the following table. 

Table 3:Predicted range of medal counts for various countries in 2028 

|NOC|Gold medals|Silver medals|Bronze medals|Total medals|
|---|---|---|---|---|
|USA|46<br>2<br>|44<br>2<br>|43<br>2<br>|133<br>6<br>|
|CHN|38<br>2<br>|26 1<br>|23 1<br>|87<br>4<br>|
|GBR|20 1<br>|20 1<br>|131|533|
|JPN|191|191|141|523|
|AUS|171|171|121|473|



Next, we combine the data predicted by the model to obtain the medal table for the 2028 Los Angeles Summer Olympics, as shown in the figure below. 



Figure7:The top ten of the 2028 Olympic Medal Table and the historical gold medal 

By deeply analyzing the relevant policies implemented by various countries in recent years and the specific events that have occurred, we can reasonably explain the fluctuations in the Olympic rankings in the prediction model. 

Through the "UK Sport" plan, the UK has increased its sports funding by 10% for the 2024-2028 Olympic cycle. This strategic funding investment is aimed at accurately cultivating sports elites. Thanks to the support of this plan and the initial results of the "Talent ID" plan launched after 2016, the new generation of British athletes in swimming, gymnastics and other projects have gradually entered a mature stage and demonstrated strong competitive potential<sup>[5]</sup> . 

Australia is the host of the 2032 Brisbane Olympics. In 2017, the Queensland government said it would continue to promote the current national sports plan (Sport 2030)<sup>[6]</sup> and its followup plans to build a more active Australia. 

The Italian government has provided strong support for the development of sports during the Olympic cycle through various measures such as financial support<sup>[7]</sup> , policy guarantees, infrastructure construction and athlete subsidies. 

As the Olympic host country effect gradually weakens<sup>[8]</sup> , Japan and France are expected 

```
Page 11of25
```

`Team` <mark>`#`</mark> XXXXXXX 

to fall in the rankings of future Olympics. 

# **5 Problem 2: Predict the number of first-time Olympic medal-** 

# **winning countries in 2028** 

In this section, we will use the gradient boosted decision tree model built in problem one to predict the number of countries that will win their first Olympic medals in 2028 and assess the odds of this number occurring. 

In this study, by analyzing the national data of the Olympic medal table, we screened out the countries that made it onto the medal table for the first time in each period and achieved zero breakthrough in Olympic medals. The following table shows the number of countries (NOC) that achieved zero breakthrough in Olympic medals in some periods. 

Table 4: The number of countries that won their first Olympic medal 

|Year|1896|1920|1936|1960|2012|
|---|---|---|---|---|---|
|Count|14|28|13|15|11|



Based on the number of countries that have achieved zero medals in each Olympic Games in historical Olympic data<sup>[9]</sup> , we will predict the number of countries that may achieve zero medals in the Olympics in 2028. 

By using the gradient boosting decision tree model, we predicted the number of countries that may achieve zero Olympic medals in 2028. 

The prediction results show that the number of countries that are expected to achieve zero Olympic medals in 2028 is expected to be 12. The following is a comparison chart of the true value and the model fitting curve. 



Figure8:Comparison of true values and fitted curve 

Then we evaluate the accuracy of this prediction by introducing the normalized mean square error (NMSE), and use it to calculate the odds that 12 countries will achieve zero Olympic medals in 2028. The normalized mean square error is a common indicator used to evaluate the prediction accuracy of regression models. _NMSE_ The smaller the value, the more accurate the prediction result. Its essence is the mean square error divided by the variance of the actual 

```
Page 12of25
```

`Team` <mark>`#`</mark> XXXXXXX 

value. The calculation formula is: 



<!-- Start of picture text -->
n<br>− ˆ 2<br> ( yi yi )<br>NMSE = i = 1<br>n<br>− 2<br> ( yi y )<br>i = 1<br><!-- End of picture text -->



<!-- Start of picture text -->
(12)<br><!-- End of picture text -->

We stipulate the probability  for: 

= (1 − _NMSE_ )*100% (13) The gradient boosting decision tree model is obtained by calculation _NMSE_ . The value is 0.16, and the probability of the corresponding event is = (1 − _NMSE_ )*100% = 84% . 





Figure9:Scatter plot and residual plot of true values and predicted values 

Through the right graph it can be visualised that most of the actual values fall within the error bands, indicating that the model's predictions are relatively accurate. The left graph shows that the data points are uniformly distributed randomly around the zero value, and although there is a certain degree of upward and downward fluctuations, overall it can be concluded that the model fit meets the requirements. 

# **6 Problem 3: The impact of sports selection on competition results** 

## **6.1 Each country's dominant sports** 

In order to explore the impact of sports selection on the results of the competition, we need to find out the dominant sports of each country, and then determine the impact of the number of Olympic sports on each country. This time we take the United States as an example to process and analyze the data. 

This article first sorted out all 55 major sports that have appeared in the history of the Olympic Games. Then, we divided the Olympic history into a time period of every 5 Olympic Games, and made a detailed statistics on the cumulative number of medals won by the United States in each sport. On this basis, we used data visualization methods to draw a three-dimensional waterfall chart of the number of medals to identify those fluctuations that significantly affected the total number of medals won by the United States. By comparing the cumulative number of medals in each sport in each time period with the total number of medals won by the country in that time period, we determined the United States' advantageous sports in each 

```
Page 13of25
```

`Team` <mark>`#`</mark> XXXXXXX 

period. As shown in the figure below. 



Figure10:3D waterfall chart of medal counts for different sports events across different time periods 



Figure11:Top 10 in American advantageous sports 

Then calculate the proportion of medals won in individual events in the five Olympic Games to the country's total medals. The specific formula is as follows: 



<!-- Start of picture text -->
5<br>M<br> i , j , t<br>ri , j = t = 15  100% (14)<br>T<br> i , t<br>t = 1<br><!-- End of picture text -->

We chose to visualize the top ten sports that influence the total number of medals in the United States, as shown in the figure above. It shows the contribution values of the top ten sports in the United States in different time periods. These ten sports are Athletics, gymnastics, cycling, swimming, boxing and so on. Among them, the sport with the largest contribution value is Athletics, with a contribution value of up to 0.32, especially in 1936-1948 and 20082024, showing the important position of track and field in American sports; gymnastics has a high contribution value in 1896-1908 and 1920-1928; swimming has a high contribution value in multiple time periods, especially in 1984-1992 and 1996-2004. In summary, the dominant sports in the United States are Athletics, swimming, gymnastics, wrestling and shooting. 

The results of analyzing France's advantageous sports using the same method are shown in the following table. 

Table5:Top 5 in France advantageous sports 

|Project|Fencing|Cycling|Athletics|Swimming|Shooting|
|---|---|---|---|---|---|
|Weight|0.17|0.12|0.08|0.07|0.06|



From the analysis of the above table, we can see that France's dominant sports are Fencing, Cycling, Athletics, Swimming and Shooting. 

The advantage sports of the hosts of the past five Olympic Games are found out respectively, that is, Japan's advantage sports are swimming, gymnastics, wrestling, judo and track and field; Brazil's advantage sports are track and field, sailing, swimming, beach volleyball and volleyball; Britain's advantage sports are track and field, cycling, swimming, rowing and sailing; China's advantage sports are diving, shooting, weightlifting, swimming and table tennis. 

```
Page 14of25
```

`Team` <mark>`#`</mark> XXXXXXX 

## **6.2 The impact of host sport selection** 

In this problem, we first find out the sports that have been added or removed from the past five Olympic Games. Then we count the number of medals won by the host country and the non-host country in each added or removed event, as well as the corresponding standardized ratio. The specific situation is shown in the figure below. 



Figure12:Standardized Medal Proportion in Added or Removed Projects 

We need to evaluate whether there is a significant difference or relationship between the award data of the host country and the non-host country. The data in the question does not meet the normal distribution and does not have outliers. The data volume is small and continuous, so we introduce the Mann-Whitney U test in statistical tests. The following is the relevant principle of the Mann-Whitney U test<sup>[10]</sup> . 

First, combined the data of the host country and the non-host country and sort them in ascending order. Calculate the rank sum of the two samples respectively. Suppose the rank sum of the host country sample is _RA_ , the rank and the rank of non-host country samples are _RB_ , use the following formula to calculate the two samples _U_ Statistics: 



<!-- Start of picture text -->
U A = nAnB + nA ( n 2 A + 1) − RA<br>(15)<br>U B = nAnB + nB ( n 2 B + 1) − RB<br><!-- End of picture text -->

Where, _nA_ and _nB_ are the sample sizes of host countries and non-host countries respectively. Select the smaller _U_ the value is used as the test statistic, _U_ = min( _U A_ , _UB_ ) . 

Next, select the significance level  If the calculated U value is less than or equal to the critical value, the null hypothesis is rejected and it is considered that there is a significant difference in the distribution of the two samples. If the U value is greater than the critical value, the null hypothesis is not rejected and it is considered that there is no significant difference in the distribution of the two samples. 

The results obtained by substituting the data are shown in the following table. 

Table6:The result of the Mann-Whitney U test 

|Type|U<br>p-value|Type|U<br>p-value|
|---|---|---|---|



```
Page 15of25
```

`Team` <mark>`#`</mark> XXXXXXX 

|Added<br>556.0<br>0.00065|Removed|307.5|0.0758|
|---|---|---|---|



From the above table, we can see that among the new events in the Olympic Games, _p_  _0 05_ . , it can be considered that there are significant differences between host countries and non-host countries; _p_  _0 05_ . , and cannot reflect the differences between host countries and non-host countries. 

Next, we introduce the Herfindahl Index, an indicator for measuring data concentration. It is widely used to evaluate the degree of market competition and concentration. The higher the index value, the higher the market concentration. Its mathematical principle is based on the sum of squares of market shares. In this problem, the host country's data set and the non-host country's data set are regarded as two markets. _n_ enterprises, _i_ the market share of a company is _si_ , by solving the square of each enterprise's market share _si 2_ , to reflect the relative importance of enterprise size, the squared values of the market shares of all data sets are added together to obtain the Herfindahl index, which is calculated as follows: 



<!-- Start of picture text -->
n<br>HHI =  si 2 (16)<br>i = 1<br><!-- End of picture text -->

Through calculation, the Herfindahl index of the host country in the newly added events is 0.4668, and the Herfindahl index of the non-host country is 0.0215. We can see that the Herfindahl index of the host country is significantly higher than that of the non-host country, which shows that the host country has a higher concentration of medals in the newly added sport events, which shows that the host country has strong competitiveness in these sport events and can win more medals. It may also be related to factors such as the host country's Olympic venue settings, resource allocation, and daily training and physical training. 

In the removed events, the Herfindahl index of the host country is 0.3186, and the Herfindahl index of the non-host country is 0.0180. The Herfindahl index of the host country is lower than the Herfindahl index of the newly added events, indicating that the concentration of medals in the reduced events of the host country has decreased, which means that in these reduced events, the competitiveness of the host country has declined relatively, and the performance of other countries has improved; while the index value of the non-host country is lower, indicating that the distribution of medals in the reduced events has a higher dispersion, indicating that more countries have the opportunity to win medals in these events and the competition is more open. 

# **7 Problem 4: Looking for evidence of hiring great coaches** 

## **7.1 Finding the time of hire great coaches** 

Great coaches have the ability to reverse a country's disadvantage in sports, just like volleyball coach Lang Ping and gymnastics coach Bela Karolyi. For countries with relatively scarce sports resources, hiring foreign coaches to supplement the deficiencies of local training has become an effective strategy. In sports powerhouses, foreign coaches play more of a role as strategic mentors. This study analyzes the changes in the number of medals of various countries in the data set to find the great coaches hidden behind the changes in the number of medals. 

Normally, if a country continues its existing sports funding and sports training policies, the number of medals it wins in each Olympics will remain basically the same. However, due 

```
Page 16of25
```

`Team` <mark>`#`</mark> XXXXXXX 

to the hiring of great coaches, the number of medals the country wins in the Olympic Games a few years later may undergo a sudden change. Based on the above ideas, we will explore the time points when the number of medals in each country has increased significantly, and preliminarily infer that these mutations may be related to the addition of great coaches. We assume that the sharp increase in the number of medals is due to the coaching of great coaches. To verify this hypothesis, we will further retrieve the reporting information before and after these time points to confirm whether the country has indeed hired a coach with significant influence. 

Assume country _i_ in the _t_ the first Olympic Games _j_ the winning rate of the projects _Yi_ , _j_ , _t_ , by calculating the difference in medal winning rates between the two sessions as the residual: 



<!-- Start of picture text -->
 i , j , t = Yi , j , t − Yi , j , t − 1 (17)<br><!-- End of picture text -->

In the process of performing data analysis, we used the technique of calculating residuals to process the data in order to standardize the indicator of the number of medals. By using the winning rate of the event in the next session minus the winning rate of the event in the previous session as the residual value, we effectively standardized the variable of the change in the number of medals, ensuring the accuracy and fairness of the data analysis. 

If the residual value is close to1, which usually means that the probability of winning an event has increased significantly between two consecutive Olympic Games, and the number of medals has also increased accordingly. This phenomenon may be attributed to the participation and guidance of great coaches; if a country achieves a zero breakthrough in medals in a certain Olympic event, this historic achievement may also be due to the leadership and motivation of a great coach. 

After considering the above factors, we will process the data systematically. Specifically, we will calculate the residual values of each sport in each Olympic Games, and further count the number of residuals in each event in each Olympic Games. After completing these calculations, we will use data visualization methods to analyze the data outliers in each Olympic Games. The specific analysis results are shown in the figure below. 



Figure13:Olympic Games Level Variation Difference Chart 

In the chart, the "Year" axis indicates the arrangement of data by year, making the changing trend of data each year more intuitive and clear. The "Difference" column is crucial, as it 

```
Page 17of25
```

`Team` <mark>`#`</mark> XXXXXXX 

indicates the difference in the winning rate of each event in two consecutive Olympic Games. It is the core indicator for judging whether there is a "great coach effect". The larger the absolute value of Difference, the more drastic the fluctuation of the winning rate, and the more likely it is to indicate the influence of a great coach. In addition, the "Count" column reveals the frequency of fluctuations in the winning rate in a specific time period, which represents the overall trend of changes in the winning rate in each Olympic Games. 

Obviously, the key to assessing whether a great coach was hired lies in the data in the "Difference" column. In this column, the larger the size and lighter the color of the points, the more significant the difference and the higher the degree of abnormality. Next, we will analyze the "Difference" column to explore those sports with significant fluctuations in winning rates and investigate whether great coaches were indeed hired in the years before these fluctuation points. Through corresponding searches, we found several examples of great coaches being hired near the fluctuation points, and the specific evidence is shown in the following table. Table7:Evidence Table of Hiring Great Coaches 

|**NOC**|**Event**|**Year**|**Difference**|**First-time**<br>**medalwinner**|**Hire a for-**<br>**eign coach**|**Coachame**|
|---|---|---|---|---|---|---|
|CHI|Women's Park|2024|0|Yes|Yes|_DanielDels_|
|SGP|Table Tennis Women's Sin-<br>gles|2012|1|Yes|Yes|_Liang Lijun_|
|EST|Athletics Men's Decathlon|1924|1|Yes|Yes|_Sergey Klevtsov_|
|ESP|Men's Water Polo|1992|1|Yes|Yes|_Dejan Savi_ć|
|CAN|Canoeing Men's Canadian<br>Singles, 1,000 meters|1984|0.667|No|Yes|_Jean-Michel Goudard_|
|AUS|Canoeing Men's Kayak<br>Doubles, 1,000 meters|1972|0.457|No|Yes|_David Smith_|
|ETH|Athletics Men's Marathon|1960|1|Yes|Yes|_Gideon Gathimba_|



In the above table, we can see that seven out of five countries have achieved a breakthrough in Olympic medals after hiring foreign coaches. Estonia and Ethiopia are two countries that tried to hire foreign coaches earlier, and their sports level has been significantly improved. 

Through comprehensive analysis of the data set, combined with actual conditions, we can infer that when the 0 breakout point and anomalies appear in the 0.2 to 0.4 range, it is very likely to mark the teaching of a great coach. 

## **7.2 Evaluation model of great coach contribution** 

In order to deeply evaluate the contribution of great coaches, we constructed a AHP evaluation model<sup>[11]</sup> . The AHP method can decompose complex problems into multiple levels and criteria, and then determine the relative importance of each criterion through pairwise comparison, and then calculate the weight of each option. This model can effectively handle complex problems with multiple levels and criteria, and is particularly suitable for qualitative problems such as the evaluation of the contribution of great coaches, which are difficult to quantify. 

_The following are the key steps of the model:_ 

Step 1. First determine the Option Layer, Criteria Layer and Objective Layer. 

```
Page 18of25
```

`Team` <mark>`#`</mark> XXXXXXX 



Figure14:The hierarchical structure of the coaching contribution evaluation model Step 2. Construct a pairwise comparison matrix, where the elements _aij_ indicators _i_ compared to the index _j_ the importance of _aij_ = 1 ,if _aij_  1, which means that the indicator _i_ ratio index _j_ important; otherwise, the indicator _j_ ratio index _i_ important. 

Step 3. Solve the eigenvector corresponding to the maximum eigenvalue of the pairwise comparison matrix, and then obtain the eigenvector of each indicator to obtain the weight matrix _K_ 



<!-- Start of picture text -->
k<br>K =<br>n (18)<br>k<br> i<br>i = 1<br><!-- End of picture text -->

Where, _k_ is the eigenvector, _n_ is the number of indicators. 

Step 4. Perform consistency check. Only the weights that pass the check can be used. The consistency indicators are: 



<!-- Start of picture text -->
 − n<br>CI = max<br>n − 1 (19)<br><!-- End of picture text -->

Where,  max is the maximum eigenvalue of the pairwise comparison matrix. Next, according to the consistency index _RI_ to calculate _CR_ : 



<!-- Start of picture text -->
CI<br>CR =<br>RI (20)<br><!-- End of picture text -->

If _CR_  0.1 , then the judgment matrix is considered to have satisfactory consistency. The specific consistency test is shown in the following table. 

Table8:Consistency check matrix 

|Matrix Type|CI|CR|Is Consistent Matrix|
|---|---|---|---|
|Rank Matrix|-4.44E-16|-7.66E-16|Yes|
|Gold Medal Matrix|0.08957|0.09952|Yes|
|Silver Medal Matrix|0.02946|0.03274|Yes|
|Bronze MedalMatrix|0.03848|0.04276|Yes|



The above table shows the consistency index and consistency ratio of different matrices, which are used to determine whether each matrix is consistent. The closer the consistency index and consistency ratio values are to 0, the higher the consistency, which means that the weights 

```
Page 19of25
```

`Team` <mark>`#`</mark> XXXXXXX 

derived from these matrices may be valid and reliable. In the above table, the CI and CR values of all matrices are either very close to zero or relatively low, indicating that these matrices are consistent and the weights can be brought into the calculation. 

Step 5. Fill in the weight matrix, calculate the score based on the matrix, and then calculate the contribution of the great coach. 



Figure15:Weight matrix heatmap 

Here is the calculation of the great coach contribution score: 

_S_ = 0.3333  0.1023 + 0.3333  0.1271 + 0.3333  0.1160 = 0.1151 (21) Therefore, the influence of great coaches on the number of medals is 11.51%. 

## **7.3 Three cases for investing in Great Coaching program identified** 

When evaluating whether a country needs to hire a great coach, we need to conduct indepth analysis of a country's economic strength, sports investment budget, the level of development of existing investable projects, and the specific situation of the sport itself. In order to clarify which countries are suitable for hiring great coaches, we have carefully defined a series of key indicators that will provide us with a scientific basis for decision-making. 

- ➢ Countries around the world with an economic level above average also attach importance to investment in sports. 

- ➢ The country has a good foundation for this project but has not won any award in this project. 

- ➢ The selected projects focus more on strategy and competition skills and are also relatively popular projects with investment value. 

After comprehensive consideration of the above, we finally chose sports from three countries: diving from South Korea, tennis from Japan, and swimming from the Philippines. 

Although **Korean diving** has not been as dominant in international competitions as countries such as China and the United States, in recent years, South Korea has made significant progress in this field and has cultivated a group of promising athletes. In the men's single 3- meter springboard final of the 2020 Tokyo Olympics, Korean athlete Yu Ha-ram won fourth place, The result demonstrate the great potential of South Korea in diving. By hiring a great coach, Korean athletes will be able to improve their diving skills more comprehensively, thereby improving South Korea's world ranking in diving. 

```
Page 20of25
```

`Team` <mark>`#`</mark> XXXXXXX 

**Japanese tennis** has a certain foundation, and Kei Nishikori has been among the top five in the world rankings of men's tennis. However, overall, Japan's tennis level still lags behind those tennis powers. As the world's third largest economy, Japan has strong economic strength and a world-leading GDP ranking, which provides stable financial support for the development of tennis. Tennis is a sport that requires skills and strategies. By introducing an outstanding coach, it will greatly promote the improvement of Japan's tennis technology and the development of its overall level, bringing a new leap forward for the development of Japanese tennis. 

In **Philippines swim** , although this country has not won an Olympic medal in swimming, the country has invested a lot of energy in the construction of its sports training system in recent years<sup>[12]</sup> , especially in the field of swimming. The tropical climate conditions in the Philippines and the people's deep interest in water sports provide a unique environment for cultivating top swimmers. Hiring a great coach can not only bring advanced training methods, techniques and tactics to Filipino athletes, but also help them break through the bottleneck of their sports career and improve their competitive level faster. 

Based on our developed Great Coach Contribution Evaluation Model, we've found that exceptional coaches can contribute up to 11.51% to a sport's overall success, which shows that introducing great coaches will have a significant and positive impact on improving the level of sports in these three countries. 

# **8 Originality Suggestions** 

Based on the model established by the first four questions and the conclusions drawn from the model, we put forward original insights on improving the number of Olympic medals from several aspects, including the physical fitness of athletes, the relationship between the number of medals and economic level, the relationship between the number of medals and sports policies, the impact of the host effect, and the role of great coaches. We will eventually submit the relevant suggestions to the National Olympic Committee in the form of a letter. The specific content is shown in Appendix 1. 

- In the **medal table prediction problem** , we established an athlete quality evaluation model. Through model analysis, we noticed that most athletes only participate in one Olympic Games, or at most five Olympic Games. In addition, combined with relevant research data, we found that some Olympic sports have certain restrictions on the age of athletes. If the age restrictions on athletes in these sports can be relaxed, those experienced and still in good condition veterans will have more opportunities to participate in the Olympic Games. This will undoubtedly help increase the chances of winning in these sports and add more excitement to the Olympic Games. 

- The **medal table prediction model** shows that countries with higher economic development levels usually win more medals at the Olympics. The National Olympic Committee can give priority to investing in regions with higher economic development levels, thereby increasing the number of medals for the country as a whole. 

- In **predicting the number of countries that will make a zero breakthrough in Olympic medals** , we can find that if the National Olympic Committee provides fund assistance and calls on outstanding coaches to go to low-income areas to teach, it can help low-income 

```
Page 21of25
```

`Team` <mark>`#`</mark> XXXXXXX 

areas break through the medal count of zero and allow talented children to participate in the Olympic selection<sup>[13]</sup> . 

- In analyzing **the increase and decrease of sports events by the host country** , it was found that new sports events are often added by the host country<sup>[14]</sup> .The National Olympic Committee can give full play to the home advantage, actively optimize the competition environment, and strengthen the training of advantageous sports, which will help increase the number of its own medals. 

- In analyzing **the influence of great coaches** , it was found that the influence of great coaches is as high as 10%-20%. The National Olympic Committee can consider establishing a discussion group for great coaches in the country to allow top sports talents to give lectures in various places to promote the development of sports levels in various regions. At the same time, it is necessary to give preferential treatment to great coaches, treat talents well, and retain talents. 

# **9 Sensitivity Analysis** 

## **9.1 Sensitivity Analysis of the 2028 Medal Table Prediction Model** 

Choose to change the algorithm learning rate  , maximum number of depth, number of decision trees, and regularization parameter are used to evaluate the accuracy of the model. _R_ 2 , _MSE_ , _NMSE_ The algorithm model used in this question is evaluated, and the results are shown in the following table. 

Table 9: Validation of the medal ranking <u>prediction model</u> 

|Model|2<br>_R_|_MSE_|_NMSE_|
|---|---|---|---|
|GBDT|0.81|79.78|0.19|



The goodness of fit of GBDT can be seen from the above table _R_ 2 the score is 0.81, the mean square error _MSE_ the normalized mean square error is 79.82. _NMSE_ the data from 2008 to 2020 in the dataset is used to predict the medal table of the 2024 Paris Olympics. The results are shown in the figure below. 

Through the analysis of the below figure, we can see that the results predicted by the GBDT model are basically consistent with the actual true values. The number of gold medals, silver medals, bronze medals and total medals won by each country fluctuate within a small range above and below the true value. Therefore, we can conclude that the model has a good fitting effect. The specific predicted values are shown in the following table, and the data in brackets are the true values. 

Table10:The Olympic Medal Table for 2024 under the GBDT model 

|NOC|Gold medals|Silver medals|Bronze medals|Total medals|
|---|---|---|---|---|
|USA|42(40)|35(44)|44(42)|121(127)|
|CHN|39(40)|25(27)|24(24)|88(91)|
|JPN|19(20)|18(12)|11(13)|45(45)|
|AUS|18(18)|17(19)|13(16)|48(53)|
|FRA|15(16)|25(26)|26(22)|66(64)|



```
Page 22of25
```

`Team` <mark>`#`</mark> XXXXXXX 



Figure16:Comparison chart of GBDT predicted medal count and actual medal count in 2024 

## **9.2 Sensitivity Analysis: First-Time Olympic Medal-Winning Countries Prediction Model** 

First, we analyze the errors caused by different models. The specific results are shown in the following table. Through this table, we can analyze that the error caused by the GBDT model is the smallest, and the corresponding model has the best fitting effect. 

Table11:Comparison of fitting errors of different models 

|Predictive model|2028prediction|NMSE|Odds|
|---|---|---|---|
|Gradient Boosting Regressor|12.11|0.16|84%|
|Naive Bayes|6|0.6|40%|
|Support Vector Machine|11.89|0.9|10%|
|ElasticNet|6.77|2.22|0|
|Random Forest|11.43|1.56|0|
|K-Nearest Neighbors|9.8|2.11|0|
|Lasso|2.32|2.86|0|



# **10 Model Evaluation and Further Discussion** 

## **10.1 Strengths** 

_Our model offers the following strengths:_ 

```
Page 23of25
```

`Team` <mark>`#`</mark> XXXXXXX 

- ⚫ The gradient boosting decision tree model was used to predict the 2028 Olympic medal table. Compared with other models such as the ARIMA model and the grey prediction model, this model has high accuracy and strong generalization ability, and can better fit the data and perform prediction work. 

- ⚫ When predicting the number of countries that will win Olympic medals for the first time in 2028, the mean square error was introduced based on the existing GBDT model to better evaluate the prediction accuracy of the model. 

- ⚫ In building a model to identify national advantage sports, we focused on in-depth mining and statistical analysis of historical data. This model effectively reduces the errors caused by subjective judgment, thereby significantly improving the scientificity and reliability of the decision-making process. In addition, the model is highly flexible and adaptable, and can flexibly adjust the analysis weight and focus according to the specific national conditions and needs of different countries. 

- ⚫ In the model of finding great coaches, we use the winning rate of each sport instead of the number of medals. Considering that every athlete in a sport in a team competition will win a medal, the winning rate of the sport is the research object. This method makes the model more in line with actual sports competitions. 

## **10.2 Weaknesses** 

Our model has the following limitations: 

- ⚫ The athlete's physical fitness model and the great coach contribution evaluation model are both constructed using the subjective weighting method. This method may lead to a certain subjective tendency in the evaluation results, making the results somewhat one-sided. 

- ⚫ When exploring the dataset for evidence of the influence of great coaches, we inferred the involvement of great coaches by identifying points where the difference in winning rate was significant. However, due to the long time span set by the model, this limited our ability to quickly and accurately locate all key points, resulting in only partial solutions rather than a complete answer from a global perspective. 

## **10.3 Further Discussion** 

Model improvement: Based on the existing athlete physical fitness evaluation model, we collected relevant factors such as the athlete's age, family status, previous awards, injuries, etc., and tried to use the AHP-Entropy-TOSIS model<sup>[15]</sup> .A combination of subjective and objective evaluation can be conducted to further clarify the current level of athletes in the country. At the same time, the model can also be considered for evaluating the contribution of great coaches. 

Model expansion: Comprehensively consider a country's economic development level, sports funding, current athlete level, world political environment and other factors, and introduce these factors as feature vectors of the gradient boosting decision tree. On this basis, we use the model to predict the medal table of the 2028 Los Angeles Olympics in the United States, which can make the prediction results not only more practical, but also more credible and persuasive. 

```
Page 24of25
```

`Team` <mark>`#`</mark> XXXXXXX 

# **References** 

- [1] Elmenshawy, A. R., Machin, D., & Tanaka, H. (2015). Peak performance age in elite athletes: A systematic review. Sports Medicine, 45(1), 83-96. 

- [2] Radicchi F (2012) Universality, Limits and Predictability of Gold-Medal Performances at the Olympic Games. PLoS ONE 7(7): e40335. 

- [3] Selvin S, Survival Analysis for Epidemiologic and Medical Research, University of California, Berkeley: Cambridge University Press, 2010, 111 – 128 

- [4] Natekin, A., & Knoll, A. (2013).Gradient boosting machines, a tutorial. Frontiers in Neurorobotics, 7, 21.DOI: 10.3389. JOURNAL OF HYDROLOGY, 476:433-441, 2013. 

- [5] UK Sport. (2020). Plans for £352 million investment in Olympic and Paralympic sports. Retrieved from www.uksport.gov.uk 

- [6] Queensland Government. (2024). Brisbane 2032 Olympic and Paralympic GamesQueensland Government. Retrieved from https://www.qld.gov.au/about/brisbane2032 

- [7] Mazza B., R.G. (2022). Italian Sport Policies for the Sustainable Development. Cham : Springer Nature ,205-224 

- [8] Baade, R. A., & Matheson, V. A. (2016). Going for the gold: The economics of the Olympics. Journal of Economic Perspectives, 30(2), 201-218. 

- [9] Johnson, D. K. N., & Ali, A. (2004). A tale of two seasons: Participation and medal counts at the summer and winter Olympic Games. Social Science Quarterly, 85(4), 974–993. 

- [10] Nachar, N. (2008). The Mann-Whitney U: A test for assessing whether two independent samples come from the same distribution. Tutor Quantitative Methods Psychology, 4(1), 13-20. 

- [11] Saaty, T. L. (1980). The Analytic Hierarchy Process: Planning, Priority Setting, Resource Allocation. McGraw-Hill International. 

- [12] ABS-CBN News. (2024, February 13). PH set to host Olympic qualifier for swimming. Retrieved from https://www.abs-cbn.com 

- [13] Moore, N., & Gilbert, K. (2008). Globalisation, migration and Olympic success: The role of foreign coaches. International Review for the Sociology of Sport, 43(4), 413-429. 

- [14] Pettigrew, S., & Reiche, D. (2016). Hosting the Olympic Games: An overstated advantage in sports history. The International Journal of the History of Sport, 33(7), 1-15. 

- [15] Chen, C. H. (2020). A novel multi-criteria decision-making model for building material supplier selection based on entropy-AHP weighted TOPSIS. Entropy, 22(2), 259. 

```
Page 25of25
```

`Team` <mark>`#`</mark> XXXXXXX 

# **Appendices** 

**<mark>Appendix 1</mark>** 

<mark>Introduce: A letter to NOC</mark> 





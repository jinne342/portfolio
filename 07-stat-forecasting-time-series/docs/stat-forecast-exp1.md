哈 尔 滨 理 工 大 学 理 学 院 专 业 实 验 报 告 

|课程名称||统计模型及预测||总 评 成 绩|
|---|---|---|---|---|
|实验题目||回归预测|||
|实 验 者|XXX|班级、学号|统计23-2<br>XXXXXXXXXX||
|时 间|2026 年10 月12 日|地 点|新主楼C811||



报告要求及时、认真、完整的完成。报告的主要内容参考如下： ① 实验目的； ② 实验原理； ③ 实 

验仪器；④实验步骤；⑤数据处理（原始数据附后）；⑥实验结果及误差处理；⑦讨论收获、建议等。 

# 一、实验目的 

   - 1.深入理解回归预测方法的原理，明晰其在数据建模与预测中的应用逻辑。 

- 2.熟练掌握构建一元、多元及非线性回归模型的操作流程，包括数据预处理、 

- 模型参数估计等关键步骤。 

- 3.学会运用 SPSS、Python、R 等相关软件实现回归模型的建立、求解及检验， 

- 提升数据分析软件的实际操作能力。 

- 4.能够依据建立的一元、多元、非线性回归模型进行预测，并对预测结果进 

- 行合理分析与评估，增强数据解读和决策支持的能力。 

# 二、实验原理 

本次实验主要围绕多元回归模型展开，通过构建不同类型的非线性回归模型， 对公路旅客周转量与现价 GDP 之间的关系进行建模和预测。下面详细介绍各个 模型的原理和公式。 

① 一元线性回归预测的理论回归模型定义为： _Yi_ =  +  _X i_ +  _i_ 其中，  为总体截距参数，  为总体回归系数；  _i_ 为随机干扰项，满足经典 假设，即随机项满足：零期望、同方差、无自相关、正态分布： 

 2, _i_ = _j E_ (  _i_ ) = 0, _Cov_ (  _i_ , _j_ ) =   0, _i_  _j_ 实际样本回归模型的定义为： _Yi_ = _a_ + _bX i_ + _ei_ ，其中 _a_ , _b_ 为总体参数  , 的样 ˆ 本估计值； _ei_ = _Yi_ − _Yi_ 为残差，代表实际观测与模型拟合值之差。 

预测模型的定义为： _Y_<sup>ˆ</sup> _i_ = _a_ + _bX i_ 

一元线性回归模型建立步骤，首先确定预测对象 _Y_ 和唯一主要影响自变量 _X_ 然后收集成对样本观测 ( _X i_ , _Yi_ ), _i_ = 1,2,  , _n_ ，接着绘制散点图，计算简单相关系数， 初步判断 _X_ 与 _Y_ 是否具备线性相关关系；设定一元线性回归模型形式。最后通过 

1 

最小二乘法进行求解。最小二乘准则是选择估计值 _a_ , _b_ ，使得残差平方和最小：  _ei_ 2 =  ( _Yi_ − _Y_ ˆ _i_ )2 =  ( _Yi_ − _a_ − _bX i_ )2 → min 对 _a_ , _b_ 求偏导并令偏导数等于 0，得到正规方程组，解得参数： 



<!-- Start of picture text -->
n<br><br>  ( X i − X )( Yi − Y )<br>= b i = 1<br>n<br>  ( X i − X )2<br> i = 1<br>= a Y − bX<br><!-- End of picture text -->

- 1 1 

- 其中， _X_ =  _X i_ ， _Y_ =  _Yi_ 为样本均值。回归系数 _b_ 含义为自变量 _X_ 每变动 _n n_ 

- 1 单位，因变量 _Y_ 平均变动 _b_ 个单位。 接着，进行模型检验，规定原假设 _H_ 0<sup>:</sup> = 0 ；备择假设 _H_ 1<sup>:</sup>  0 。构造 _t_ 统 _b_ 

- 计量： _tb_ = _S_ ~ _t_ ( _n_ − 2) ，其中 _Sb_ 为回归系数的标准差；自由度 _df_ = _n_ − 2 。判断规 _b_ 

- 则为| _tb_ |  _t_  /2 ( _n_ − 2) ，拒绝原假设，自变量对因变量影响显著，检验通过；也可依 据 _p_  0.05 拒绝原假设。一元回归中 _t_ 检验等价于 _F_ 检验。回归方程 _F_ 检验用于 整体显著性检验，总离差平方和分解：  ( _Yi_ − _Y_ )2 =  ( _Yi_ − _Y_ ˆ _i_ )2 +  ( _Y_ ˆ _i_ − _Y_ )2 _S yy_ =  ( _Yi_ − _Y_ )2 为总平方和； _Q_ 1 =  ( _Yi_ − _Y_ ˆ _i_ )2 为残差平方和； _Q_ 2 =  ( _Y_ ˆ _i_ − _Y_ )2 为 

- 回归平方和。 _F_ = _<u>Q</u>_ <u>2</u> /1 ~ _F_ (1, _n_ − 2) 若 _F_  _F_  (1, _n_ − 2) ，拒绝 _H_ 0 : = 0 ，回归 _Q_ 1 / ( _n_ − 2) 

- 方程整体线性关系显著。 回归方程模型进行预测，点预测：给定自变量未来取值 _X_ 0 ，代入预测模型 ˆ ˆ 

- _Y_ ˆ0 = _a_ + _bX_ 0 ；区间预测：95%置信区间近似： ( _Y_ 0 − 1.96 _S y_ , _Y_ 0 + 1.96 _S y_ ) 。 ② 多元线性回归预测，是指多个自变量 _X_ 1, _X_ 2,  , _X k_ ， _k_ 为自变量个数。其 

- 理论总体模型定义为： _Yi_ =  0 +  1 _X_ 1 _i_ +  2 _X_ 2 _i_ ++  _k X ki_ +  _i_ ，其中  0 为总体截距；  _j_ 为偏回归系数；  _i_ 随机干扰项，除满足一元回归全部经典假设外，新增假设自 变量之间无多重共线性。 

- 样本实际回归模型的定义为： _Yi_ = _b_ 0 + _b X_ 1 1 _i_ + _b_ 2 _X_ 2 _i_ ++ _bk X ki_ + _ei_ ，其中 

- _b_ 0, _b_ 1,  , _bk_ 为参数样本估计， _ei_ 残差。 ˆ 

- 预测模型的定义为： _Yi_ = _b_ 0 + _b X_ 1 1 _i_ + _b_ 2 _X_ 2 _i_ ++ _bk X ki_ ，偏回归系数 _b j_ 含义：其 

- 他自变量保持不变时，自变量 _X_ 每变动 1 单位，因变量 _Y_ 平均变动 _j b j_ 单位。 

- 矩阵形式表达为： 



<!-- Start of picture text -->
 Y 1   b 0   1 X 11 X 21  X k 1 <br>Y 2 b 1 1 X 12 X 22  X k 2<br>Y = XB + e Y =   , B =   , X =  <br>     <br> Yn   bk   1 X 1 n X 2 n  X kn <br><!-- End of picture text -->

- ③ 非线性回归预测分为三类：可线性化变换模型、多项式回归模型、一般非 

- 线性函数模型。 可线性化模型，变换后转化线性回归，通过最小二乘求解，常见模型： 

2 

_b_ 双曲线模型： _Y_ = _a_ + + _e X_ 

对数模型： _Y_ = _a_ + _b_ ln _X_ + _e b_ 幂函数模型： _Y_ = _aX e_ ，两边取对数线性化 _bX_ 指数模型： _Y_ = _ae e_ ，两边取对数线性化 多项式回归模型，变量替换转为多元线性回归，常见模型为： 2 2 一元二次多项式： _Y_ = _b_ 0 + _b X_ 1 + _b_ 2 _X_ + _e_ ，令 _X_ 1 = _X_ , _X_ 2 = _X_ ，转化为二元 线性回归。同理三次多项式。 一般非线性模型，参数本身非线性，采用泰勒展开迭代的非线性最小二乘法 _Yi_ = _f_ ( _X_ 1 _i_ ,  , _X ki_ ; _b_ 1, _b_ 2,  , _bp_ ) +  _i_ 

线性回归。同理三次多项式。 

非线性回归预测的参数求解方法，包括直接变换法、对数变换法、泰勒级数 展开迭代法。直接变换法，适用于多项式、双曲线、对数、三角函数模型，主要 是通过变量替换，将非线性模型变换为标准线性回归模型，使用普通最小二乘法 OLS 求解参数；对数变换法适用于幂函数、指数模型，等式两边取自然对数，把 参数非线性转变为参数线性；OLS 估计变换后参数，再反变换还原原始模型参 数，泰勒级数展开迭代法适用于非线性最小二乘法，对非线性函数 _f_ ( )  ，给定一 组参数初始值，泰勒展开只保留一阶项，逐次线性逼近，反复迭代直到参数变化 小于给定阈值  ，得到收敛参数估计结果。该计算一般依靠软件完成。 

# 三、实验仪器 

Python3.10 

# 四、实验步骤 

1、运用 Python 读取人寿保险购买额、年均收入、风险反感度样本数据，构 建 DataFrame 数据结构，然后分别绘制人寿保险购买额对年均收入、人寿保险购 买额对风险反感度的散点图，直观观察因变量与两个自变量之间的相关变化趋势， 初步判断变量之间是否存在非线性关系。 

2、基于普通最小二乘法 OLS，依次建立模型一包含交互项的二元二次多项 式模型；模型二不包含交互项的二元二次多项式模型；模型三教材优选多项式模 型；模型四自变量对数回归模型；模型五二元幂函数回归模型五组回归模型。 3、运行模型得到各模型系数、t 统计量、p 值、 _R_ 2 、调整 _R_ 2 、F 统计量等统 计结果，计算每组模型的平均绝对百分误差 MAPE，完成模型拟合效果评价。 4、计算全部模型在 18 个样本上的拟合值，输出实际值与各模型拟合值对比 表格，并保存至 Excel 文件。 

5、绘制全部模型拟合值与实际值对比图、各模型 MAPE 精度对比柱状图， 可视化对比不同模型拟合效果与预测误差。 

6、选择综合表现最优的模型三教材多项式模型，给定自变量新取值，完成 人寿保险购买额的点预测。 

# 五、数据处理 

本实验利用书 68 页例 3-1 的数据，影响购买寿险的因素很多。收入水平、 职业、所在地区等，都会影响购买寿险的行为，但综合考察，不同年均收入和对 风险的反感程度可能是影响的主要因素。由于不同职业、不同年龄的人群收入与 对风险的反感差异较大，因此预测时分别建立预测模型较为合适。为限制影响因 素，在某地区 35-44 岁经理人员中随机抽选 18 人进行调查，得到如表 3-1 所示 

3 

的数据。用 _X_ 2 表示对风险的反感程度，其数值越大，表明对风险越反感； _X_ 1 表 示年均收入。人寿保险额与年均收入、风险反感度之间呈现何种关系形式，事先 并不清楚，只能根据数据分析。原始数据如下： 表 1 实验数据 

|受访者编号|人寿保险购买额（元）|年均收入（千元）|风险反感度|
|---|---|---|---|
|1|19.6|66.29|7|
|2|6.3|40.964|5|
|3|25.2|72.996|10|
|4|8.4|45.01|6|
|5|12.6|57.204|4|
|6|1.4|26.852|5|
|7|4.9|38.122|4|
|8|4.9|35.84|6|
|9|26.6|75.796|9|
|10|4.9|37.408|5|
|11|10.5|54.376|2|
|12|9.8|46.386|7|
|13|7.7|46.13|4|
|14|1.4|30.366|3|
|15|5.6|39.06|5|
|16|24.5|79.38|1|
|17|13.3|52.766|8|
|18|13.3|55.916|6|



首先，我们将人寿保险购买额设定为 Y 轴，年均收入、风险的反感程度分 别设置成 X 轴，然后绘制的散点图如下所示： 



图 1 人寿保险购买额与年平均收入散点图、 

随着年均收入 _X_ 1 上升，寿险保额整体上升；而风险反感度 _X_ 2 和保额之间没 有简单的直线变化趋势。如果散点呈现弯曲、曲线形态，就提示不能直接用线性 模型，可以优先考虑多项式、对数、幂函数等非线性回归模型。因此本文在教材 模型的基础上引入包含交叉项和不含交叉项的多项式非线性回归模型以及用于 对比实验的对数非线性回归模型和幂函数非线性回归模型。 

4 



图 2 人寿保险购买额与风险反感度散点图 

# 六、实验结果 

本次实验共建立 5 个回归模型，分别为模型一包含交互项的二元二次多项 式、模型二不包含交互项的二元二次多项式、模型三教材多项式模型、模型四自 变量对数回归模型、模型五二元幂函数回归模型。利用 Python 实现这 5 种模型 的非线性回归结果如下： 

### 表 2 模型结果 

|模型名称|2<br>_R_|调整<br>2<br>_R_|MAPE(%)|
|---|---|---|---|
|模型一：包含交互项的二元二次多项式|0.999<br>7|0.9996|1.6456|
|模型二：不包含交互项的二元二次多项式|0.999<br>6|0.9995|1.847|
|模型三：教材多项式模型|0.999<br>6|0.9995|1.8388|
|模型四：自变量对数回归模型|0.925<br>4|0.9154|37.5922|
|模型五：二元幂函数回归模型|0.958<br>2|0.9527|14.3575|



包含交互项的二元二次多项式模型整体 F 检验显著，但是 _X_ 22 、交互项 _X_ 1 _X_ 2 对应的 p 值分别为 0.203、0.226，大于 0.05，参数不具备统计显著性。模型 MAPE 为 1.6456%，样本内拟合误差最低，但存在不显著自变量项，变量存在多重共线 性问题；剔除交互项 _X_ 1 _X_ 2 ，保留 _X_ 1, _X_ 2, _X_ 12, _X_ 22 ，模型整体 F 检验显著， _X_ 22 的 p 值等于 0.343$  0.05$ ，该参数依旧不显著。MAPE 为 1.8470%，拟合精度略有下 降；教材多项式模型，剔除不显著的交互项 _X_ 22 ，保留自变量 _X_ 1, _X_ 2, _X_ 12 。所有自 变量 p 值均小于 0.05，全部参数统计显著；F 统计量为 12120，F 值接近于 0，方 程整体线性关系高度显著；调整 R 平方达到 0.9995，说明模型可以解释人寿保 险购买额总变异的 99.95%；MAPE 等于 1.8388%，预测精度很高；DW 统计量为 1.867，数值接近 2，残差不存在明显序列自相关。模型表达式为： _Y_ ˆ = − 6.1995 + 0.0825 _X_ 1 + 0.5669 _X_ 2 + 0.0037 _X_ 12 

该模型和教材例 3-1 结果保持一致，综合各项检验指标，为本实验最优模型； 自变量对数回归模型， _R_ 2 为 0.9254，调整 _R_ 2 为 0.9154，拟合效果远弱于多项式 模型； ln _X_ 2 的 p 值 0.198 大于 0.05，参数不显著；MAPE 高达 37.5922%，预测 误差很大，该模型不适用于本组数据；二元幂函数回归模型，在对数空间完成 OLS 

5 

估计，还原原始因变量空间后 MAPE 达到 14.3575%，预测误差显著高于多项式 类模型，不适合该组样本的预测。 

输出 18 组样本的人寿保险购买额实际值，以及五个模型对应的拟合预测值。 模型一、模型二、模型三多项式类模型的拟合值与样本实际值非常接近；模型四、 模型五部分样本拟合偏差较大，个别样本出现负预测值，不符合人寿保险购买额 现实含义。全部样本数据的实际值、拟合值保存输出至 Excel 文件，便于查阅核 对。由下图可知模型一、二、三多项式模型拟合曲线与实际样本点贴合程度很高； 对数模型、幂函数模型部分样本点拟合偏离程度大。 



图 3 模型拟合值与实际值对比图 

接下来，我们绘制 MAPE 柱状图，MAPE 取值越小模型越好，下图展示五 个模型平均绝对百分误差，模型一 MAPE 最小，但是存在不显著变量；模型三 各项参数全部显著，同时保持很低的 MAPE；模型四 MAPE 显著高于其他模型， 预测效果最差。 



图 4 各模型 MAPE 精度对比图 

接下来，给出样本实际值与各模型拟合值对比，具体如下表： 

表 3 样本实际值与各模型拟合值对比 

|样本id|_Y_|1ˆ_Y_|2ˆ_Y_|3ˆ_Y_|4ˆ_Y_|5ˆ_Y_|
|---|---|---|---|---|---|---|
|1|19.6|19.4888|19.5239|19.599|19.6947|21.6548|
|2|6.3|6.2501|6.2506|6.2626|7.4116|5.5481|
|3|25.2|25.3972|25.4194|25.3304|22.5503|30.1273|



6 

|4|8.4|8.4768|8.4456|8.4584|9.9748|7.4121|
|---|---|---|---|---|---|---|
|5|12.6|12.8966|12.9344|12.9712|15.3071|13.0307|
|6|1.4|1.5318|1.5107|1.5351|-2.9615|1.7813|
|7|4.9|4.5946|4.6318|4.6244|5.3398|4.3738|
|8|4.9|4.9965|4.9345|4.9415|4.3795|4.016|
|9|26.6|26.4437|26.5171|26.5456|23.3304|32.6458|
|10|4.9|4.9261|4.9208|4.9316|5.1813|4.3457|
|11|10.5|10.4706|10.5079|10.4293|13.1117|9.9043|
|12|9.8|9.6896|9.6182|9.607|10.9257|8.2879|
|13|7.7|7.7595|7.7962|7.7971|10.0227|7.3048|
|14|1.4|1.3969|1.4816|1.4399|-0.6412|2.24|
|15|5.6|5.5299|5.5272|5.5382|6.2426|4.8814|
|16|24.5|24.4686|24.3713|24.377|21.4533|23.8719|
|17|13.3|13.1787|13.0979|13.0554|14.2738|12.0375|
|18|13.3|13.4038|13.411|13.4562|15.3035|13.2864|



因此，我们选用最优模型三教材多项式模型，给定输入条件为年均收入 _X_ 1 = 60 千元，风险反感度 _X_ 2 = 6 ，得到人寿保险购买额点预测结果为 15.556。 本文采用 MAPE 平均绝对百分误差作为预测精度评价指标，MAPE 越小， 模型预测精度越高。模型一虽然样本 MAPE 最低，但存在不显著回归系数，存 在多重共线性，若直接用于预测，外推时结果可靠性会下降。遵循教材逐步剔 除不显著变量的建模思路，优先选择全部参数统计显著的模型三作为最终预测 模型。模型四、模型五 MAPE 数值过大，部分预测结果违背经济现实，予以舍 弃。实验中模型输出提示条件数较大，表明多项式衍生特征带来多重共线性， 属于多项式回归的常见现象，通过逐步剔除不显著变量进行缓解。 

# 七、实验收获 

在通过本次人寿保险购买额的非线性回归分析实验，我完整完成了数据预处 理、探索性绘图、多类非线性回归模型构建、统计检验以及模型对比优选的整套 实验流程。实验一共搭建了多项式、对数、幂函数五种不同形式的回归模型，参 照教材逐步剔除统计不显著变量，结合 _R_ 2 、调整 _R_ 2 、MAPE 等多项指标综合评 判模型效果，最终筛选出适配本组样本的最优多项式模型，并且完成样本点预测。 

本次实验带给我的收获是多方面的。理论层面，我不再只是被动记忆课本上 各类非线性模型的公式，而是切实理解多项式、对数、幂函数模型各自的适用场 景，懂得不能单纯依靠 R 平方高低去选择模型。实践操作层面，借助 Python 与 statsmodels 工具完成建模运算，我熟悉了多元非线性回归的完整实操步骤，学会 结合 p 值、F 检验、DW 统计量、MAPE 多项指标综合判断模型优劣，也认识到 多重共线性、参数显著性对于模型的实际影响，体会到逐步回归剔除不显著项这 一建模思路的实际意义。 

这次实验也让我对统计预测建立起更深的感悟。统计建模不是简单追求样本 内的拟合效果，高拟合度不代表模型就可靠，要兼顾参数经济含义、统计显著性 与预测精度。数据不会直接给出答案，需要结合理论、统计指标与业务含义反复 权衡筛选。这也提醒我，后续面对实际数据分析任务，要保持严谨客观的态度， 理性看待模型输出结果，真正学会利用统计工具挖掘数据背后蕴含的信息。 

7 

# 附录 

## <u><mark>模型检验结果</mark></u> 













8 

<u><mark>实验代码</mark></u> **<mark>import</mark>** <mark>pandas</mark> **<mark>as</mark>** <mark>pd</mark> **<mark>import</mark>** <mark>numpy</mark> **<mark>as</mark>** <mark>np</mark> **<mark>import</mark>** <mark>matplotlib.pyplot</mark> **<mark>as</mark>** <mark>plt plt.switch_backend(</mark> **<mark>'TkAgg'</mark>** <mark>)</mark> **<mark>from</mark>** <mark>sklearn.metrics</mark> **<mark>import</mark>** <mark>mean_absolute_percentage_error</mark> **<mark>import</mark>** <mark>statsmodels.api</mark> **<mark>as</mark>** <mark>sm plt.rcParams[</mark> **<mark>'font.sans-serif'</mark>** <mark>] = [</mark> **<mark>'SimHei'</mark>** <mark>] plt.rcParams[</mark> **<mark>'axes.unicode_minus'</mark>** <mark>] =</mark> **<mark>False</mark>** <mark>data_raw = [ {</mark> **<mark>"id"</mark>** <mark>:1,</mark> **<mark>"Y"</mark>** <mark>:19.6,</mark> **<mark>"X1"</mark>** <mark>:66.290,</mark> **<mark>"X2"</mark>** <mark>:7}, {</mark> **<mark>"id"</mark>** <mark>:2,</mark> **<mark>"Y"</mark>** <mark>:6.3,</mark> **<mark>"X1"</mark>** <mark>:40.964,</mark> **<mark>"X2"</mark>** <mark>:5}, {</mark> **<mark>"id"</mark>** <mark>:3,</mark> **<mark>"Y"</mark>** <mark>:25.2,</mark> **<mark>"X1"</mark>** <mark>:72.996,</mark> **<mark>"X2"</mark>** <mark>:10}, {</mark> **<mark>"id"</mark>** <mark>:4,</mark> **<mark>"Y"</mark>** <mark>:8.4,</mark> **<mark>"X1"</mark>** <mark>:45.010,</mark> **<mark>"X2"</mark>** <mark>:6}, {</mark> **<mark>"id"</mark>** <mark>:5,</mark> **<mark>"Y"</mark>** <mark>:12.6,</mark> **<mark>"X1"</mark>** <mark>:57.204,</mark> **<mark>"X2"</mark>** <mark>:4}, {</mark> **<mark>"id"</mark>** <mark>:6,</mark> **<mark>"Y"</mark>** <mark>:1.4,</mark> **<mark>"X1"</mark>** <mark>:26.852,</mark> **<mark>"X2"</mark>** <mark>:5}, {</mark> **<mark>"id"</mark>** <mark>:7,</mark> **<mark>"Y"</mark>** <mark>:4.9,</mark> **<mark>"X1"</mark>** <mark>:38.122,</mark> **<mark>"X2"</mark>** <mark>:4}, {</mark> **<mark>"id"</mark>** <mark>:8,</mark> **<mark>"Y"</mark>** <mark>:4.9,</mark> **<mark>"X1"</mark>** <mark>:35.840,</mark> **<mark>"X2"</mark>** <mark>:6}, {</mark> **<mark>"id"</mark>** <mark>:9,</mark> **<mark>"Y"</mark>** <mark>:26.6,</mark> **<mark>"X1"</mark>** <mark>:75.796,</mark> **<mark>"X2"</mark>** <mark>:9}, {</mark> **<mark>"id"</mark>** <mark>:10,</mark> **<mark>"Y"</mark>** <mark>:4.9,</mark> **<mark>"X1"</mark>** <mark>:37.408,</mark> **<mark>"X2"</mark>** <mark>:5}, {</mark> **<mark>"id"</mark>** <mark>:11,</mark> **<mark>"Y"</mark>** <mark>:10.5,</mark> **<mark>"X1"</mark>** <mark>:54.376,</mark> **<mark>"X2"</mark>** <mark>:2}, {</mark> **<mark>"id"</mark>** <mark>:12,</mark> **<mark>"Y"</mark>** <mark>:9.8,</mark> **<mark>"X1"</mark>** <mark>:46.386,</mark> **<mark>"X2"</mark>** <mark>:7}, {</mark> **<mark>"id"</mark>** <mark>:13,</mark> **<mark>"Y"</mark>** <mark>:7.7,</mark> **<mark>"X1"</mark>** <mark>:46.130,</mark> **<mark>"X2"</mark>** <mark>:4}, {</mark> **<mark>"id"</mark>** <mark>:14,</mark> **<mark>"Y"</mark>** <mark>:1.4,</mark> **<mark>"X1"</mark>** <mark>:30.366,</mark> **<mark>"X2"</mark>** <mark>:3}, {</mark> **<mark>"id"</mark>** <mark>:15,</mark> **<mark>"Y"</mark>** <mark>:5.6,</mark> **<mark>"X1"</mark>** <mark>:39.060,</mark> **<mark>"X2"</mark>** <mark>:5}, {</mark> **<mark>"id"</mark>** <mark>:16,</mark> **<mark>"Y"</mark>** <mark>:24.5,</mark> **<mark>"X1"</mark>** <mark>:79.380,</mark> **<mark>"X2"</mark>** <mark>:1}, {</mark> **<mark>"id"</mark>** <mark>:17,</mark> **<mark>"Y"</mark>** <mark>:13.3,</mark> **<mark>"X1"</mark>** <mark>:52.766,</mark> **<mark>"X2"</mark>** <mark>:8}, {</mark> **<mark>"id"</mark>** <mark>:18,</mark> **<mark>"Y"</mark>** <mark>:13.3,</mark> **<mark>"X1"</mark>** <mark>:55.916,</mark> **<mark>"X2"</mark>** <mark>:6}, ] df = pd.DataFrame(data_raw) Y = df[</mark> **<mark>'Y'</mark>** <mark>].copy() df[</mark> **<mark>'X1_sq'</mark>** <mark>] = df[</mark> **<mark>'X1'</mark>** <mark>] ** 2 df[</mark> **<mark>'X2_sq'</mark>** <mark>] = df[</mark> **<mark>'X2'</mark>** <mark>] ** 2 df[</mark> **<mark>'X1_X2'</mark>** <mark>] = df[</mark> **<mark>'X1'</mark>** <mark>] * df[</mark> **<mark>'X2'</mark>** <mark>] df[</mark> **<mark>'lnX1'</mark>** <mark>] = np.log(df[</mark> **<mark>'X1'</mark>** <mark>]) df[</mark> **<mark>'lnX2'</mark>** <mark>] = np.log(df[</mark> **<mark>'X2'</mark>** <mark>]) X_m1 = df[[</mark> **<mark>"X1"</mark>** <mark>,</mark> **<mark>"X2"</mark>** <mark>,</mark> **<mark>"X1_sq"</mark>** <mark>,</mark> **<mark>"X2_sq"</mark>** <mark>,</mark> **<mark>"X1_X2"</mark>** <mark>]].copy() X_m1 = sm.add_constant(X_m1) mod1 = sm.OLS(Y, X_m1).fit() y_pred1 = mod1.fittedvalues mape1 = mean_absolute_percentage_error(Y, y_pred1)*100 X_m2 = df[[</mark> **<mark>"X1"</mark>** <mark>,</mark> **<mark>"X2"</mark>** <mark>,</mark> **<mark>"X1_sq"</mark>** <mark>,</mark> **<mark>"X2_sq"</mark>** <mark>]].copy() X_m2 = sm.add_constant(X_m2)</mark> 

9 

<mark>mod2 = sm.OLS(Y, X_m2).fit() y_pred2 = mod2.fittedvalues mape2 = mean_absolute_percentage_error(Y, y_pred2)*100 X_m3 = df[[</mark> **<mark>"X1"</mark>** <mark>,</mark> **<mark>"X2"</mark>** <mark>,</mark> **<mark>"X1_sq"</mark>** <mark>]].copy() X_m3 = sm.add_constant(X_m3) mod3 = sm.OLS(Y, X_m3).fit() y_pred3 = mod3.fittedvalues mape3 = mean_absolute_percentage_error(Y, y_pred3)*100 X_m4 = df[[</mark> **<mark>"lnX1"</mark>** <mark>,</mark> **<mark>"lnX2"</mark>** <mark>]].copy() X_m4 = sm.add_constant(X_m4) mod4 = sm.OLS(Y, X_m4).fit() y_pred4 = mod4.fittedvalues mape4 = mean_absolute_percentage_error(Y, y_pred4)*100 Y_log = np.log(Y) X_m5 = df[[</mark> **<mark>"lnX1"</mark>** <mark>,</mark> **<mark>"lnX2"</mark>** <mark>]].copy() X_m5 = sm.add_constant(X_m5) mod5 = sm.OLS(Y_log, X_m5).fit() a_hat = np.exp(mod5.params[</mark> **<mark>"const"</mark>** <mark>]) b1_hat = mod5.params[</mark> **<mark>"lnX1"</mark>** <mark>] b2_hat = mod5.params[</mark> **<mark>"lnX2"</mark>** <mark>] y_pred5 = a_hat * (df[</mark> **<mark>"X1"</mark>** <mark>]**b1_hat) * (df[</mark> **<mark>"X2"</mark>** <mark>]**b2_hat) mape5 = mean_absolute_percentage_error(Y, y_pred5)*100</mark> **<mark>def</mark>** <mark>print_model_info(title, model, mape_val): print(</mark> **<mark>"\n"</mark>** <mark>+</mark> **<mark>"="</mark>** <mark>*70) print(title) print(</mark> **<mark>"="</mark>** <mark>*70) print(model.summary()) print(</mark> **<mark>f"MAPE</mark>** <mark>平均绝对百分误差</mark> **<mark>= {</mark>** <mark>mape_val</mark> **<mark>:.4f} %"</mark>** <mark>) print(</mark> **<mark>f"R</mark>** <mark>平方</mark> **<mark>= {</mark>** <mark>model.rsquared</mark> **<mark>:.6f} ,</mark>** <mark>调整</mark> **<mark>R</mark>** <mark>平方</mark> **<mark>= {</mark>** <mark>model.rsquared_adj</mark> **<mark>:.6f}\n"</mark>** <mark>) print_model_info(</mark> **<mark>"</mark>** <mark>模型一 包含交互项的二元二次多项式</mark> **<mark>"</mark>** <mark>, mod1, mape1) print_model_info(</mark> **<mark>"</mark>** <mark>模型二 不包含交互项的二元二次多项式</mark> **<mark>"</mark>** <mark>, mod2, mape2) print_model_info(</mark> **<mark>"</mark>** <mark>模型三 教材多项式模型</mark> **<mark>"</mark>** <mark>, mod3, mape3) print_model_info(</mark> **<mark>"</mark>** <mark>模型四 自变量对数回归模型</mark> **<mark>"</mark>** <mark>, mod4, mape4) print_model_info(</mark> **<mark>"</mark>** <mark>模型五 二元幂函数回归模型</mark> **<mark>"</mark>** <mark>, mod5, mape5) summary_table = pd.DataFrame({</mark> **<mark>"</mark>** <mark>模型名称</mark> **<mark>"</mark>** <mark>:[</mark> **<mark>"</mark>** <mark>模型一 包含交互项的二元二次多项式</mark> **<mark>"</mark>** <mark>,</mark> **<mark>"</mark>** <mark>模型二 不包含交互项的二 元二次多项式</mark> **<mark>"</mark>** <mark>,</mark> **<mark>"</mark>** <mark>模型三 教材多项式模型</mark> **<mark>"</mark>** <mark>,</mark> **<mark>"</mark>** <mark>模型四 自变量对数回归模型</mark> **<mark>"</mark>** <mark>,</mark> **<mark>"</mark>** <mark>模型五 二 元幂函数回归模型</mark> **<mark>"</mark>** <mark>],</mark> **<mark>"R</mark>** <mark>平方</mark> **<mark>"</mark>** <mark>:[mod1.rsquared, mod2.rsquared, mod3.rsquared, mod4.rsquared, np.nan],</mark> **<mark>"</mark>** <mark>调整</mark> **<mark>R</mark>** <mark>平方</mark> **<mark>"</mark>** <mark>:[mod1.rsquared_adj, mod2.rsquared_adj, mod3.rsquared_adj, mod4.rsquared_adj, np.nan],</mark> **<mark>"MAPE"</mark>** <mark>:[mape1, mape2, mape3, mape4, mape5]</mark> <u><mark>})</mark></u> 

1 

<mark>print(</mark> **<mark>"\n"</mark>** <mark>+</mark> **<mark>"#"</mark>** <mark>*60) print(</mark> **<mark>"</mark>** <mark>全部模型指标汇总对比表</mark> **<mark>"</mark>** <mark>) print(summary_table.round(4)) result_df = pd.DataFrame({</mark> **<mark>"</mark>** <mark>样本</mark> **<mark>id"</mark>** <mark>:df[</mark> **<mark>"id"</mark>** <mark>],</mark> **<mark>"Y</mark>** <mark>实际值</mark> **<mark>"</mark>** <mark>:df[</mark> **<mark>"Y"</mark>** <mark>],</mark> **<mark>"Y</mark>** <mark>预测值模型一</mark> **<mark>"</mark>** <mark>:y_pred1,</mark> **<mark>"Y</mark>** <mark>预测值模型二</mark> **<mark>"</mark>** <mark>:y_pred2,</mark> **<mark>"Y</mark>** <mark>预测值模型三</mark> **<mark>"</mark>** <mark>:y_pred3,</mark> **<mark>"Y</mark>** <mark>预测值模型四</mark> **<mark>"</mark>** <mark>:y_pred4,</mark> **<mark>"Y</mark>** <mark>预测值模型五</mark> **<mark>"</mark>** <mark>:y_pred5 }) result_df = result_df.round(4) print(</mark> **<mark>"\n</mark>** <mark>样本实际值与各模型拟合值对比</mark> **<mark>"</mark>** <mark>) print(result_df) result_df.to_excel(</mark> **<mark>"</mark>** <mark>保险额全部模型拟合结果</mark> **<mark>.xlsx"</mark>** <mark>, index=</mark> **<mark>False</mark>** <mark>) plt.figure(figsize=(8,6)) plt.scatter(df[</mark> **<mark>"X1"</mark>** <mark>], df[</mark> **<mark>"Y"</mark>** <mark>], c=</mark> **<mark>'#add8e6'</mark>** <mark>, s=60, marker=</mark> **<mark>'o'</mark>** <mark>, facecolors=</mark> **<mark>'none'</mark>** <mark>, edgecolors=</mark> **<mark>'#add8e6'</mark>** <mark>, linewidth=1.5) plt.xlabel(</mark> **<mark>"X1</mark>** <mark>年均收入</mark> **<mark>"</mark>** <mark>) plt.ylabel(</mark> **<mark>"</mark>** <mark>人寿保险购买额</mark> **<mark>Y"</mark>** <mark>) plt.title(</mark> **<mark>"</mark>** <mark>人寿保险购买额</mark> **<mark>Y</mark>** <mark>关于</mark> **<mark>X1</mark>** <mark>年均收入散点图</mark> **<mark>"</mark>** <mark>) plt.grid(alpha=0.3) plt.tight_layout() plt.savefig(</mark> **<mark>"</mark>** <mark>散点图</mark> **<mark>X1</mark>** <mark>年均收入</mark> **<mark>.png"</mark>** <mark>, dpi=250) plt.show() plt.figure(figsize=(8,6)) plt.scatter(df[</mark> **<mark>"X2"</mark>** <mark>], df[</mark> **<mark>"Y"</mark>** <mark>], c=</mark> **<mark>'#f0b0b0'</mark>** <mark>, s=60, marker=</mark> **<mark>'o'</mark>** <mark>, facecolors=</mark> **<mark>'none'</mark>** <mark>, edgecolors=</mark> **<mark>'#f0b0b0'</mark>** <mark>, linewidth=1.5) plt.xlabel(</mark> **<mark>"X2</mark>** <mark>风险反感度</mark> **<mark>"</mark>** <mark>) plt.ylabel(</mark> **<mark>"</mark>** <mark>人寿保险购买额</mark> **<mark>Y"</mark>** <mark>) plt.title(</mark> **<mark>"</mark>** <mark>人寿保险购买额</mark> **<mark>Y</mark>** <mark>关于</mark> **<mark>X2</mark>** <mark>风险反感度散点图</mark> **<mark>"</mark>** <mark>) plt.grid(alpha=0.3) plt.tight_layout() plt.savefig(</mark> **<mark>"</mark>** <mark>散点图</mark> **<mark>X2</mark>** <mark>风险反感度</mark> **<mark>.png"</mark>** <mark>, dpi=250) plt.show() plt.figure(figsize=(10,6)) x_index = np.arange(len(df)) plt.plot(x_index, Y, marker=</mark> **<mark>'o'</mark>** <mark>, lw=2, label=</mark> **<mark>"</mark>** <mark>实际</mark> **<mark>Y"</mark>** <mark>, c=</mark> **<mark>'black'</mark>** <mark>) plt.plot(x_index, y_pred1,</mark> **<mark>'--'</mark>** <mark>, label=</mark> **<mark>"</mark>** <mark>模型一 包含交互项的二元二次多项式</mark> **<mark>"</mark>** <mark>, c=</mark> **<mark>'red'</mark>** <mark>) plt.plot(x_index, y_pred2,</mark> **<mark>'--'</mark>** <mark>, label=</mark> **<mark>"</mark>** <mark>模型二 不包含交互项的二元二次多项式</mark> **<mark>"</mark>** <mark>, c=</mark> **<mark>'orange'</mark>** <mark>) plt.plot(x_index, y_pred3,</mark> **<mark>'--'</mark>** <mark>, label=</mark> **<mark>"</mark>** <mark>模型三 教材多项式模型</mark> **<mark>"</mark>** <mark>, c=</mark> **<mark>'blue'</mark>** <mark>)</mark> <u><mark>plt.plot(x_index, y_pred4,</mark></u> **<mark>'--'</mark>** <u><mark>,</mark></u> <mark>label=</mark> **<mark>"</mark>** <mark>模型四 自变量对数回归模型</mark> **<mark>"</mark>** <u><mark>,</mark></u> <mark>c=</mark> **<mark>'green'</mark>** <u><mark>)</mark></u> 

1 

<mark>plt.plot(x_index, y_pred5,</mark> **<mark>'--'</mark>** <mark>, label=</mark> **<mark>"</mark>** <mark>模型五 二元幂函数回归模型</mark> **<mark>"</mark>** <mark>, c=</mark> **<mark>'purple'</mark>** <mark>) plt.xlabel(</mark> **<mark>"</mark>** <mark>样本编号</mark> **<mark>"</mark>** <mark>) plt.ylabel(</mark> **<mark>"</mark>** <mark>人寿保险购买额</mark> **<mark>"</mark>** <mark>) plt.title(</mark> **<mark>"</mark>** <mark>全部模型拟合值与实际值对比图</mark> **<mark>"</mark>** <mark>) plt.legend(fontsize=9) plt.grid(alpha=0.3) plt.tight_layout() plt.savefig(</mark> **<mark>"</mark>** <mark>图</mark> **<mark>3</mark>** <mark>全部模型拟合对比</mark> **<mark>.png"</mark>** <mark>, dpi=250) plt.show() plt.figure(figsize=(12,6)) model_names = [</mark> **<mark>"</mark>** <mark>模型一</mark> **<mark>\n</mark>** <mark>包含交互项的二元二次多项式</mark> **<mark>"</mark>** <mark>,</mark> **<mark>"</mark>** <mark>模型二</mark> **<mark>\n</mark>** <mark>不包含交互项的二 元二次多项式</mark> **<mark>"</mark>** <mark>,</mark> **<mark>"</mark>** <mark>模型三</mark> **<mark>\n</mark>** <mark>教材多项式模型</mark> **<mark>"</mark>** <mark>,</mark> **<mark>"</mark>** <mark>模型四</mark> **<mark>\n</mark>** <mark>自变量对数回归模型</mark> **<mark>"</mark>** <mark>,</mark> **<mark>"</mark>** <mark>模型五</mark> **<mark>\n</mark>** <mark>二元幂函数回归模型</mark> **<mark>"</mark>** <mark>] mape_list = [mape1, mape2, mape3, mape4, mape5] bar_color = [</mark> **<mark>"#c82423"</mark>** <mark>,</mark> **<mark>"#ff8800"</mark>** <mark>,</mark> **<mark>"#2878b5"</mark>** <mark>,</mark> **<mark>"#389c47"</mark>** <mark>,</mark> **<mark>"#90469c"</mark>** <mark>] bars = plt.bar(model_names, mape_list, color=bar_color) plt.ylabel(</mark> **<mark>"MAPE</mark>** <mark>平均绝对百分误差</mark> **<mark>"</mark>** <mark>) plt.title(</mark> **<mark>"</mark>** <mark>各模型</mark> **<mark>MAPE</mark>** <mark>精度对比图</mark> **<mark>"</mark>** <mark>) plt.grid(axis=</mark> **<mark>'y'</mark>** <mark>, alpha=0.3)</mark> **<mark>for</mark>** <mark>bar</mark> **<mark>in</mark>** <mark>bars: height = bar.get_height() plt.text(bar.get_x()+bar.get_width()/2., height+0.12,</mark> **<mark>f'{</mark>** <mark>height</mark> **<mark>:.2f}'</mark>** <mark>,ha=</mark> **<mark>'center'</mark>** <mark>,va=</mark> **<mark>'bottom'</mark>** <mark>) plt.tight_layout() plt.savefig(</mark> **<mark>"</mark>** <mark>图</mark> **<mark>7MAPE</mark>** <mark>模型对比柱状图</mark> **<mark>.png"</mark>** <mark>,dpi=250) plt.show( new_sample = pd.DataFrame({</mark> **<mark>"const"</mark>** <mark>:[1],</mark> **<mark>"X1"</mark>** <mark>:[60],</mark> **<mark>"X2"</mark>** <mark>:[6],</mark> **<mark>"X1_sq"</mark>** <mark>:[60**2] }) pred_val = mod3.predict(new_sample) print(</mark> **<mark>"\n</mark>** <mark>点预测演示 模型三 教材多项式模型</mark> **<mark>"</mark>** <mark>) print(</mark> **<mark>f"</mark>** <mark>输入条件 年均收入</mark> **<mark>X1</mark>** <mark>等于</mark> **<mark>60</mark>** <mark>千元 风险反感度</mark> **<mark>X2</mark>** <mark>等于</mark> **<mark>6"</mark>** <mark>)</mark> <u><mark>print(</mark></u> **<mark>f"</mark>** <mark>预测人寿保险购买额</mark> **<mark>= {</mark>** <u><mark>pred_val.values[0]</mark></u> **<mark>:.3f}"</mark>** <u><mark>)</mark></u> 

1 


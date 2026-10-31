# 哈 尔 滨 理 工 大 学 理 学 院 专 业 实 验 报 告 

|课程名称||时间序列分析||总 评 成 绩|
|---|---|---|---|---|
|实验题目||平稳时间序列分析与建模|||
|实 验 者|XXX|班级、学号|统计23-2班<br>XXXXXXXXXX||
|时 间|2026.04.29|地 点|新主楼C911||



报告要求及时、认真、完整的完成。报告的主要内容参考如下：①实验目的；②实验原理；③实 

验仪器；④实验步骤；⑤数据处理（原始数据附后）；⑥实验结果及误差处理；⑦讨论收获、建议等。 

## 一、实验目的 

- 1.理解时间序列数据的基本结构和特征； 

- 2.了解纯随机性检验的目的和原理，能够判断时间序列是否为白噪声序列； 

- 3.学会根据平稳时间序列的自相关函数（ACF）和偏自相关函数（PACF）的特点，选择合 适的时间序列模型； 

- 4.学会运用相应的方法进行模型参数的估计，从而建立能够准确描述时间序列数据生成机制 的模型； 

- 5.掌握对建立的时间序列模型进行检验的方法。 

## 二、实验原理 

拿到一个观察值序列之后，首先要对序列的平稳性和纯随机性进行检验。 

### **1.** 平稳性检验 

对序列的平稳性检验有两种方法： 

- （1）根据 时序图和自相关图的特征 作出判断的图检验方法。 

时序图检验方法 的原理是平稳时间序列具有常数均值和方差。这意味着平稳序列的时 序图应该显示出该序列始终在一个常数值附近波动，而且波动的范围有界的特点。 

自相关图 是一个平面二维坐标悬垂线图，横坐标表示延迟期数，纵坐标表示自相关函 数，悬垂线的长度表示自相关系数的大小。由于平稳序列通常具有短期相关性，该性质用自 

相关系数来描述就是随着延迟阶数 _k_ 的增加，平稳序列的自相关系数  _k_ 会很快地衰减向 0； 

反之，非平稳时间序列的自相关系数  _k_ 衰减向 0 的速度通常较慢。这就是我们利用自相关 图进行平稳性判别的标准。 （2）构造检验统计量进行假设检验 

### **2.** 纯随机性检验 

（1）纯随机序列的定义 

> 如果时间序列  _X t_  满足下列性质： 

a) 任取 _t_  _T_ ，有 _EX t_ =  

b) 任取 _t_ , _s_  _T_ ，有 



<!-- Start of picture text -->
 2, t = s<br> ( t , s ) = <br> 0, t  s<br><!-- End of picture text -->

> 称序列  _X t_  为纯随机序列，也称为白噪声序列。 

- （2）纯随机性 由于白噪声序列具有如下性质： 



<!-- Start of picture text -->
= k 0,  k 0<br><!-- End of picture text -->

这说明白噪声序列的各项序列值之间没有任何相关关系，如果序列值之间呈现出某种 显著的相关关系  _k_  0,  _k_ 0 ，说明该序列不是纯随机序列。 

### **3.** 时间序列模型 

- （1）AR 模型： _xt_ = 0 + 1 _xt_ − 1 + 2 _xt_ − 2 + + _p xt_ − _p_ +  _t_ 

（2）MA 模型： _xt_ = +  _t_ − 1 _t_ − 1 − 2 _t_ − 2 − − _q t_ − _q_ 

（3）ARMA 模型： _xt_ = 1 _xt_ − 1 ++ _p xt_ − _p_ +  _t_ − 1 _t_ − 1 − − _q t_ − _q_ 

||自相关函数ACF|偏自相关函数PACF|
|---|---|---|
|AR|拖尾|截尾|
|MA|_q_阶截尾|拖尾|
|ARMA|拖尾|拖尾|



三、实验仪器 R4.4.3 以及 RStudio 四、实验步骤 

五、数据处理 

六、实验结果分析 

七、实验收获 

指导教师： XXX _ 2026年4月13日 

<u><mark>实验代码</mark></u> data(airquality) aq <- na.omit(airquality) print(head(aq, 15)) cat("\n 数据维度：", dim(aq), "\n") ozone_5 <- aq$Ozone[aq$Month == 5] ozone_7 <- aq$Ozone[aq$Month == 7] before <- aq$Ozone[-nrow(aq)] after  <- aq$Ozone[-1] diff   <- after - before may <- subset(aq, Month == 5, c(Ozone, Day)) jul <- subset(aq, Month == 7, c(Ozone, Day)) paired <- merge(may, jul, by = "Day") colnames(paired) <- c("Day", "May", "Jul") # Mann-Whitney U 检验 print(wilcox.test(ozone_5, ozone_7, paired = F)) #符号检验 np <- sum(diff > 0, na.rm = T) nn <- sum(diff < 0, na.rm = T) s  <- min(np, nn) pv <- binom.test(s, np + nn)$p.value cat("正差值：", np, " 负差值：", nn, "\n") cat("统计量 S：", s, "  p 值：", round(pv, 4), "\n") #Wilcoxon 符号秩检验 print(wilcox.test(before, after, paired = T)) if (!require(ggplot2)) install.packages("ggplot2") library(ggplot2) c5 <- "#f2c078" c7 <- "#e88a93" line_grey <- "gray70" df <- data.frame( Month = rep(c("May", "Jul"), each = nrow(paired)), Ozone = c(paired$May, paired$Jul), ID    = rep(1:nrow(paired), 2) ) p1 <- ggplot(df, aes(Month, Ozone)) + geom_violin(aes(fill = Month), trim = T, alpha = 0.85) + geom_boxplot(width = 0.13, fill = "white", outlier.shape = NA) + geom_line(aes(group = ID), col = line_grey, alpha = 0.5, lwd = 0.7) + geom_point(aes(col = Month), size = 1.8, alpha = 0.7) + scale_fill_manual(values = c("May" = c5, "Jul" = c7)) + scale_color_manual(values = c("May" = "#d4a76a", "Jul" = "#d97a85")) + labs(title = "5 月与 7 月臭氧浓度配对比较", y = "臭氧浓度 (ppb)") + theme_classic() + theme(plot.title = element_text(hjust = 0.5), legend.position = "none") print(p1) dev.new() hist(diff, col = c5, border = "#d49a4a", main = "相邻日期臭氧浓度差值分布", xlab = "差值") dev.new() plot(before, after, pch = 19, col = adjustcolor(c7, 0.7), main = "相邻日期臭氧浓度散点图", xlab = "前一日", ylab = "后一日") abline(0, 1, col = "red", lty = 2, lwd = 2) dev.new() qqnorm(diff, pch = 19, col = adjustcolor(c5, 0.7), main = "差值 Q-Q 图") <u>qqline(diff, col =</u> "red", lwd = 2) 


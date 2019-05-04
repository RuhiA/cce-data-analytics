1. There is 1 python file in this folder - linearRegression.py
2. There is 1 test file in this folder - demo.xlsv. It is on this file that linear regression is performed.
3. The file could be run as:  python3 linearRegression.py pathOfXlsxFile columnXTitle columnYTitle
4. The given file will be populated with x-mean, y-mean, (x-mean)sq, (y-mean)sq, (x-xmean)(y-ymean) after execution of the program
5.The program will output m and c values of linear relation if the correlation coefficient between x and y values is significant



Functions | Input | Output          
------------ | --------------- | ------------------
1.)sumOfColumn()| columnTitle | calculates sum of all elements in gven column
2.)meanOfColumn()|columnTitle | calculates mean of all elements of a column
3.)addColumnMinusMean()| columnTitle | calculates sum(x-xmean)
4.)addSquareOfColumn() | columnTitle | calculates sux(xsquare)
5.)addProductOfColumns() | col1, col2 | calculate sum(col1*col2)
6.)stdDeviation() | columnTitle | calculates stdDeviation Of given column
7.)covariance() | col1, col2 | calculates covariance between col1 and col2
8.)correlation()| col1, col2 | calculates correlation between col1 and col2
9.)linearRegression() | col1, col2 | calculates linear relation i.e. m and c between col1 and col2
10)mapColumnsWithIndex() | void | creates a map mapping index with columnTitle in excel

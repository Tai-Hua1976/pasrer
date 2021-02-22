CPU = "CA55"

if CPU == "CA53":
    f = open('CA53_3.log')
    f2 = open('CA53_3_result.csv','w')
else:
    f = open('CA55_3.log')
    f2 = open('CA55_3_result.csv','w')

try:
    item=0
    print('No, Running No, Test Name, Average time (us), Std dev (%), Min time (us), Max time (us), Median time (us)')
    print('No, Running No, Test Name, Average time (us), Std dev (%), Min time (us), Max time (us), Median time (us)', file = f2)
    for line in f:
        if line.find('Running') != -1:
            line_running_no=line[(line.find('[')+1):line.find(']')]
            line_testname=line[(line.find('NEON')):(len(line)-2)]
            item=item+1
        elif line.find('Wall clock/Wall clock time:') != -1:
            line_avg=line[(line.find('AVG=')+4):(line.find('us, STDDEV')-1)]
            line_stddev=line[(line.find('STDDEV=')+7):(line.find('%, MIN')-1)]
            line_min=line[(line.find('MIN=')+4):(line.find('us, MAX')-1)]
            line_max=line[(line.find('MAX=')+4):(line.find('us, MEDIAN')-1)]
            line_median=line[(line.find('MEDIAN=')+7):(line.find('us/n')-2)]
            print(item,',',line_running_no,',"'+line_testname+'",',line_avg,',',line_stddev,',',line_min,',',line_max,',',line_median)
            print(item,',',line_running_no,',"'+line_testname+'",',line_avg,',',line_stddev,',',line_min,',',line_max,',',line_median, file = f2)
finally:
    f.close()
    f2.close()

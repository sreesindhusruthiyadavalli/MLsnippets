def fittingBlocks(input1,input2):

#Write code here
    
    rst = ''
    list_length = len(input1)
    #print list_length
    for i in range(list_length - 1):
        for x in range(i+1, list_length):
            #print i, x
            
            if (input1[i] + input1[x]) == input2:
                if input1[i] < input1[x]:
                    #temp = "%d+%d" % (input1[i], input1[x])
                    temp = str(input1[i]) + "+" +str(input1[x])
                    #print temp
                    if rst == '':
                        rst = temp
                    else:
                        rst = rst + "," +  temp
                    #result.append(temp)
                    #print i,x, result
                else:
                    temp = "%d+%d" % (input1[x], input1[i])
                    if rst == '':
                        rst = temp
                    else:
                        rst = rst + "," +  temp

                    #result.append(temp)
                            
    return rst
    
    
    
    
    
input1 = [5, 8, 12, 15, 20, 21]
input2 = 20  
print fittingBlocks(input1,input2)  





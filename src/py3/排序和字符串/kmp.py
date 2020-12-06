def kmp(mom_string,son_string):
    # 传入一个母串和一个子串
    # 返回子串匹配上的第一个位置，若没有匹配上返回-1
    test=''
    if type(mom_string)!=type(test) or type(son_string)!=type(test):
        return -1
    if len(son_string)==0:
        return 0
    if len(mom_string)==0:
        return -1
    #求next数组
    next=[-1]*len(son_string)
    if len(son_string)>1:# 这里加if是怕列表越界
        next[1]=0
        i,j=1,0
        while i<len(son_string)-1:#这里一定要-1，不然会像例子中出现next[8]会越界的
            if j==-1 or son_string[i]==son_string[j]:
                i+=1
                j+=1
                next[i]=j
            else:
                j=next[j]

    # kmp框架
    m=s=0#母指针和子指针初始化为0
    ans = []
    # 原来的基础上完善，可以循环找更多的匹配串
    while m<len(mom_string):
        if  s==len(son_string) - 1  and mom_string[m]==son_string[s]: #匹配成功；子串最后一位正好匹配上了，
                                                                      #不让s + 1，s变成一个新的匹配；
            print('匹配成功,位置是：%d' % (m - s))
            ans.append(m-s)
            s = next[s]

        if s==-1 or mom_string[m]==son_string[s]:
            m+=1
            s+=1
        else:
            s=next[s]


        #匹配失败
    return ans

# 测试

if __name__ == "__main__":
    mom_string='89uababababcafgabababca'
    son_string='abababca'
    print(kmp(mom_string,son_string))


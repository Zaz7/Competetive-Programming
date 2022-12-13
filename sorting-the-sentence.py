class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        shuffled = s.split(" ")
        re_shuffeled = ""
        for i in range(len(shuffled)):
            m_index = i
            for j in range(i+1 , len(shuffled)):
                if shuffled[j][-1] < shuffled[m_index][-1]:
                    m_index = j 
            if i != m_index: 
                shuffled[m_index],shuffled[i] = shuffled[i],shuffled[m_index]
            re_shuffeled += shuffled[i][:-1]  + ' '
        return (re_shuffeled[0:-1] )
         
       

def MaxSubarray(self,nums):
    c_s=nums[0]
    m_s=nums[0]
    for num in nums[1:]:
        c_s=max(num,c_s+num)
        m_s=max(c_s,m_s)
    return m_s
#!/usr/bin/env python
# coding: utf-8

# In[26]:


apart = [ [101, 102], [201, 202], [301, 302]]

for row in apart:       # row(행) 명령어로 apart 리스트 안에 있는 행 정렬
    for col in row:     # col(열) 명령어로 apart 리스트 안에 있는 열 정렬
        print(col, "호")  # col 뒤에 "호" 붙여서 출력
print("-" * 5)            # - 5개 출력


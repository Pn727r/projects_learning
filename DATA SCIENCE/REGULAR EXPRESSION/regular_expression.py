import re

str = '''Physics 
is the branch of science that
deals with the structure of matter and how
the fundamental constituents of the universe interact. 
It studies objects rangingfrom the very small using quantum 
mechanics to the entire universe using general relativity.

The Tata Group is an Indian multinational conglomerate headquartered 
in Mumbai. Established in 1868, it is India's largest conglomerate, 
with products and services in over 150 
countries, and operations in 100 countries across six continents.

Parent organization: Tata Sons
Subsidiaries: Tata Motors, Tata Steel Ltd, MORE
Founder: Jamsetji Tata
Founded: 1868, Mumbai
Revenue: 12,800 crores USD (2022)
Headquarters: Mumbai
parthnagariya789@rku.ac.in 
pnagariya123@gmail.com
Number of employees: 9,35,000 2022'''

# findall search split sub finditer

print(re.search(r"\." , str))

match = re.findall(r'[M]',str) # return in list
print(match)

print(re.search(r'^P',str))
print(re.search(r'2022$' , str))

print(re.search(r"P.y" , str))

print(re.search(r'Tata|Phy' , str)) # phy or tata any match return

print(re.findall(r'Ta?t', str)) 

print(re.findall(r'Ta*t',str))

import urllib2
from bs4 import BeautifulSoup

#definition of functions used
# def my_function():
    # print("Hello From My Function!")

# def my_function_with_args(username, greeting):
    # print("Hello, %s , From My Function!, I wish you %s"%(username, greeting))


def sum_two_numbers(a, b):
    return a + b


#calling of functions
# my_function()
# my_function_with_args("John Doe", "a great year!")
x = sum_two_numbers(1,2)

#printing vlaue
# print x


wiki = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"
page = urllib2.urlopen(wiki)
# print page
soup = BeautifulSoup(page,"html.parser")

right_table=soup.find('table', class_='wikitable sortable plainrowheaders')
trs = right_table.findAll("tr")
for each_tr in trs:
    # print each_tr
    th = each_tr.findAll("th")
    # print th
    # print th[0].find(text=True)
    tds = each_tr.findAll("td")
    if len(tds) < 1:
        continue
    print  tds[0].find(text=True), th[0].find(text=True), tds[1].find(text=True), tds[4].find(text=True)
    # for eachtd in tds:
    #     print eachtd.text
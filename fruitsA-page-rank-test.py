
import testingtools
import crawler
import searchdata
import search
output = open('fruitsA-page-rank-failed.txt', 'w')
success_output = open('fruitsA-page-rank-passed.txt', 'w')

#Performing crawl starting at seed https://people.scs.carleton.ca/~avamckenney/fruitsA/N-0.html
crawler.crawl('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-0.html')
#Test #0 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-7.html
expected = 0.00842744607991679
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-7.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #0 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-7.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #0 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-7.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #1 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-42.html
expected = 0.011154456645823681
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-42.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #1 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-42.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #1 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-42.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #2 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-21.html
expected = 0.008146450733114232
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-21.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #2 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-21.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #2 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-21.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #3 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-39.html
expected = 0.009554372228209911
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-39.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #3 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-39.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #3 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-39.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #4 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-22.html
expected = 0.009209149498372309
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-22.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #4 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-22.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #4 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-22.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #5 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-8.html
expected = 0.009568218662109124
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-8.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #5 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-8.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #5 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-8.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #6 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-32.html
expected = 0.00989042024734023
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-32.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #6 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-32.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #6 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-32.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #7 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-1.html
expected = 0.007787506718804841
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-1.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #7 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-1.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #7 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-1.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #8 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-13.html
expected = 0.010692925808903712
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-13.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #8 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-13.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #8 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-13.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #9 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-45.html
expected = 0.010246641185165176
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-45.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #9 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-45.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #9 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-45.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #10 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-47.html
expected = 0.011356574520041724
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-47.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #10 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-47.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #10 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-47.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #11 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html
expected = 0.012782602633378081
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #11 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #11 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-20.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #12 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-29.html
expected = 0.011302700731264232
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-29.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #12 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-29.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #12 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-29.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #13 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html
expected = 0.013371438790729918
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #13 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #13 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-35.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #14 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-38.html
expected = 0.008846499047983169
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-38.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #14 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-38.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #14 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-38.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #15 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-33.html
expected = 0.011736012378240443
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-33.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #15 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-33.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #15 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-33.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #16 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-46.html
expected = 0.00900534032968973
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-46.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #16 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-46.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #16 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-46.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #17 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-10.html
expected = 0.010309017660974815
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-10.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #17 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-10.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #17 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-10.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #18 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-1.html
expected = 0.007905594863312888
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-1.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #18 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-1.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #18 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-1.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #19 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-41.html
expected = 0.010756947395543918
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-41.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #19 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-41.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #19 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-41.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #20 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-32.html
expected = 0.011733466741607019
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-32.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #20 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-32.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #20 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-32.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #21 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-2.html
expected = 0.012355739083682959
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-2.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #21 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-2.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #21 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-2.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #22 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-40.html
expected = 0.011916545805988004
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-40.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #22 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-40.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #22 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-40.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #23 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-14.html
expected = 0.011291254701698296
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-14.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #23 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-14.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #23 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-14.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #24 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-12.html
expected = 0.009469120081819478
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-12.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #24 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-12.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #24 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-12.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #25 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-4.html
expected = 0.012038453294035877
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-4.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #25 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-4.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #25 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-4.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #26 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-38.html
expected = 0.01049596025571534
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-38.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #26 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-38.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #26 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-38.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #27 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-10.html
expected = 0.006412633993100728
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-10.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #27 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-10.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #27 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-10.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #28 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-6.html
expected = 0.010209549078826331
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-6.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #28 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-6.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #28 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-6.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #29 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-22.html
expected = 0.00811717706315345
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-22.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #29 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-22.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #29 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-22.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #30 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-24.html
expected = 0.009006883257038334
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-24.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #30 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-24.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #30 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-24.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #31 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-5.html
expected = 0.010922536587749608
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-5.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #31 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-5.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #31 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-5.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #32 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-30.html
expected = 0.008271800846422634
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-30.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #32 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-30.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #32 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-30.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #33 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-18.html
expected = 0.009666097400413055
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-18.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #33 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-18.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #33 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-18.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #34 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-48.html
expected = 0.007538038677279526
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-48.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #34 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-48.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #34 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-48.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #35 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-12.html
expected = 0.009386556654339736
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-12.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #35 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-12.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #35 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-12.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #36 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html
expected = 0.013090651714295071
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #36 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #36 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-15.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #37 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-29.html
expected = 0.011579316303660131
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-29.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #37 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-29.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #37 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-29.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #38 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-23.html
expected = 0.01191978150259852
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-23.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #38 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-23.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #38 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-23.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #39 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-9.html
expected = 0.009663655808218279
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-9.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #39 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-9.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #39 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-9.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #40 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-20.html
expected = 0.01041396901898389
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-20.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #40 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-20.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #40 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-20.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #41 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html
expected = 0.012389463375719929
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #41 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #41 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-28.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #42 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-2.html
expected = 0.007815919431340641
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-2.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #42 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-2.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #42 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-2.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #43 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-36.html
expected = 0.007801502954421344
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-36.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #43 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-36.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #43 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-36.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #44 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-42.html
expected = 0.009086719123415842
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-42.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #44 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-42.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #44 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-42.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #45 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-23.html
expected = 0.009421874895440729
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-23.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #45 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-23.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #45 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-23.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #46 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-34.html
expected = 0.007845754756936617
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-34.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #46 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-34.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #46 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-34.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #47 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-16.html
expected = 0.007390720440343274
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-16.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #47 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-16.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #47 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-16.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #48 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-0.html
expected = 0.010376031762759474
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruitsB/N-0.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #48 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-0.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #48 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsB/N-0.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #49 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-9.html
expected = 0.011142026133579024
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruitsA/N-9.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #49 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-9.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #49 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruitsA/N-9.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #50 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html
expected = -1
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #50 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #50 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/tinyfruits/N.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


output.close()
success_output.close()

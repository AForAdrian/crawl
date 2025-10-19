
import testingtools
import crawler
import searchdata
import search
output = open('fruits50-page-rank-failed.txt', 'w')
success_output = open('fruits50-page-rank-passed.txt', 'w')

#Performing crawl starting at seed https://people.scs.carleton.ca/~avamckenney/fruits50/N-0.html
crawler.crawl('https://people.scs.carleton.ca/~avamckenney/fruits50/N-0.html')
#Test #0 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html
expected = 0.020879121129498537
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #0 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #0 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-33.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #1 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html
expected = 0.0169757927537423
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #1 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #1 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-6.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #2 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html
expected = 0.02309603479833191
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #2 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #2 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-16.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #3 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-4.html
expected = 0.019965557177111293
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits50/N-4.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #3 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-4.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #3 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-4.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #4 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-31.html
expected = 0.016464465936013667
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits50/N-31.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #4 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-31.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #4 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-31.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #5 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html
expected = 0.022319897048681214
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #5 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #5 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-39.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #6 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html
expected = 0.023512486890770116
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #6 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #6 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-37.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #7 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html
expected = 0.01582493067849243
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #7 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #7 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-18.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #8 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html
expected = 0.021733475880946682
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #8 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #8 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-42.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #9 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html
expected = 0.022928426413570565
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #9 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #9 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-13.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #10 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html
expected = 0.02478877289603739
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #10 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #10 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-19.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #11 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html
expected = 0.02125532473797621
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #11 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #11 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-30.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #12 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-15.html
expected = 0.01866341974192488
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits50/N-15.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #12 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-15.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #12 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-15.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #13 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-35.html
expected = 0.019699810806851036
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits50/N-35.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #13 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-35.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #13 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-35.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #14 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html
expected = 0.016031653610443078
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #14 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #14 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-2.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #15 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html
expected = 0.021020886832165405
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #15 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #15 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-44.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #16 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html
expected = 0.024517192369952933
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #16 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #16 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-1.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #17 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-0.html
expected = 0.015340370467515478
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits50/N-0.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #17 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-0.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #17 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-0.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #18 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-36.html
expected = 0.021296112692564713
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits50/N-36.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #18 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-36.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #18 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-36.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #19 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html
expected = 0.01862831362809595
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #19 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #19 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-11.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #20 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html
expected = 0.019621312459575258
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #20 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #20 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-47.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #21 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html
expected = 0.01759767856747224
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #21 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #21 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-12.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #22 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html
expected = 0.028196116466136123
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #22 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #22 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-27.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #23 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html
expected = 0.018540350263185165
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #23 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #23 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-45.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #24 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html
expected = 0.018011802902362414
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #24 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #24 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-49.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #25 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html
expected = 0.01436886259697471
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #25 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #25 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-32.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #26 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html
expected = 0.02422492536118724
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #26 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #26 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-23.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #27 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html
expected = 0.014965155749157563
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #27 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #27 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-48.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #28 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-26.html
expected = 0.01808195280176957
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits50/N-26.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #28 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-26.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #28 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-26.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #29 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html
expected = 0.01904868764048156
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #29 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #29 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-10.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #30 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-41.html
expected = 0.01969017211916767
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits50/N-41.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #30 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-41.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #30 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-41.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #31 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html
expected = 0.021687974328279274
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #31 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #31 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-17.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #32 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html
expected = 0.01873710048205946
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #32 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #32 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-28.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #33 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html
expected = 0.024976447632762886
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #33 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #33 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-24.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #34 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-29.html
expected = 0.017456501027369117
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits50/N-29.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #34 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-29.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #34 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-29.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #35 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html
expected = 0.0218509561429526
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #35 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #35 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-21.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #36 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-7.html
expected = 0.015445411901758497
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits50/N-7.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #36 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-7.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #36 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-7.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #37 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html
expected = 0.022453862071676416
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #37 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #37 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-38.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #38 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html
expected = 0.024563566260840976
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #38 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #38 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-14.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #39 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-5.html
expected = 0.020521032078930534
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits50/N-5.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #39 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-5.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #39 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-5.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #40 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html
expected = 0.01973463975614724
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #40 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #40 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-40.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #41 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html
expected = 0.02252941664731043
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #41 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #41 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-3.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #42 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-20.html
expected = 0.01750679182106982
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits50/N-20.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #42 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-20.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #42 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-20.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #43 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html
expected = 0.022437743754489158
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #43 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #43 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-25.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #44 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html
expected = 0.019192833780611134
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #44 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #44 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-22.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #45 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html
expected = 0.015873819376002803
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #45 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #45 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-8.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #46 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html
expected = 0.020666584367551567
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #46 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #46 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-43.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #47 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-9.html
expected = 0.018414962224977762
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits50/N-9.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #47 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-9.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #47 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-9.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #48 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html
expected = 0.021203702409582584
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #48 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #48 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-34.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #49 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html
expected = 0.017457590517472418
result = searchdata.get_page_rank('https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #49 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #49 checking page rank for URL https://people.scs.carleton.ca/~avamckenney/fruits50/N-46.html\n\n')
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

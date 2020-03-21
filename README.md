This is just starting out, but is supposed to serve as a python library that allows you to query OpenSecrets information regarding fundraising as well as the FEC for itemized contribution records.

Complete:
- Summary Data for a race (Center for Responsive Politics)
```
>>> from summary_data_race import *
>>> summary_data_race("GA", "07", 2020)
                  Candidate      Raised     Spent Cash on Hand Last Report
0     Carolyn Bourdeaux (D)  $1,154,686  $433,578     $863,041  12/31/2019
1        Renee Unterman (R)    $882,340  $117,150     $765,191  12/31/2019
2         Lynne Homrich (R)    $781,139  $382,388     $398,751  12/31/2019
3     Richard McCormick (R)    $665,959  $132,512     $533,286  12/31/2019
4             Lerah Lee (R)    $576,662  $502,703      $73,959  12/31/2019
5    Zahra S. Karinshak (D)    $514,942   $93,113     $421,829  12/31/2019
6         Nabilah Islam (D)    $393,192  $334,017      $59,174  12/31/2019
7        Mark Gonsalves (R)    $250,418  $124,355     $126,063  12/31/2019
8   Brenda Lopez Romero (D)    $137,913   $95,749      $42,164  12/31/2019
9            Joe Profit (R)    $124,708   $34,597     $191,582  12/31/2019
10           John Eaves (D)    $116,887   $61,479      $55,409  09/30/2019
11          Marqus Cole (D)     $60,718   $60,718           $0  09/30/2019
12     Jacqueline Tseng (R)     $17,600   $15,903       $1,697  12/31/2019
13            David Kim (D)    -$14,192    $2,795           $0  04/04/2019
>>> summary_data_race("MA", "S2", 2020)
                  Candidate      Raised       Spent Cash on Hand Last Report
0             Ed Markey (D)  $7,063,137  $4,740,022   $4,550,451  12/31/2019
1       Joe Kennedy III (D)  $3,922,598  $2,551,108   $5,544,670  12/31/2019
2  Shannon Liss-Riordan (D)  $3,234,569    $808,693   $2,425,876  12/31/2019
3       Shiva Ayyadurai (I)     $56,324     $46,391      $10,285  12/31/2019
```

- Financial Summary for a candidate (Federal Election Commission)
```
>>> from summary_data_individual import *
>>> ids = ["H0MA04192", "S0DE00175", "S4MA00028"] # Jake Auchincloss, Jessica Scarane, and Ed Markey
>>> total_spent_table(ids, 2020)
                                           H0MA04192  S0DE00175      S4MA00028
Total disbursements                       $63,618.84  $9,232.43  $4,950,669.22
Operating expenditures                    $54,768.84  $8,962.43  $4,584,998.57
Transfers to other authorized committees       $0.00      $0.00          $0.00
Total contribution refunds                 $8,850.00    $270.00    $148,587.47
Individual refunds                         $8,850.00    $270.00    $146,087.47
Political party refunds                        $0.00      $0.00          $0.00
Other committee refunds                        $0.00      $0.00      $2,500.00
Total loan repayments                          $0.00      $0.00          $0.00
Candidate loan repayments                      $0.00      $0.00          $0.00
Other loan repayments                          $0.00      $0.00          $0.00
Other disbursements                            $0.00      $0.00    $217,070.18
>>> total_reciepts_table(ids, 2020)
                                              H0MA04192   S0DE00175      S4MA00028
Total receipts                              $617,918.21  $56,203.21  $7,273,783.80
Total contributions                         $617,918.21  $56,203.21  $6,836,962.73
Total individual contributions              $615,418.21  $54,097.60  $5,761,136.80
Itemized individual contributions           $591,176.00  $29,130.20  $4,548,134.57
Unitemized individual contributions          $24,242.21  $24,967.40  $1,212,993.23
Party committee contributions                     $0.00       $0.00          $0.00
Other committee contributions                 $2,500.00       $0.00  $1,075,825.93
Candidate contributions                           $0.00   $2,105.61          $0.00
Transfers from other authorized committees        $0.00       $0.00    $309,897.74
Total loans received                              $0.00       $0.00          $0.00
Loans made by candidate                           $0.00       $0.00          $0.00
Other loans                                       $0.00       $0.00          $0.00
Offsets to operating expenditures                 $0.00       $0.00     $62,059.50
Other receipts                                    $0.00       $0.00     $64,857.83
>>> cash_summary_table(ids, 2020)
                                 H0MA04192   S0DE00175      S4MA00028
Ending cash on hand            $554,299.37  $46,970.78  $4,550,451.01
Debts/loans owed to committee        $0.00       $0.00          $0.00
Debts/loans owed by committee        $0.00       $0.00          $0.00
```
Future Work:
- Search for Candidate's ID based on name (Federal Election Commission)
- Itemized spending and contributions (Federal Election Commission)
- Congressional contribution distributions based on type of donation (Center for Responsive Politics)

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
- Retrieve the IDs for Representatives in the 115th Congress by State (Center for Responsive Politics)
```
>>> from id_query import *
>>> states = ["MA", "RI"]
>>> get_ids_for_states(states)
{'N00000153': 'Richard E Neal', 'N00000179': 'James P McGovern', 'N00029026': 'Niki Tsongas', 'N00034044': 'Joe Kennedy III', 'N00035278': 'Katherine Clark', 'N00035431': 'Seth Moulton', 'N00000267': 'Michael E Capuano', 'N00013855': 'Stephen F Lynch', 'N00031933': 'Bill Keating', 'N00033492': 'Elizabeth Warren', 'N00000270': 'Ed Markey', 'N00032019': 'David Cicilline', 'N00009724': 'Jim Langevin', 'N00027533': 'Sheldon Whitehouse', 'N00000362': 'Jack Reed'}
```
- Financial Summary for a candidate (Federal Election Commission)
```
>>> from summary_data_individual import *
>>> ids = {"H0MA04192": "Jake Auchincloss", "S0DE00175": "Jessica Scarane", "S4MA00028": "Ed Markey"}
>>> total_spent_table_candidate(ids, 2020)
                                         Jake Auchincloss Jessica Scarane      Ed Markey
Total disbursements                            $63,618.84       $9,232.43  $4,950,669.22
Operating expenditures                         $54,768.84       $8,962.43  $4,584,998.57
Transfers to other authorized committees            $0.00           $0.00          $0.00
Total contribution refunds                      $8,850.00         $270.00    $148,587.47
Individual refunds                              $8,850.00         $270.00    $146,087.47
Political party refunds                             $0.00           $0.00          $0.00
Other committee refunds                             $0.00           $0.00      $2,500.00
Total loan repayments                               $0.00           $0.00          $0.00
Candidate loan repayments                           $0.00           $0.00          $0.00
Other loan repayments                               $0.00           $0.00          $0.00
Other disbursements                                 $0.00           $0.00    $217,070.18
>>> total_reciepts_table_candidate(ids, 2020)
                                           Jake Auchincloss Jessica Scarane      Ed Markey
Total receipts                                  $617,918.21      $56,203.21  $7,273,783.80
Total contributions                             $617,918.21      $56,203.21  $6,836,962.73
Total individual contributions                  $615,418.21      $54,097.60  $5,761,136.80
Itemized individual contributions               $591,176.00      $29,130.20  $4,548,134.57
Unitemized individual contributions              $24,242.21      $24,967.40  $1,212,993.23
Party committee contributions                         $0.00           $0.00          $0.00
Other committee contributions                     $2,500.00           $0.00  $1,075,825.93
Candidate contributions                               $0.00       $2,105.61          $0.00
Transfers from other authorized committees            $0.00           $0.00    $309,897.74
Total loans received                                  $0.00           $0.00          $0.00
Loans made by candidate                               $0.00           $0.00          $0.00
Other loans                                           $0.00           $0.00          $0.00
Offsets to operating expenditures                     $0.00           $0.00     $62,059.50
Other receipts                                        $0.00           $0.00     $64,857.83
>>> cash_summary_table_candidate(ids, 2020)
                              Jake Auchincloss Jessica Scarane      Ed Markey
Ending cash on hand                $554,299.37      $46,970.78  $4,550,451.01
Debts/loans owed to committee            $0.00           $0.00          $0.00
Debts/loans owed by committee            $0.00           $0.00          $0.00
```
- Financial Summary for a PAC (Federal Election Commission)
```
>>> from summary_data_committee import *
>>> ids = {"C00503185": "Ro for Congress", "C00331769": "Barbara Lee for Congress"}
>>> total_reciepts_table_race(ids, 2020)
                                           Ro for Congress Barbara Lee for Congress
Total receipts                               $2,259,081.59              $986,918.73
Total contributions                          $2,251,636.71              $956,611.24
Total individual contributions               $2,251,636.71              $701,761.24
Itemized individual contributions            $2,073,207.95              $507,988.38
Unitemized individual contributions            $178,428.76              $193,772.86
Party committee contributions                        $0.00                    $0.00
Other committee contributions                        $0.00              $254,850.00
Candidate contributions                              $0.00                    $0.00
Transfers from other authorized committees           $0.00                    $0.00
Total loans received                                 $0.00                    $0.00
Loans made by candidate                              $0.00                    $0.00
Other loans                                          $0.00                    $0.00
Offsets to operating expenditures                $4,703.03               $30,307.49
Other receipts                                   $2,741.85                    $0.00
>>> total_spent_table_race(ids, 2020)
                                         Ro for Congress Barbara Lee for Congress
Total disbursements                        $1,373,189.46              $948,612.62
Operating expenditures                     $1,253,629.19              $742,107.26
Transfers to other authorized committees           $0.00                    $0.00
Total contribution refunds                    $37,115.75                $3,195.36
Individual refunds                            $37,115.75                $3,195.36
Political party refunds                            $0.00                    $0.00
Other committee refunds                            $0.00                    $0.00
Total loan repayments                              $0.00                    $0.00
Candidate loan repayments                          $0.00                    $0.00
Other loan repayments                              $0.00                    $0.00
Other disbursements                           $82,444.52              $203,310.00
>>> cash_summary_table_race(ids, 2020)
                              Ro for Congress Barbara Lee for Congress
Beginning cash on hand            $878,603.52              $132,303.44
Ending cash on hand             $1,764,495.65              $170,609.55
Debts/loans owed to committee           $0.00                    $0.00
Debts/loans owed by committee     $101,738.30                $4,401.75
```
- Congressional contribution distributions based on type of donation (Center for Responsive Politics)
```
>>> from contribution_distributions import *
>>> ids = {"N00038858": "Pramila Jayapal", "N00026686": "Al Green"}
>>> source_of_funds_distribution(ids, 2020)
                                        Pramila Jayapal  Al Green
Large Individual Contributions                 $913,625   $77,050
Small Individual Contributions (< $200)        $286,339   $15,451
PAC Contributions                              $187,000  $114,000
Other                                            $8,934     -$165
Candidate self-financing                           $200        $0
```
- Congressional contribution distributions based on PAC breakdown (Center for Responsive Politics)
```
>>> from contribution_distributions import *
>>> ids = {"N00038858": "Pramila Jayapal", "N00026686": "Al Green"}
>>> pac_contribution_distribution(ids, 2020)
            Pramila Jayapal Al Green
Labor              $136,800  $84,500
Business            $29,250  $46,300
Ideological         $27,500   $1,000
```
Future Work:
- Search for Candidate's ID (Center for Responsive Politics)
- Itemized spending and contributions (Federal Election Commission)

import output
import get

# get the start Monday date(DONT modify start_date)
start_date=str(get.date_from_user())
period_length=int(get.period_length_from_user())

# use iterations to collect data from Mon. to given period length
date=start_date
period_data_list=[] # this used to store from day 1 to day n data in a list format
output.color_output("cyan", "\n==============$$$$===============", True)
for i in range(period_length): # THE 5 CAN CHANGED TO ANY LENGTH OF DAYS AS WE WANT
    # XXXX_stats can allow XXXX_prune function recognize if the data is needed to prune or not
    twse_stats=get.twse(date, "ALL", "ALL_TSE")
    get.twse_prune(date, twse_stats)
    tpex_stats=get.tpex(date, "AL", "ALL_OTC")
    get.tpex_prune(date, tpex_stats)
    period_data_list.append(get.merge_same_day_data(date)) # append the single-day-data-list to period_data_list
    date=str(get.date_with_given_delta(date, 1)) # add 1 day, continue collect next date stock data

# find weekly data of TWSE and TPEX from the period_data_list(each components in it means a single-day all stocks data)
print("\n")
output.color_output("purple", "獲取所有股票代號", False)
stockid_list=get.stockid_list(period_data_list)
output.color_output("green", "[完成]", True)
output.color_output("purple", "總和各日資料", False)
collect_result=get.combine_daily_data(period_data_list, stockid_list, start_date)
output.color_output("green", "[完成]", True)
print("\n")

# final show reminder and some info
output.color_output("purple", "所有股票支數:", False)
output.color_output("green", str(len(stockid_list)), True)
output.color_output("cyan", "==============$$$$===============", True)

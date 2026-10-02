"""
TASK: 04 Temp Stats Csv

# Skills CSV read, simple maths
Go to this site https://www.metoffice.gov.uk/hadobs/hadcet/data/download.html and download the txt file
Daily Mean Temperature.
This file has dates and daily temperatures:
- Read all of the values
- Find the highest, lowest and average
- Print those three values
Extend - See how you can potentially use the dates to chart daily temp changes by years, by months
by day comparisons over time. Maybe chart them using mathplotlib or another library. Just see what you can do with it

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def main():
    count=0
    high_temp=-10000000000000
    low_temp=10000000000000
    total=0
    for_count=0

    file=open("meantemp_daily_totals.txt","r")
    next(file)

    for line in file:
        for_count+=1
        data=line.split()
        if len(data) < 2:
            continue
        date=data[0]
        temp=data[1]
        try:
            temp=float(temp)
        except ValueError:
            continue
        total+=temp
        if temp > high_temp:
            high_temp=temp
            high_date=date
        elif temp < low_temp:
            low_temp=temp
            low_date=date
        else:
            pass

    average = total / for_count

    low_date=str(low_date)
    low_temp=str(low_temp)
    high_temp=str(high_temp)
    high_date=str(high_date)
    average=str(average)

    print("The lowest temperature was",low_temp+". Date:",low_date+".")
    print("The highest temperature was",high_temp+". Date:",high_date+".")
    print("The average temperature was",average+".")

    pass


if __name__ == "__main__":
    main()

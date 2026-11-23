"""Task 12: effective-date rules and service-period aggregation demonstration."""
from datetime import date
SCHEMES=[{'name':'old','from':date(2000,1,1),'to':date(2020,12,31),'minimum_years':10},{'name':'revised','from':date(2021,1,1),'to':None,'minimum_years':8}]
def scheme_on(d):
 for s in SCHEMES:
  if d>=s['from'] and (s['to'] is None or d<=s['to']):return s
 return None
def qualifying_years(periods,excluded_breaks=()):
 days=sum((end-start).days for start,end in periods)-sum((end-start).days for start,end in excluded_breaks)
 return max(0,days)/365.25
def check_eligibility(retirement_date,periods,excluded_breaks=()):
 s=scheme_on(retirement_date)
 if not s:return {'status':'UNKNOWN','reason':'No scheme for date'}
 years=qualifying_years(periods,excluded_breaks)
 return {'status':'TRUE' if years>=s['minimum_years'] else 'FALSE','scheme':s['name'],'qualifying_years':round(years,2),'threshold':s['minimum_years']}

if __name__ == "__main__":
    from datetime import date
    print("TASK 12 - TEMPORAL PENSION RULES")
    periods = [(date(2000, 1, 1), date(2019, 1, 1))]
    breaks = [(date(2005, 1, 1), date(2006, 1, 1))]
    for retirement in [date(2019, 6, 1), date(2022, 6, 1)]:
        print("\nRetirement date:", retirement)
        print("Eligibility result:", check_eligibility(retirement, periods, breaks))
    print("Task 12 demo completed.")

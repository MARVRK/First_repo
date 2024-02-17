import sys
from collections import defaultdict

def parse_log_line(line: str) -> dict:
    date,time,level,*message=line.split(" ")
    return{'date':date,'time':time,'level':level,'message':" ".join(message)}

def load_logs(file_path: str) -> list:
    with open(file_path, "r+") as logfile:
        lines=list(map(parse_log_line,logfile.readlines()))
    return lines

def filter_logs_by_level(logs: list, level: str) -> list:
     return list(filter(lambda x: x['level']==level,logs))

def count_logs_by_level(logs: list) -> dict:
    calc=defaultdict()
    calc.default_factory=int
    for log in logs:
        if log['level'] not in calc:
            calc[log['level']]+=1
    return print(calc)

     
    
def display_log_counts(counts: dict):
    pass

if __name__== "__main__":
    filename=sys.argv[0]
    logs=load_logs(file_path=filename)
    if len(sys.argv)==3:
        level=sys.argv[2]
        logs=filter_logs_by_level(logs,level)
    
       


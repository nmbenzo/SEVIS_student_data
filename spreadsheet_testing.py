advisor_major = {
    'Cynthia':['MSDS','MSHI','MBA','MSFN'],
    'Nina':['BENI','BNTL','BMKT','BFIN','BMGT'],
    'Nathan':['CS','COMS','CHEM','POLS','HIST','BIO',],
    'Marcella':['IDEC','MSCS','CSBR','ECON','MSCHEM',]
     }


def find_major():
    major = [[i for i in advisor_major[x]] for x in advisor_major.keys()]
    return(major)

def find_advisor(advisor_major):
  for k, v in advisor_major.items():
    if isinstance(v, dict):
      find_advisor(v)
    else:
      print("{0} : {1}".format(k, v))

print(find_advisor(advisor_major))


major = advisor_major.values()


def _findadvisor(data, search_for):
    for k in data:
        for v in data[k]:
            if search_for in v:
                return k
    return None

print(_findadvisor(advisor_major, 'BIO'))




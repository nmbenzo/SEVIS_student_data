from dicttoxml import dicttoxml
from xml.dom.minidom import parseString


advisor_major_ug = {
    'BACT-Accounting': 'Nina',
    'BADM-Business Administration': 'Nina',
    'BENI-Entrepreneurship & Innovation': 'Nina',
    'BMGT-Management': 'Nina',
    'BNTL-International Business': 'Nina',
    'BMKT-Marketing': 'Nina',
    'BFIN-Finance': 'Nina',
    'HM-Hospitality Management': 'Nina',
    'CS-Computer Science': 'Nathan',
    'COMS-Communication Studies': 'Nathan',
    'CHEM-Chemistry': 'Nathan',
    'POLS-Politics': 'Nathan',
    'HIST-History': 'Nathan',
    'BIO-Biology': 'Nathan',
    'BAIS-International Studies': 'Nathan',
    'UNLA-Undeclared Arts': 'Nathan',
    'UNSC-Undeclared Sciences': 'Nathan',
    'ADVT-Advertising': 'Nathan',
    'LAW-Law': 'Nathan',
    'PSYC-Psychology': 'Nathan',
    'ECON-Economics': 'Nathan',
    'ARCD-Architecture & Community Desig': 'Nathan',
    'BSDS-Data Science':'Nathan',
    'ENVS-Environmental Science':'Nathan',
    'CMPL-Comparative Lit. & Culture': 'Nathan',
    'ICL-Intl Transaction & Comp. Law':'Nathan',
    'IPTL-Intellectual Property Tech Law': 'Nathan',
    'MATH-Mathematics': 'Nathan',
    'MS-Media Studies': 'Nathan',
    'PASJ-Perf. Arts & Soc. Justice': 'Nathan',
    'SOC-Sociology': 'Nathan',
    'DSGN-Design': 'Nathan',
    'KIN-Kinesiology': 'Nathan',
    'JNST-Japanese Studies': 'Nathan',
    'ANST-Asian Studies': 'Nathan',
    'BIOL-Biology':'Nathan'
     }

advisor_major_gr = {
    'IDEC-Intl & Development Economics': 'Marcella',
    'CSBR-Computer Science Bridge': 'Marcella',
    'ENVS-Environmental Science': 'Marcella',
    'ECON-Economics': 'Marcella',
    'CHEM-Chemistry': 'Marcella',
    'ENGY-Energy Systems Management': 'Marcella',
    'MAIS-International Studies': 'Marcella',
    'MAPC-Professional Communication': 'Marcella',
    'CPSY-Counseling Psychology': 'Marcella',
    'CAPS-Asia Pacific Graduate Studies': 'Marcella',
    'APS-Asia Pacific Studies': 'Marcella',
    'BTEC-Biotechnology': 'Marcella',
    'CSBR-Computer Science': 'Marcella',
    'PA-Public Affairs': 'Marcella',
    'PSYD-Psychology': 'Marcella',
    'SM-Sport Management': 'Macella',
    'SM-Sports Management': 'Marcella',
    'UPA-Urban and Public Affairs':'Marcella',
    'IME-Intl and Multicultural Educ.': 'Cynthia',
    'MBA-Business Administration': 'Cynthia',
    'MNAF-Nonprofit Administration': 'Cynthia',
    'MSHI-Health Informatics': 'Cynthia',
    'MSBH-Behavorial Health': 'Cynthia',
    'MSEI-Entrepreneurship Innovation': 'Cynthia',
    'MSFN-Financial Analysis': 'Cynthia',
    'EDUC-Education': 'Cynthia',
    'L&I-Learning and Instruction': 'Cynthia',
    'MPH-Public Health': 'Cynthia',
    'O&L-Organization and Leadership':'Cynthia',
    'TSOL-Teach Engl/Speakers Other Lang': 'Cynthia'
}

master_deg_adv = {
    'Master of Arts':'Marcella',
    "'Professional Science Master's":'Marcella',
    'Master of Science':'Marcella',
    'Master of Public Health':'Cynthia',
    'Doctor of Education':'Cynthia',
    'Master of Science in Nursing':'Cynthia',
    'Master of Public Affairs':'Cynthia',
    'Master in Global Entrprnr/Mgt':'Cynthia',
    'Master of Business Admin': 'Cynthia'
}


bachelor_deg_adv = {
    'BS in Business Administration': 'Nina',
    'Bachelor of Arts': 'Nathan',
    'Bachelor of Science': 'Nathan',
    'Master of Laws': 'Nathan',
    'Juris Doctor': 'Nathan',
    'Bachelor of Science in Nursing': 'Nathan'
}


GR_major_xml = dicttoxml(advisor_major_gr, custom_root='root', attr_type=False)
UG_major_xml = dicttoxml(advisor_major_ug, custom_root='root', attr_type=False)
GR_level_xml = dicttoxml(master_deg_adv, custom_root='root', attr_type=False)
UG_level_xml = dicttoxml(bachelor_deg_adv, custom_root='test', attr_type=False)

dom = parseString(UG_major_xml)
print(dom.toprettyxml())

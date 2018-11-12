from dicttoxml import dicttoxml
from xml.dom.minidom import parseString


advisor_major_ug = {
    'Nina': {'BACT-Accounting',
    'BADM-Business Administration',
    'BENI-Entrepreneurship & Innovation',
    'BMGT-Management',
    'BNTL-International Business',
    'BMKT-Marketing',
    'BFIN-Finance',
    'HM-Hospitality Management'},
    'Nathan': {'CS-Computer Science',
    'COMS-Communication Studies',
    'CHEM-Chemistry',
    'POLS-Politics',
    'HIST-History',
    'BIO-Biology',
    'BAIS-International Studies',
    'UNLA-Undeclared Arts',
    'UNSC-Undeclared Sciences',
    'ADVT-Advertising',
    'LAW-Law',
    'PSYC-Psychology',
    'ECON-Economics',
    'ARCD-Architecture & Community Desig',
    'BSDS-Data Science',
    'ENVS-Environmental Science',
    'CMPL-Comparative Lit. & Culture',
    'ICL-Intl Transaction & Comp. Law',
    'IPTL-Intellectual Property Tech Law',
    'MATH-Mathematics',
    'MS-Media Studies',
    'PASJ-Perf. Arts & Soc. Justice',
    'SOC-Sociology',
    'DSGN-Design',
    'KIN-Kinesiology',
    'JNST-Japanese Studies',
    'ANST-Asian Studies',
    'BIOL-Biology'}

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


GR_major_xml = dicttoxml(advisor_major_gr, custom_root='root', ids=False)
UG_major_xml = dicttoxml(advisor_major_ug, custom_root='root', attr_type=False)
GR_level_xml = dicttoxml(master_deg_adv, custom_root='root', attr_type=False)
UG_level_xml = dicttoxml(bachelor_deg_adv, custom_root='test', attr_type=False)

dom = parseString(UG_major_xml)
print(dom.toprettyxml())

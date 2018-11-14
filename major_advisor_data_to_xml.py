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
    'Marcella':{'IDEC-Intl & Development Economics',
    'CSBR-Computer Science Bridge'
    'ENVS-Environmental Science'
    'ECON-Economics'
    'CHEM-Chemistry'
    'ENGY-Energy Systems Management',
    'MAIS-International Studies',
    'MAPC-Professional Communication',
    'CPSY-Counseling Psychology',
    'CAPS-Asia Pacific Graduate Studies',
    'APS-Asia Pacific Studies',
    'BTEC-Biotechnology',
    'CSBR-Computer Science',
    'PA-Public Affairs',
    'PSYD-Psychology',
    'SM-Sport Management',
    'UPA-Urban and Public Affairs'},

    'Cynthia': {'IME-Intl and Multicultural Educ.',
    'MBA-Business Administration',
    'MNAF-Nonprofit Administration',
    'MSHI-Health Informatics:',
    'MSBH-Behavorial Health',
    'MSEI-Entrepreneurship Innovation',
    'MSFN-Financial Analysis',
    'EDUC-Education',
    'L&I-Learning and Instruction',
    'MPH-Public Health',
    'O&L-Organization and Leadership',
    'TSOL-Teach Engl/Speakers Other Lang'}
    }

master_deg_adv = {
    'Marcella':{'Master of Arts',
    "'Professional Science Master's",
    'Master of Science'},

    'Cynthia':{
    'Master of Public Health',
    'Doctor of Education',
    'Master of Science in Nursing',
    'Master of Public Affairs',
    'Master in Global Entrprnr/Mgt',
    'Master of Business Admin'}
    }


bachelor_deg_adv = {
    'Nina':{'BS in Business Administration'},

    'Nathan': {
    'Bachelor of Arts',
    'Bachelor of Science',
    'Master of Laws',
    'Juris Doctor',
    'Bachelor of Science in Nursing'}
    }


GR_major_xml = dicttoxml(advisor_major_gr, custom_root='root', attr_type=False)
UG_major_xml = dicttoxml(advisor_major_ug, custom_root='root', attr_type=False)
GR_level_xml = dicttoxml(master_deg_adv, custom_root='root', attr_type=False)
UG_level_xml = dicttoxml(bachelor_deg_adv, custom_root='root', attr_type=False)

domUG = parseString(UG_major_xml)
domGR = parseString(GR_major_xml)
domLevUG = parseString(UG_level_xml)
domLevGR = parseString(GR_level_xml)

print(domUG.toprettyxml())
print(domGR.toprettyxml())
print(domLevUG.toprettyxml())
print(domLevGR.toprettyxml())


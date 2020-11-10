""" Email Files """

i_901_fee = '/Users/natebenzschawel/Downloads/SEVIS_Reg/Emails/I_901_fee_email.txt'

bad_phone = '/Users/natebenzschawel/Downloads/SEVIS_Reg/Emails/Bad_phone.txt'

bad_perm_addy = '/Users/natebenzschawel/Downloads/SEVIS_Reg/Emails/Local_Addy_as_Perm.txt'

sv_incomplete = '/Users/natebenzschawel/Downloads/SEVIS_Reg/Emails/SV_Incomplete.txt'

loa_term = '/Users/natebenzschawel/Downloads/SEVIS_Reg/Emails/loa_term.txt'

with open(i_901_fee, 'r') as file_901:
    data_901 = file_901.read()

with open(bad_phone, 'r') as phone:
    data_bad_phone = phone.read()

with open(bad_perm_addy, 'r') as perm_addy:
    data_bad_addy = perm_addy.read()

with open(sv_incomplete, 'r') as sv:
    data_sv = sv.read()

with open(loa_term, 'r') as sv:
    loa_term = sv.read()

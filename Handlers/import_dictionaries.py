try:
    from Handlers.major_advisor_data import master_deg_adv, bachelor_deg_adv

    from Active_Students_Requiring_Registration.build_data import \
    active_campusID_SEVISID, active_SEVISID_major, active_SEVISID_units, \
    sevisID_emails, SEVISID_term

    from Handlers.major_advisor_data import ug_final_df, gr_final_df

    from Student_Cancellations.build_cancel_data import \
    Cancel_SEVISID_banner, Cancel_SEVISID_credits, Cancel_SEVISID_SV

    from Handlers.major_advisor_data \
    import advisor_major_ug, advisor_major_gr,\
    gr_major_advisor_df, ug_major_advisor_df, ug_final_df, gr_final_df
except:
    print('Files no longer available')
    pass
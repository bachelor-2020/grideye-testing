# OLD INDEX STATES 1
print("creating pickle...")
print("this will take some time...")
# Variable initialisation
walk_in = 1
walk_out = -1
stay = 0

left   = 1
middle = 3
right  = 5

#keep track of last non-stay state and the index/time respectively
left_state_out= 0; middle_state_out= 0; right_state_out=0
left_state_in = 0; middle_state_in = 0; right_state_in =0


states_left_in = [];       states_middle_in = [];       states_right_in = []
states_left_out = [];      states_middle_out = [];      states_right_out = []
states_left_in_time = [];  states_middle_in_time = [];  states_right_in_time = []
states_left_out_time = []; states_middle_out_time = []; states_right_out_time = []

for t in tnrange(len(df_temp_diff_red)):

    #test left
    if df_temp_diff_red.iloc[t,left] == stay:
        pass
    elif df_temp_diff_red.iloc[t,left] == walk_out:
        left_state_out = t
        states_left_in.append(left_state_in)
        states_left_out.append(left_state_out)

        states_left_in_time.append(df_temp_diff_red.iloc[t,left-1])
        states_left_out_time.append(df_temp_diff_red.iloc[t,left-1])

    elif df_temp_diff_red.iloc[t,left] == walk_in:
        left_state_in = t


# OLD INDEX STAES 2
# Check all that all who entered also left
# assert df_temp_diff_red.iloc[:,0].sum() == False # <-- FAILS
# assert df_temp_diff_red.iloc[:,1].sum() == False # <-- FAILS
assert df_temp_diff_red.iloc[:,2].sum() == False

picklename = 'index_states'+str(threshold)[0:2]+'_'+str(threshold)[3]+'.p'

if os.path.isfile(picklename):
    print("loading pickles")
    index_states = pd.read_pickle(picklename)
else:
    print("creating pickle...")
    print("this will take some time...")
    # Variable initialisation
    walk_in = 1
    walk_out = -1
    stay = 0

    left   = 1
    middle = 3
    right  = 5

    #keep track of last non-stay state and the index/time respectively
    left_state_out= 0; middle_state_out= 0; right_state_out=0
    left_state_in = 0; middle_state_in = 0; right_state_in =0


    states_left_in = [];       states_middle_in = [];       states_right_in = []
    states_left_out = [];      states_middle_out = [];      states_right_out = []
    states_left_in_time = [];  states_middle_in_time = [];  states_right_in_time = []
    states_left_out_time = []; states_middle_out_time = []; states_right_out_time = []

    for t in tnrange(len(df_temp_diff_red)):

        #test left
        if df_temp_diff_red.iloc[t,left] == stay:
            pass
        elif df_temp_diff_red.iloc[t,left] == walk_out:
            left_state_out = t
            states_left_in.append(left_state_in)
            states_left_out.append(left_state_out)

            states_left_in_time.append(df_temp_diff_red.iloc[t,left-1])
            states_left_out_time.append(df_temp_diff_red.iloc[t,left-1])

        elif df_temp_diff_red.iloc[t,left] == walk_in:
            left_state_in = t


        #test middle
        if df_temp_diff_red.iloc[t,middle] == stay:
            pass
        elif df_temp_diff_red.iloc[t,middle] == walk_out:
            middle_state_out = t
            states_middle_in.append(middle_state_in)
            states_middle_out.append(middle_state_out)

            states_middle_in_time.append(df_temp_diff_red.iloc[t,middle-1])
            states_middle_out_time.append(df_temp_diff_red.iloc[t,middle-1])

        elif df_temp_diff_red.iloc[t,middle] == walk_in:
            middle_state_in = t


        #test right
        if df_temp_diff_red.iloc[t,right] == stay:
            pass
        elif df_temp_diff_red.iloc[t,right] == walk_out:
            right_state_out = t
            states_right_in.append(right_state_in)
            states_right_out.append(right_state_out)

            states_right_in_time.append(df_temp_diff_red.iloc[t,right-1])
            states_right_out_time.append(df_temp_diff_red.iloc[t,right-1])

        elif df_temp_diff_red.iloc[t,right] == walk_in:
            right_state_in = t

    print("creating Dataframes")
    print("Left")
    states_left_in_df   = pd.DataFrame({'left_in': states_left_in})
    states_left_out_df   = pd.DataFrame({'left_out': states_left_out})
    states_left_in_time_df   = pd.DataFrame({'left_in_time': states_left_in_time})
    states_left_out_time_df   = pd.DataFrame({'left_out_time': states_left_out_time})

    print("Middle")
    states_middle_in_df = pd.DataFrame({'middle_state_in': states_middle_in})
    states_middle_out_df = pd.DataFrame({'middle_state_out': states_middle_out})
    states_middle_in_time_df   = pd.DataFrame({'middle_in_time': states_middle_in_time})
    states_middle_out_time_df   = pd.DataFrame({'middle_out_time': states_middle_out_time})

    print("Right")
    states_right_in_df  = pd.DataFrame({'right_state_in': states_right_in})
    states_right_out_df  = pd.DataFrame({'right_state_out': states_right_out})
    states_right_in_time_df   = pd.DataFrame({'right_in_time': states_right_in_time})
    states_right_out_time_df   = pd.DataFrame({'right_out_time': states_right_out_time})


    index_states = pd.concat([states_left_in_df,states_left_out_df,states_middle_in_df,states_middle_out_df,states_right_in_df,states_right_out_df,
                             states_left_in_time_df, states_left_out_time_df, states_middle_in_time_df, states_middle_out_time_df,
                              states_right_in_time_df, states_right_out_time_df], ignore_index=True, axis=1)

    index_states.columns = ['left_in','left_out','middle_in','middle_out','right_in','right_out',
                            'left_in_time','left_out_time','middle_in_time','middle_out_time','right_in_time','right_out_time']

    print("Pickling")
    index_states.to_pickle(picklename)

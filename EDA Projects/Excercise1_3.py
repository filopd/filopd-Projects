import survey
table = survey.Pregnancies()
table.ReadRecords()
print('Number of pregnancies', len(table.records))
count_LiveBirths = 0
count_FirstBaby = 0
avg_preglength_FirstBaby = 0
avg_preglength_OthThanFirstBaby = 0
for eatch_rec in table.records:
    # outcome 1 indicates the live birth.
    # birthord is blank if outcome is not live birth i.e. not 1.
    # birthord is 1 for first baby.
    if eatch_rec.outcome == 1:
        # Add a counter to which will increment by 1 whenever pregnancy outcome is 1.
        count_LiveBirths += 1
        # To partition live births into two groups, one for first babies and second for others.
        if eatch_rec.birthord == 1:
            count_FirstBaby += 1
            # Get the total length of pregnancies in weeks.
            avg_preglength_FirstBaby += eatch_rec.prglength
        else:
            # Get the total length of pregnancies in weeks.
            avg_preglength_OthThanFirstBaby += eatch_rec.prglength
# Divide the total by count to ge the average.
avg_preglength_FirstBaby = (avg_preglength_FirstBaby/count_FirstBaby)
avg_preglength_OthThanFirstBaby = (avg_preglength_OthThanFirstBaby/(count_LiveBirths-count_FirstBaby))

print("Count of Live Births is:", str(count_LiveBirths))
print("Count of First Baby is:", str(count_FirstBaby))
print("Count of other than First Baby is:", str(count_LiveBirths - count_FirstBaby))
print("Average of Pregnancy length of all First Babies in weeks is:", str(avg_preglength_FirstBaby))
print("Average of Pregnancy length of all other than First Baby in weeks is:", str(avg_preglength_OthThanFirstBaby))

a = avg_preglength_FirstBaby - avg_preglength_OthThanFirstBaby
a = a * 7
a = a * 24
a = int(a)
print("Difference between Avg of Pregnancy length of First Babies and all other than First Babies in weeks is:", str(a))

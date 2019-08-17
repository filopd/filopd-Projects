import survey
table = survey.Pregnancies()
table.ReadRecords()
'''
Let's see whether the first baby is boy or girl ? How many counts ?
https://www.icpsr.umich.edu/nsfg6/Controller?displayPage=labelDetails&fileCode=PREG&section=&subSec=8014&srtLabel=611801
1 - Male
2 - Female
'''

count_Boy = 0
count_Girl = 0
for eatch_rec in table.records:
    # outcome 1 indicates the live birth.
    # birthord is blank if outcome is not live birth i.e. not 1.
    # birthord is 1 for first baby.
    if (eatch_rec.outcome == 1) & (eatch_rec.birthord == 1):
        # Add a counter to which will increment by 1.
        if eatch_rec.babysex == 1:
            count_Boy += 1
        elif eatch_rec.babysex == 2:
            count_Girl += 1
print("Count of First Baby Boy is", str(count_Boy), "and Baby Girl is", str(count_Girl))

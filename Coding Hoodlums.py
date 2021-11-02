print("Mensuration Health")
question1 = "What problem u are facing during your periods?"
options1 = "a. Cramps\nb. irregularity\nc. heavy flow\nd. none of these\n"
print(question1)
print(options1)

while True:
    response = input("Hit 'a', 'b', 'c' or 'd' for your answer\n")

    if response == "d":
        print("Congrats you have  no issues regarding  periods")
        break
    if response == "b":
        print("SYMPTOMS:\n.1 menstruation  cycle is longer than 35 days\n2. changes in blood flow\n")
        print("POSSIBLE CAUSES:\n1. hormonal imbalance\n2. PCOS(polycystic overy syndrome)\n3. stress\n4. pregnancy\n5. perimenopause\n6. thyroid problems\n7. extreme weight loss and eating disorders\n")
        print("TREATMENT:\n Treatment depends on what’s causing your irregular periods and thus you should consult your doctor without any delays.Here are some methods\nwhich will help you in reducing stress and hence curing your irregular periods:\n1. yoga\n2. meditation\n3. deep breathing\n4.healthful diet\n")
        break
    if response == "c":
        print("SYMPTOMS:\n1. Soaking through one or more sanitary pads or tampons every hour for several consecutive hours\n2. Needing to use double sanitary protection to control your menstrual flow\n3. Needing to wake up to change sanitary protection during the night\n4. Bleeding for longer than a week\n5. Passing blood clots larger than a quarter\n6. Restricting daily activities due to heavy menstrual flow\n7. Symptoms of anemia, such as tiredness, fatigue or shortness of breath\n")
        print("POSSIBLE CAUSES:\n1. Hormone imbalance\n2. Dysfunction of the ovaries\n3. Pregnancy complications\n4. Cancer\n5. Medications\n")
        print("TREATMENT:\n1.place heat pad on belly area\n2.take iron pills\n3. consult your gynecologist if not relief\n")
        break
    if response == "a":
        print("SYMPTOMS:\n1. Nausea\n2. Vomiting\n3. Diarrhea\n4. Lightheadedness\n5. Severe headache\n6. Fatigue\n7. Presence of clots in the menstrual blood\n8. Constipation\n9. Bloating in the belly area\n10. Bouts of fainting\n11. Tender breasts\n")
        print("POSSIBLE CAUSES:\n1. Lack of exercise\n2. Psychological or social stress\n3. Excessive smoking\n4. Women who have never been pregnant\n5. Consuming excessive alcohol\n6. Obesity\n")
        print("TREATMENT:\n1. Placing a heating pad across the belly or lower back\n2. Taking a hot bath or shower\n3. Yoga\n4. Conscious dietary changes such as reducing caffeine & sugar intake and increasing protein intake\n5. Acupuncture\n6. Doing mild but regular exercises in the form of walking or cycling\n7. Taking plenty of bed rest as the period approaches or on the first day of the period\n")
        break
    
        

while True:
    bonus = input("I hope we helped you a little.\nHit 'y' for yes and 'n' for no.\n")

    if bonus == "y":
        print(" WE ARE HAPPY TO HEAR THAT\n. Thanks for your response :)")
        
            
        break
    elif bonus == "n":
        print("SORRY :( It is out of our knowledge please consult your gynecologist")
        break
    else:
        print("INVALID INPUT!!! Only hit 'y' or 'n' for your response")



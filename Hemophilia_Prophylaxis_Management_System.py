
def get_data(week_counter, contestant_number, coach_scoring_order_number, audience_scoring_order_number,overall_points):
    global weekly_points
    global week_champions
    global global_counter
    global coach_scores_per_contestant

    print(f"Week {week_counter}")
    print("------")
    
    contestant_point_by_coach=[0]*contestant_number
    contestant_point_by_audience=[0]*contestant_number
    if global_counter==0: 
        week_champions=[0]*contestant_number
        coach_scores_per_contestant = [[0] * contestant_number for contestant_counter in range(contestant_number)]
        
        global_counter=+1
        
    selected_numbers=[]
    selected_numbers.clear()
    # Koç puanlama
    for coach_count in range(contestant_number):
        selected_numbers.clear()
        for coach_scoring_order in range(coach_scoring_order_number):
            keep_asking=True
            while keep_asking==True:
                try:    
                    contestant_num_by_coach=int(input(f"Coach {coach_count+1} Enter the number of the competitor you will give {coach_scoring_order+1} point to :"))       
                    while contestant_num_by_coach<=0 or contestant_num_by_coach>contestant_number or contestant_num_by_coach in selected_numbers or coach_count+1==contestant_num_by_coach :
                        print("Invalid Data Entry!")
                        if contestant_num_by_coach<=0 or contestant_num_by_coach>contestant_number:
                            print("Contestant can not be found!")
                        if contestant_num_by_coach in selected_numbers:
                            print("You can not give point to the same contestant!")
                        if coach_count+1==contestant_num_by_coach:
                            print("You can not give point to your own contestant!")
                        contestant_num_by_coach=int(input(f"Coach {coach_count+1} Enter the number of the competitor you will give {coach_scoring_order+1} point to :"))
                except(ValueError,TypeError):
                    print("Invalid Entry,Please enter an integer!")
                else:
                    keep_asking=False       
            coach_scores_per_contestant[coach_count][contestant_num_by_coach-1]+=(coach_scoring_order+1)
            selected_numbers.append(contestant_num_by_coach)
            contestant_point_by_coach[contestant_num_by_coach-1]+=(coach_scoring_order+1)

    selected_numbers.clear()
    for audience_scoring_order in range(audience_scoring_order_number):
        keep_asking=True
        while keep_asking==True:
            try:
                contestant_num_by_audience=int(input(f"Auidience choose the contestant you will give {audience_scoring_order+1} point to :"))
                while contestant_num_by_audience<=0 or contestant_num_by_audience>contestant_number or contestant_num_by_audience in selected_numbers : 
                    print("Invalid Data Entry!")
                    if contestant_num_by_audience<=0 or contestant_num_by_audience>contestant_number:
                        print("Contestant can not be found!")
                    if contestant_num_by_audience in selected_numbers:
                        print("You can not give point to the same contestant!")
                    contestant_num_by_audience=int(input(f"Auidience choose the contestant you will give {audience_scoring_order+1} point to :"))
                selected_numbers.append(contestant_num_by_audience)
                contestant_point_by_audience[contestant_num_by_audience-1]+=((audience_scoring_order+1)*(contestant_number-1))
            except(ValueError,TypeError):
                    print("Invalid Entry,Please enter an integer!")
            else:
                keep_asking=False 
    total_points = [x + y for x, y in zip(contestant_point_by_coach, contestant_point_by_audience)]

    all_data_for_week=[]
        
    for x in range(len(contestant_point_by_coach)):
        collective_list= [x+1,contestant_point_by_coach[x],contestant_point_by_audience[x],total_points[x]]
        all_data_for_week.append(collective_list)
    weekly_points.append(total_points)

    
    # Haftalık sıralama
    sorted_all_data_for_week = sorted(all_data_for_week, key=lambda x: (x[3], x[1], -x[0]), reverse=True) 
    if sorted_all_data_for_week[0][3]== sorted_all_data_for_week[1][3]:
        pass
    else:
        week_champions[(sorted_all_data_for_week[0][0])-1] +=1


    print(f"Scoring results for week-{week_counter}")
    print(f"{'Rank':6}{'Contestant No':15}{'Coach Score':15}{'Audience Score':15}{'Total Score':10}")
    print("----------------------------------------------------------------------")

    
    
    rank_counter2=0
    for point in sorted_all_data_for_week:
        rank_counter2+=1
        
        print(f"{rank_counter2:<6}{point[0]:<15}{point[1]:<15}{point[2]:<15}{point[3]:<15}")
        

    
    if week_counter == 1:
            overall_points[:]= all_data_for_week
    else:
        for i in range(len(overall_points)):
            overall_points[i][1:] = [x + y for x, y in zip(overall_points[i][1:], all_data_for_week[i][1:])]

    sorted_overall_data = sorted(overall_points, key=lambda x: (x[3], x[1], -x[0]), reverse=True)  
    # Genel sıralama
    print(f"OVERALL STANDINGS AT THE END OF THE WEEK-{week_counter} :")
    print(f"{'Rank':6}{'Contestant No':15}{'Coach Score':15}{'Audience Score':15}{'Total Score':10}")
    print("--------------------------------------------------------------------------------")

    rank_counter=0
    for point in sorted_overall_data:
        rank_counter+=1
        
        print(f"{rank_counter:<6}{point[0]:<15}{point[1]:<15}{point[2]:<15}{point[3]:<15}")
    

       
        
        
        
            




def starting():
    
            global contestant_number
            global competition_weeks
            keep_asking=True
            while keep_asking==True:
                try:
                    contestant_number=int(input("Enter the number of contestants (at least 5):"))
                    while contestant_number<5:
                        print("Invalid Data Entry!")
                        contestant_number=int(input("Enter the number of contestants (at least 5):"))
                except  (ValueError,TypeError):
                    print("Invalid Entry,Please enter an integer!")
                else:
                    keep_asking=False    
            keep_asking=True  
            while keep_asking==True:
                try:    
                    competition_weeks=int(input("Enter the number of weeks the competition will continue (at least 3):"))
                    while competition_weeks<3:
                        print("Invalid Data Entry!")
                        competition_weeks=int(input("Enter the number of weeks the competition will continue (at least 3):"))
                except  (ValueError,TypeError):
                    print("Invalid Entry,Please enter an integer!")
                else:
                    keep_asking=False  
    
   

cont='y'

while cont in['y','Y'] :    
    
    starting()
    
    
    coach_scoring_order_number=3
    audience_scoring_order_number=3
    overall_points=[]
    coach_scores_per_contestant=[]
    weekly_points=[]
    week_champions=[]
    global_counter = 0
    week_counter=0
    for week in range(competition_weeks):
        week_counter+=1
        
        get_data(week_counter, contestant_number, coach_scoring_order_number, audience_scoring_order_number,overall_points)
    print(f"Overall standings based on the coaches' scores only: :")
    print(f"{'Rank':6}{'Contestant No':15}{'Score':15}")
    print("------------------------------")
    rank_counter4=0
    sorted_overall_data = sorted(overall_points, key=lambda x: (x[1], -x[0]), reverse=True)
    for i in (sorted_overall_data):
        rank_counter4+=1
        print(f"{rank_counter4:<6}{i[0]:<15}{i[1]:<15}")  

    print(f"Overall standings based on the audience scores only:")
    print(f"{'Rank':6}{'Contestant No':15}{'Score':15}")
    print("-----------------------------")
    rank_counter3=0
    sorted_overall_data = sorted(overall_points, key=lambda x: (x[2],), reverse=True)
    for i in (sorted_overall_data):
        rank_counter3+=1
        print(f"{rank_counter3:<6}{i[0]:<15}{i[2]:<15}")      
    print("Total scores for each week and the number of week championships of the contestants:")
    print("Contestant No", end="  ")
    for i in range(competition_weeks):
        print(f"WEEK-{i+1}",end="  ")

    weekly_points.append(week_champions)
    print("Week Championships")
    rank_counter3=0
    contestant_no= 0
    print("-"*(15+(competition_weeks*8)+19))
    for i in range(len(weekly_points[0])):
        contestant_no+=1
        while rank_counter3==week_counter+1:
            rank_counter3=0
            print("")
        else:
            print(f"{contestant_no:<15}",end="")
            for x in weekly_points:
                print(f"{x[i]:<7}",end="  ")
                rank_counter3+=1
    print("")
    

    print(f"Total scores received by the contestants from the coaches:")
    print(f"{'Contestant No':15}",end="")
    for coach_number in range (contestant_number):

        print(f"{'Coach '}{coach_number+1:<5}",end="")
    print("")
    print("-"*(15+(contestant_number-1)*11+7))
    rank_counter5=0
    
    for contestant_order in range(contestant_number):
        rank_counter5+=1
        
        print(f"{rank_counter5:<15}",end="")
        for coach_order in range(contestant_number):
            
            print(f"{coach_scores_per_contestant[coach_order][contestant_order]:<11}",end="")
            
        print("\n")

    




    cont=input("Whether a new competition will be organized?(yYnN):")
while cont not in ['y','Y','n','N']:
    print("Invalid Data Entry!")
    cont=input("Whether a new competition will be organized?(yYnN):")
if cont in ['n','N']:
    exit










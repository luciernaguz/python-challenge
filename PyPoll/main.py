import os
import csv

csvpath = os.path.join("Resources", "election_data.csv")
VoterID=[]
County=[]
Candidate=[]
TotalVotes = 0 
KhanVotes = 0
CorreyVotes = 0
LiVotes = 0
OtooleyVotes = 0

KeyWinner=""
# Open and read csv
with open(csvpath) as csv_file:
    csvreader =csv.reader(csv_file, delimiter=",")
 
    # Read the header row first (skip this part if there is no header)
    csv_header = next(csvreader)
    #print(csvreader)
    #print(f"Header: {csv_header}")

    #Read each row of data after the header
    cont1=0
    cont2=0
    for row in csvreader:
        #cont no necessary  with len 
        #cont+=1
        VoterID.append(row[0])
        County.append(row[1])
        Candidate.append(row[2])
        #Obtein TotalVotes
        TotalVotes+=1
        #Total each candidate
        if row[2] == "Khan": 
            KhanVotes +=1
        elif row[2] == "Correy":
            CorreyVotes +=1
        elif row[2] == "Li": 
            LiVotes +=1
        elif row[2] == "O'Tooley":
            OtooleyVotes +=1
        #NameWinner=max[KhanVotes,CorreyVotes,LiVotes,OtooleyVotes]
        #print(NameWinner)
    #Dic KEYS/VALUES
    #Dic for Winner
    NameCandidates=["Khan","Correy","Li","O´Tooley"]
    CandidatesVotes=[KhanVotes,CorreyVotes,LiVotes,OtooleyVotes]
    NameWinner=dict(zip(NameCandidates,CandidatesVotes))
    KeyWinner=max(NameWinner,key=NameWinner.get)
    print(KeyWinner)
    #The percentage of votes each candidate won   votes/total *100
    PercentageKhan=(KhanVotes/TotalVotes)*100
    print(f"{PercentageKhan:.3}%")
    PercentageCorrey=(CorreyVotes/TotalVotes)*100
    print(f"{PercentageCorrey:.3}%")
    PercentageLi=(LiVotes/TotalVotes)*100
    print(f"{PercentageLi:.3f}%")
    PercentageOtooley=(OtooleyVotes/TotalVotes)*100
    print(f"{PercentageOtooley:.3f}%")
    #function to parser percentage 
    
print(f"Election Results")
print(f"----------------------------------------")
print(f"Total Votes:{len(VoterID)}")
print(f"----------------------------------------")
print(f"Khan: {PercentageKhan:.3}% ({KhanVotes})")
print(f"Correy: {PercentageCorrey:.3}% ({CorreyVotes})")
print(f"Li: {PercentageLi:.3f}% ({LiVotes})")
print(f"O´Tooley: {PercentageOtooley:.3f}% ({OtooleyVotes})")
print(f"----------------------------------------")
print(f"Winner:{KeyWinner}")
print(f"----------------------------------------")

# Specify the file to write to
output_path = os.path.join("analysis", "Election Results.txt")
# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path,'w') as outfile:

    # Initialize csv.writer
    #csvwriter = csv.writer(outfile)
    #Write the first row (column headers)
    #csvwriter.writerow("Financial Analysis")
    
    outfile.write(f"Election Results\n")
    outfile.write(f"------------------------------------------------\n")
    outfile.write(f"Total Votes:{len(VoterID)}\n")
    outfile.write(f"----------------------------------------\n")
    outfile.write(f"Khan: {PercentageKhan:.3}% ({KhanVotes})\n")
    outfile.write(f"Correy: {PercentageCorrey:.3}% ({CorreyVotes})\n")
    outfile.write(f"Li: {PercentageLi:.3f}% ({LiVotes})\n")
    outfile.write(f"O´Tooley: {PercentageOtooley:.3f}% ({OtooleyVotes})\n")
    outfile.write(f"----------------------------------------\n")
    outfile.write(f"Winner:{KeyWinner}\n")


   



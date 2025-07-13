import random

QuestionBank = [
    {
        "question": "Name a city in Wales",
        "answers": {
            "cardiff": 91,
            "swansea": 82,
            "newport": 62,
            "st davids": 7,
            "bangor": 0,
            "st asaph": 0,
            "wrexham": 0
        }
    },
    {
        "question": "Name a planet in the solar system",
        "answers": {
            "mercury": 9,
            "venus": 7,
            "earth": 95,
            "mars": 85,
            "jupiter": 12,
            "saturn": 8,
            "uranus": 4,
            "neptune": 0
        }
    },
    {
        "question": "Name a Harry Potter character",
        "answers": {
            "harry potter": 96,
            "ron weasley": 84,
            "hermione granger": 88,
            "albus dumbledore": 34,
            "minerva mcgonagall": 15,
            "neville longbottom": 7,
            "seamus finnigan": 0,
            "madam hooch": 0
        }
    },
    {
        "question": "Name a UK Prime Minister",
        "answers": {
            "rishi sunak": 88,
            "boris johnson": 85,
            "david cameron": 72,
            "theresa may": 66,
            "winston churchill": 49,
            "edward heath": 7,
            "neville chamberlain": 0,
            "henry campbell-bannerman": 0
        }
    },
    {
        "question": "Name an Olympic sport",
        "answers": {
            "athletics": 91,
            "swimming": 89,
            "gymnastics": 78,
            "cycling": 66,
            "sailing": 12,
            "archery": 4,
            "modern pentathlon": 0
        }
    },
    {
        "question": "Name a type of pasta",
        "answers": {
            "spaghetti": 96,
            "penne": 87,
            "fusilli": 75,
            "farfalle": 32,
            "tagliatelle": 15,
            "orzo": 4,
            "ditalini": 0
        }
    },
    {
        "question": "Name a European capital city",
        "answers": {
            "paris": 97,
            "rome": 94,
            "berlin": 88,
            "madrid": 82,
            "lisbon": 35,
            "ljubljana": 0,
            "vaduz": 0
        }
    },
    {
        "question": "Name a Shakespeare play",
        "answers": {
            "hamlet": 93,
            "romeo and juliet": 91,
            "macbeth": 88,
            "othello": 64,
            "king lear": 41,
            "cymbeline": 0,
            "pericles": 0
        }
    },
    {
        "question": "Name a chemical element",
        "answers": {
            "oxygen": 94,
            "hydrogen": 90,
            "carbon": 86,
            "iron": 74,
            "zinc": 31,
            "ruthenium": 0,
            "ytterbium": 0
        }
    },
    {
        "question": "Name a fruit",
        "answers": {
            "apple": 97,
            "banana": 96,
            "orange": 94,
            "grape": 88,
            "kiwi": 51,
            "guava": 4,
            "salak": 0
        }
    },
    {
        "question": "Name a programming language",
        "answers": {
            "python": 93,
            "java": 89,
            "c++": 85,
            "javascript": 82,
            "swift": 36,
            "r": 7,
            "nim": 0
        }
    },
    {
        "question": "Name a famous artist",
        "answers": {
            "picasso": 91,
            "da vinci": 90,
            "van gogh": 89,
            "monet": 66,
            "banksy": 42,
            "arcimboldo": 0,
            "boldini": 0
        }
    },
    {
        "question": "Name a James Bond actor",
        "answers": {
            "sean connery": 92,
            "roger moore": 89,
            "daniel craig": 88,
            "pierce brosnan": 84,
            "george lazenby": 25,
            "timothy dalton": 14,
            "barry nelson": 0
        }
    },
    {
        "question": "Name a language spoken in Africa",
        "answers": {
            "swahili": 72,
            "arabic": 64,
            "afrikaans": 51,
            "yoruba": 34,
            "zulu": 23,
            "twi": 3,
            "kanuri": 0
        }
    },
    {
        "question": "Name a UK motorway",
        "answers": {
            "m1": 91,
            "m25": 88,
            "m6": 84,
            "m4": 76,
            "m5": 68,
            "m53": 11,
            "m181": 0
        }
    },
    {
        "question": "Name a nursery rhyme",
        "answers": {
            "humpty dumpty": 95,
            "baa baa black sheep": 92,
            "jack and jill": 89,
            "twinkle twinkle little star": 87,
            "little miss muffet": 58,
            "cock a doodle doo": 3,
            "polly put the kettle on": 0
        }
    },
    {
        "question": "Name a dog breed",
        "answers": {
            "labrador": 96,
            "german shepherd": 89,
            "poodle": 82,
            "bulldog": 79,
            "shih tzu": 41,
            "komondor": 3,
            "otterhound": 0
        }
    },
    {
        "question": "Name a UK river",
        "answers": {
            "thames": 94,
            "severn": 88,
            "trent": 64,
            "tyne": 48,
            "avon": 33,
            "ouse": 11,
            "usk": 0
        }
    },
    {
        "question": "Name a country that ends in -stan",
        "answers": {
            "pakistan": 91,
            "afghanistan": 86,
            "kazakhstan": 72,
            "turkmenistan": 33,
            "kyrgyzstan": 21,
            "tajikistan": 14,
            "uzbekistan": 0
        }
    },
    {
        "question": "Name a London Underground line",
        "answers": {
            "central": 88,
            "piccadilly": 86,
            "northern": 83,
            "jubilee": 76,
            "district": 63,
            "metropolitan": 28,
            "waterloo & city": 0
        }
    },
    {
        "question": "Name a famous explorer",
        "answers": {
            "christopher columbus": 95,
            "marco polo": 88,
            "ferdinand magellan": 67,
            "ernest shackleton": 48,
            "roald amundsen": 33,
            "mary kingsley": 4,
            "ibn battuta": 0
        }
    },
    {
        "question": "Name a classical composer",
        "answers": {
            "mozart": 94,
            "beethoven": 93,
            "bach": 88,
            "tchaikovsky": 62,
            "vivaldi": 41,
            "grieg": 9,
            "satie": 0
        }
    }
]

#  GLOBAL VARIABLES  #
QuestionsAsked = set()
# Track used question, so that the same question doesn't get repeated in a game.

AnswersGiven = set()
# Track answers used per question
# Two questions could have the same answers so this needs to be reset ever round of questions

################  Functions ############################################################################################

def GetPlayerName(PlayerNumber):
    while True:
        name = input(f"Please enter name for Player {PlayerNumber}: ").strip()
        if len(name) > 1:
            return name
        print("Name must be at least 2 characters long. Please try again.")


def GetQuestion():
    available = [i for i in range(len(QuestionBank)) if i not in QuestionsAsked]
    # list of indexes from the question bank that haven’t been used yet
    if not available:
        print("No questions available")
        exit() #if none found end program
    index = random.choice(available) #pick random question from those available
    QuestionsAsked.add(index) #flag question as asked
    return QuestionBank[index]["question"], QuestionBank[index]["answers"]


def AskQuestion(PlayerName, TeamData, QuestionToAsk, ValidAnswers):
    global AnswersGiven
    # using the global keyword allows me to alter the value of a global variable
    while True:
        answer = input(f"{PlayerName}, {QuestionToAsk} ").strip().lower()
        #get the answer and convert to lower text removing spaces to check against the answer dictionary
        if answer in AnswersGiven:
        # validation - can't repeat a previously used answer
            print("That answer has already been used for this question. Try again.")
        else:
            AnswersGiven.add(answer)
            # if the answer hasn't been used we can class it as valid
            # add it to the list of used answers until the next question
            break
    score = ValidAnswers.get(answer, 100)
    #return the score value for the answer or error 100
    TeamData["score"] += score
    #add the score to the teams score
    if score == 0:
        print(f"Correct you have scored: {score}")
        print("Congratulations you've found a pointless answer!")
    elif score == 100:
        print("Wrong answer. Scored 100")
    else:
        print(f"Correct you have scored: {score}")


def EliminateHighestScoringTeam(teams):
    # Find the highest scoring team and eliminate them.
    highest_score = teams[0]["score"]
    highest_score_index = 0
    # Start by assuming team 0 is the highest scorer.
    for i in range(1, len(teams)):  # check teams 1, 2, …
        # If this team’s score beats the current highest, update trackers.
        if teams[i]["score"] > highest_score:
            highest_score = teams[i]["score"]
            highest_score_index = i
    # Say goodbye to the eliminated team.
    players = teams[highest_score_index]['players']
    print(f"\n{teams[highest_score_index]['name']} ")
    print(f"{players[0]} and {players[1]} have been eliminated")
    # Remove that team from the list and return the updated list of teams
    teams.pop(highest_score_index)
    return teams


def RoundThree(teams):
    #initialise win count
    teams[0]["wins"] = 0
    teams[1]["wins"] = 0
    while teams[0]["wins"] < 2 and teams[1]["wins"] < 2:
        print(f"\nHead-to-Head Question:")
        QuestionPrompt, ValidAnswers = GetQuestion()
        global AnswersGiven
        AnswersGiven = set()
        scores = []
        for team in teams:
            player = team["players"][0]
            AskQuestion(player, team, QuestionPrompt, ValidAnswers)
            scores.append(team["score"])
            team["score"] = 0
        if scores[0] < scores[1]:
            print(f"{teams[0]['name']} wins this round!")
            teams[0]["wins"] += 1
        elif scores[1] < scores[0]:
            print(f"{teams[1]['name']} wins this round!")
            teams[1]["wins"] += 1
        else:
            print("It's a tie! No point awarded.")
        print(f"Current wins: {teams[0]['name']} = {teams[0]['wins']}, {teams[1]['name']} = {teams[1]['wins']}")
    # one of the teams one with 2 points: keep them and eliminate the other team
    if teams[0]["wins"] == 2:
        print(f"{teams[1]['name']} eliminated")
        return teams[0]
    else:
        print(f"{teams[0]['name']} eliminated")
        return teams[1]


def FinalRound(team):
    global AnswersGiven
    print(f"\n Finalists: {team['players'][0]} and {team['players'][1]} ")
    print("You will be asked 3 questions. Try to give at least one pointless answer to win")
    pointless_found = False
    for i in range(1, 4):
        QuestionPrompt, ValidAnswers = GetQuestion()
        AnswersGiven = set()
        print(f"\n Final Round Question {i} of 3:{QuestionPrompt}")
        answer = input(f"Your answer: ").strip().lower()
        score = ValidAnswers.get(answer, 100)
        if score == 0:
            print("You've found a pointless answer and won the game...here's a prize!!!!")
            pointless_found = True
            break
        elif score == 100:
            print("Wrong answer")
        else:
            print(f"Correct, but not pointless")
    if not pointless_found:
    # after 3 questions if still false game over
        print(f"\n😞 Sorry, {team['name']}, none of your answers were pointless. Better luck next time!")

################  MAIN CODE ############################################################################################

# Collect all 8 valid player names
PlayersNames = []
for x in range(8):
    PlayersNames.append(GetPlayerName(x + 1))
print("\nCollected players:", PlayersNames)
print("The goal of this game is to provide a correct answer that the fewest people know, aiming for a 0.")

# Create teams
teams = []
for i in range(4): # 0, 1, 2, 3
    team = {
        "name": f"Team {i+1}",
        "players": PlayersNames[i*2:(i+1)*2],
        #0:2[0,1], 2:4[2,3], 4:6[4,5], 6:8[6,7]
        "score": 0
    }
    teams.append(team)

#Now have 4 teams with two players in each team, all team scores set to 0

# Round 1
print("\n========== ROUND 1 ==========")
for RoundQuestion in range(2):
#run round 1 twice for each partner in the team
    QuestionPrompt, ValidAnswers = GetQuestion()
    #return question text and answer values to look up (dictionary)

    AnswersGiven = set()
    #reset variable for use
    # (more for round 2 than round 1) but think it's good practise to code it in the loop

    print(f"\nQuestion {RoundQuestion + 1}:")
    for team in teams:
        player = team["players"][RoundQuestion]
        #get the player1/2 from each team to ask the question

        AskQuestion(player, team, QuestionPrompt, ValidAnswers)
        #as the "player" in the "team" the "QuestionPrompt"  and pass in answer dictionary

print("\n Team scores after Round 1:")

for team in teams:
    print(f"{team['name']}: {team['score']} points")
#print the scores for each team

teams = EliminateHighestScoringTeam(teams)
#teams updated with the high scorers removed

# Round 2
print("\n========== ROUND 2 ==========")
for RoundQuestion in range(2):
#as with round one we ask two questions
    QuestionPrompt, ValidAnswers = GetQuestion()

    AnswersGiven = set()

    print(f"\nQuestion {RoundQuestion + 1}:")

    for team in teams:
        player = team["players"][RoundQuestion]
        AskQuestion(player, team, QuestionPrompt, ValidAnswers)

print("\n Team scores after Round 2:")

for team in teams:
    print(f"{team['name']}: {team['score']} points")

teams = EliminateHighestScoringTeam(teams)

for team in teams:
    team["score"] = 0
#after round 1 and 2 we rest the team scores as they are now best of 3 in the head to head

# Head-to-Head
print("\n========== HEAD-TO-HEAD ==========")
LastTeam = RoundThree(teams)
#run the head to head and return the winning team

# Final round
print("\n========== FINAL ROUND ==========")
FinalRound(LastTeam)
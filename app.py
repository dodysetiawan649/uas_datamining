import pickle
from flask import Flask, request, render_template

app = Flask(__name__)

model_file = open('socc.pkl', 'rb')
model = pickle.load(model_file)


@app.route('/')
def index():
    return render_template('index.html', output='Silakan Pilih')


@app.route('/hasil', methods=['POST'])
def hasil():
    date, home_team, away_team, tournament = [
        x for x in request.form.values()]
    data = []

    data.append(int(date))
    data.append(int(home_team))
    data.append(int(away_team))
    data.append(int(tournament))


    skor = model.hasil([data])
    output = (skor[0])
#     # if output == 1.0:
#     hasil = "Anda beresiko penyakit jantung"
#     # else:
#     #     hasil = "Anda tidak beresiko penyakit jantung"



        # iterating through each match to find the match_id
    for match in hasil:
        home_team_value = (match['home_team']['home_team_name'] == home_team)
        away_team_value = (match['away_team']['away_team_name'] == away_team)

        if home_team_value and away_team_value:
            match_id = match['match_id']
            score = str(match['home_score']) + ' : ' + str(match['away_score'])

    # checking if the match is found or not
    # if found then displaying the right result
    if match_id != None:
        print('{} vs {} has match id: {}'.format(home_team, away_team, match_id))
        print('Score: {}'.format(score))
    else:
        print('No match found')

    # let's try to find all the results for Barcelona for
    # La Liga season 2008-09
    for match in hasil:
        home_team_value = match['home_team']['home_team_name']
        away_team_value = match['away_team']['away_team_name']

        if home_team_value == 'Barcelona' or away_team_value == 'Barcelona':
            score = str(match['home_score']) + ' : ' + str(match['away_score'])
            print('{} vs {}, score: {}'.format(
                home_team_value, away_team_value, score))

    return render_template('index.html', output=hasil, date=date, home_team=home_team, away_team=away_team, tournament=tournament, home_team_score=home_team_score, away_team_score=away_team_score)


    if __name__ == '__main__':
        app.run(debug=True)

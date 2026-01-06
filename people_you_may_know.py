import json
def load_data(filename):
    with open(filename,"r") as f:
        return json.load(f)
def find_people_you_may_know(user_id,data):
    user_friends = {}
    #unique values pick for user id in each row of friends.
    for user in data['users']:
        user_friends[user['id']] = set(user['friends'])
    if user_id not in user_friends:
        return []
    #I got direct friends from dict with name user_friends(key) , this will get me the value of that key.
    direct_friends = user_friends[user_id]
    suggestions = {}

    for friend in direct_friends:
        for mutual in user_friends[friend]:
            if mutual != user_id and mutual not in direct_friends:
                #count mutual friends
                suggestions[mutual] = suggestions.get(mutual,0) + 1
    
    sorted_suggestions = sorted(suggestions.items(),key = lambda x:x[1],reverse=True)
    return [user_id for user_id, mutual_count in sorted_suggestions]
#Load the data
data = load_data("messive_data.json")
user_id = 1
recc = find_people_you_may_know(user_id,data)
print(recc)


        
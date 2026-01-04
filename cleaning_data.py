import json
from contextlib import redirect_stdout

#load the data 
def load_data(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    return data

#cleaning and preprocessing the data
def clean_data(data):
    # Remove missing name users
    data['users'] =  [user for user in data['users'] if user['name'].strip()]
    
    
    #Remove Duplicate friends
    for user in data['users']:
        user['friends'] = list(set(user['friends']))

    #Remove Inactive users(no likes or no friends)
    data['users'] = [user for user in data['users'] if user['friends'] or user['liked_pages']]

    #Remove duplicate pages(I will use dict as it has unique keys)
    unique_pages= {}
    for page in data['pages']:
        unique_pages[page['id']] = page
    data['pages'] = list(unique_pages.values())

    
    return data


#functionto display users and their connections
def display_users(cleaned_data):
    print("Users and their connections: ")
    for user in cleaned_data['users']:
        
        print(f"{user['name']} has friends with User_Id's: {user['friends']} and Liked Pages with page_Id's:{user['liked_pages']}")
    print("\n Page Information: ")
    for page in cleaned_data['pages']:
        print(f"Page ID: {page['id']}, Page Name: {page['name']}")
            
data = load_data('data.json')
cleaned_data = clean_data(data)
with open('cleaned_data_output.txt', 'w') as f:
    with redirect_stdout(f):
        display_users(cleaned_data)

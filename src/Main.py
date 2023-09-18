import pandas as pd
from telegram import Bot

# Your Telegram Bot Token
BOT_TOKEN = "6591582102:AAF_v5S5X1ircq1u3YetDFlj5i7YerB58ss"

# The group chat ID you want to query
GROUP_CHAT_ID = -1001975455133  # Use a negative value to represent a group chat ID

def get_group_members_info(bot_token, chat_id):
    bot = Bot(token=bot_token)
    members_info = []

    # Get the count of members in the group
    members_count = bot.get_chat_members_count(chat_id)

    # Fetch information about each member
    members = bot.get_chat_members(chat_id)
    
    for member in members:
        user_id = member.user.id
        username = member.user.username
        first_name = member.user.first_name
        last_name = member.user.last_name
        language_code = member.user.language_code
        status = member.status
        join_date = member.date  # Get the join date
        
        # Append member information to the list
        members_info.append({
            "User ID": user_id,
            "Username": username,
            "First Name": first_name,
            "Last Name": last_name,
            "Language Code": language_code,
            "Status": status,
            "Join Date": join_date,
        })

    return members_info

def save_member_info_to_csv(members_info, filename):
    # Create a DataFrame
    df = pd.DataFrame(members_info)
    
    # Save it as a CSV file
    df.to_csv(filename, index=False)

if __name__ == "__main__":
    members_info = get_group_members_info(BOT_TOKEN, GROUP_CHAT_ID)
    if members_info:
        save_member_info_to_csv(members_info, "group_members_info.csv")
        print("Member information saved to group_members_info.csv")
    else:
        print("No members found in the group or information is not available.")

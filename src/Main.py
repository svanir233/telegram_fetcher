from telethon.sync import TelegramClient
import csv
import json
import datetime

# Your API ID and API hash (obtain these from my.telegram.org)
api_id = 29592935
api_hash = '7e41b018b51c7a4f62d54af120a58ce2'

# Your bot token
bot_token = '6591582102:AAF_v5S5X1ircq1u3YetDFlj5i7YerB58ss'

# Initialize the client
client = TelegramClient('mnlwin_bot_session', api_id, api_hash)

async def main():
    await client.start(bot_token=bot_token)
        # Search for the group chat by title (replace 'GroupName' with your group name)
    group_entity = await client.get_entity(-1001975455133)
        
    # Get the group chat members
    members = []
    async for member in client.iter_participants(group_entity):
    # Convert member object to dictionary
        member_dict = member.to_dict()
        
        # Append member information as a dictionary
        members.append(member_dict)

    # Log out at the end of your operations
    await client.log_out()

    # Generate a timestamp for the current time
    current_time = datetime.datetime.now().strftime('%Y%m%d%H%M%S')

    # Save members information to a CSV file
    with open(f'group_members_{current_time}.csv', 'w', newline='', encoding='utf-8') as csv_file:
        # Extract column names from the first member's keys
        column_names = members[0].keys()
        
        writer = csv.DictWriter(csv_file, fieldnames=column_names)
        
        # Write header row
        writer.writeheader()
        
        # Write member information rows
        writer.writerows(members)

    # Save members information to a JSON file
    with open(f'group_members{current_time}.json', 'w', encoding='utf-8') as json_file:
        json.dump(members, json_file, ensure_ascii=False, indent=4)

if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
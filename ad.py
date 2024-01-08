from pyrogram import Client
import asyncio
from colorama import Fore, Style, init
init(autoreset=True)

async def get_chat_ids(app):
    chat_ids = []
    async for dialog in app.get_dialogs():
        chat_ids.append(dialog.chat.id)
        chat_ids = [str(chat_id) for chat_id in chat_ids if str(chat_id).startswith('-')]
        chat_ids = [int(chat_id) for chat_id in chat_ids]
    return chat_ids

async def send_last_message_to_groups(app, timee, numtime, chat_ids):
    async for message in app.get_chat_history('me', limit=1):
        last_message = message.id

    for i in range(numtime):
        for chat_id in chat_ids:
            try:
                await app.forward_messages(chat_id, "me", last_message)
                print(f"{Fore.GREEN}Message sent to chat_id {chat_id}")
                await asyncio.sleep(2)
            except Exception as e:
                print(f"{Fore.RED}Failed to send message to chat_id {chat_id}: {e}")
            await asyncio.sleep(5)
        await asyncio.sleep(timee)

async def leave_chats(app, chat_ids):
    for chat_id in chat_ids:
        try:
            await app.leave_chat(chat_id)
            print(f"{Fore.CYAN}Left chat_id {chat_id}")
        except Exception as e:
            print(f"{Fore.RED}Failed to leave chat_id {chat_id}: {e}")

async def join_group(app, chat_id):
    try:
        await app.join_chat(chat_id)
        print(f"{Fore.MAGENTA}Joined chat_id {chat_id}")
    except Exception as e:
        print(f"{Fore.RED}Failed to join chat_id {chat_id}: {e}")

async def main():
    api_id = '26066257'
    api_hash = '5159005d97d4d671081c998a61577833'
    app = Client("my_account", api_id, api_hash)
    await app.start()

    while True:

        a = int(input(
            f"{Style.BRIGHT}{Fore.YELLOW}1. Scrape Group List\n2. AutoSender\n3. Auto Group Joiner\n4. Leave all groups\n5. Exit\nEnter the choice: {Style.RESET_ALL}"
        ))

        if a == 1:
            chat_ids = await get_chat_ids(app)
            print(f"{Fore.CYAN}Group IDs: {chat_ids}")

        elif a == 2:
            chat_ids = await get_chat_ids(app)
            numtime = int(input("How many times you want to send the message: "))
            timee = int(input("Enter the time delay: "))
            await send_last_message_to_groups(app, timee, numtime, chat_ids)

        elif a == 3:
            chat_id = input("Enter the Chat ID to join: ")
            await join_group(app, chat_id)

        elif a == 4:
            chat_ids = await get_chat_ids(app)
            await leave_chats(app, chat_ids)

        elif a == 5:
            await app.stop()
            break

if __name__ == "__main__":
    authMain = "L"
    stytext = f"{Fore.CYAN}{Style.BRIGHT}"
    stytext += '''

░██████╗██╗░░██╗██╗██╗░░░██╗░█████╗░███╗░░██╗░██████╗░  ░█████╗░██████╗░██████╗░░█████╗░████████╗
██╔════╝██║░░██║██║██║░░░██║██╔══██╗████╗░██║██╔════╝░  ██╔══██╗██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝
╚█████╗░███████║██║╚██╗░██╔╝███████║██╔██╗██║██║░░██╗░  ███████║██║░░██║██████╦╝██║░░██║░░░██║░░░
░╚═══██╗██╔══██║██║░╚████╔╝░██╔══██║██║╚████║██║░░╚██╗  ██╔══██║██║░░██║██╔══██╗██║░░██║░░░██║░░░
██████╔╝██║░░██║██║░░╚██╔╝░░██║░░██║██║░╚███║╚██████╔╝  ██║░░██║██████╔╝██████╦╝╚█████╔╝░░░██║░░░
╚═════╝░╚═╝░░╚═╝╚═╝░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░  ╚═╝░░╚═╝╚═════╝░╚═════╝░░╚════╝░░░░╚═╝░░░
    '''
    authMain1 = "L "
    print(stytext)
    authinp = input("Enter the authorization key: ")
    
    if authMain == authinp or authMain1 == authinp:
        asyncio.run(main())
    else:
        print(f"{Fore.RED}Invalid auth key!!\nExiting.....")

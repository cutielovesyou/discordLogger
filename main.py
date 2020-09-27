import discord,getpass,os
from colorama import init,Fore,Style
init(convert=True)
client=discord.Client()
@client.event
async def on_connect():
    print(Fore.RED+"connected to: "+Fore.GREEN+str(client.user)+Style.RESET_ALL+'\n\ntype "1" - log all dms')
    if not os.path.exists(f'{client.user.id}'):
        os.mkdir(f'{client.user.id}')
        open(os.path.join(os.path.abspath(f'{client.user.id}'),f'USER.txt'),'w', encoding='utf-8').write(str(client.user))
    while 1:
        type=input("> ")
        if type=="1":
            if not os.path.exists(f'{client.user.id}/DMLOGS'):os.mkdir(f'{client.user.id}/DMLOGS')
            print(Fore.CYAN+"Logging all open DMs..."+Style.RESET_ALL)
            numdms=1
            for pvtchdm in client.private_channels:
                numdms=numdms+1
            print(Fore.CYAN+"Logging "+Fore.BLUE+str(numdms)+Fore.CYAN+" DMs."+Style.RESET_ALL)
            numdms=1
            with open(os.path.join(os.path.abspath(f'{client.user.id}'),'DMLOGS.txt'),'w+', encoding='utf-8') as f1:
                for ch in client.private_channels:
                    print(Fore.CYAN+str(numdms)+Style.RESET_ALL)
                    numdms=numdms+1
                    f1.write(str(numdms)+' - '+str(ch)+'\n')
                    with open(os.path.join(os.path.abspath(f'{client.user.id}/DMLOGS'),str(numdms)+'.txt'),'w+', encoding='utf-8') as f2:
                        f2.write(str(ch)+'\n\n')
                        async for msg in ch.history(limit=999999999):
                            if msg.content and not msg.attachments:
                                f2.write(f'{msg.author} [{str(msg.created_at)[:-7]}]\n'+msg.content+'\n\n')
                            if msg.content and msg.attachments:
                                f2.write(f'{msg.author} [{str(msg.created_at)[:-7]}]\n'+msg.content+'\n'+f'({msg.attachments[0].url})'+'\n\n')
                            if not msg.content and msg.attachments:
                                f2.write(f'{msg.author} [{str(msg.created_at)[:-7]}]\n'+f'({msg.attachments[0].url})'+'\n\n')
            print(Fore.CYAN+"Done logging "+Fore.BLUE+str(numdms)+Fore.CYAN+" DMs."+Style.RESET_ALL)
token=getpass.getpass("Enter User Token (right click to paste): ")
client.run(token,bot=False)

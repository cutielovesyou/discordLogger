import discord,getpass,os
from colorama import init,Fore,Style
from glob import glob
init(convert=True)
client=discord.Client()
@client.event
async def on_connect():
    print(Fore.RED+"\nconnected to: "+Fore.GREEN+str(client.user)+Style.RESET_ALL+'\ntype "1" - log all dms\ntype "2" - log certain channel (DM,GROUP,TEXT CHANNELS.)\ntype "3" - log entire server\ntype "4" - filter all logs')
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
            print(Fore.CYAN+"Logging "+Fore.BLUE+str(numdms-1)+Fore.CYAN+" DMs."+Style.RESET_ALL)
            numdms=1
            with open(os.path.join(os.path.abspath(f'{client.user.id}'),'DMLOGS.txt'),'w+', encoding='utf-8') as f1:
                for ch in client.private_channels:
                    print(Fore.CYAN+str(numdms)+Style.RESET_ALL)
                    f1.write(str(numdms)+' - '+str(ch)+'\n')
                    with open(os.path.join(os.path.abspath(f'{client.user.id}/DMLOGS'),str(numdms)+'.txt'),'w+', encoding='utf-8') as f2:
                        f2.write(str(ch)+'\n\n')
                        async for msg in ch.history(limit=999999999,oldest_first=True):
                            if msg.content and not msg.attachments:
                                f2.write(f'{msg.author} [{str(msg.created_at)[:-7]}]\n'+msg.content+'\n\n')
                            if msg.content and msg.attachments:
                                f2.write(f'{msg.author} [{str(msg.created_at)[:-7]}]\n'+msg.content+'\n'+f'({msg.attachments[0].url})'+'\n\n')
                            if not msg.content and msg.attachments:
                                f2.write(f'{msg.author} [{str(msg.created_at)[:-7]}]\n'+f'({msg.attachments[0].url})'+'\n\n')
                    numdms=numdms+1
            print(Fore.CYAN+"Done logging "+Fore.BLUE+str(numdms-1)+Fore.CYAN+" DMs."+Style.RESET_ALL)
        if type=="2":
            if not os.path.exists(f'{client.user.id}/TEXTLOGS'):os.mkdir(f'{client.user.id}/TEXTLOGS')
            if not os.path.exists(f'{client.user.id}/NEXTFILE.ignore'):
                with open(os.path.join(os.path.abspath(f'{client.user.id}'),'NEXTFILE.ignore'),'w+') as fp:
                    fp.write('1')
            chtxt=client.get_channel(int(input('enter channel id: ')))
            print(Fore.CYAN+f"Logging {chtxt}..."+Style.RESET_ALL)
            numdms=int(open(os.path.join(os.path.abspath(f'{client.user.id}'),'NEXTFILE.ignore'),'r').readline())
            with open(os.path.join(os.path.abspath(f'{client.user.id}'),'TEXTLOGS.txt'),'a', encoding='utf-8') as f1:
                f1.write(str(numdms)+' - '+str(chtxt)+'\n')
                with open(os.path.join(os.path.abspath(f'{client.user.id}/TEXTLOGS'),str(numdms)+'.txt'),'w+', encoding='utf-8') as f2:
                    f2.write(str(chtxt)+'\n\n')
                    async for msg in chtxt.history(limit=999999999,oldest_first=True):
                        if msg.content and not msg.attachments:
                            f2.write(f'{msg.author} [{str(msg.created_at)[:-7]}]\n'+msg.content+'\n\n')
                        if msg.content and msg.attachments:
                            f2.write(f'{msg.author} [{str(msg.created_at)[:-7]}]\n'+msg.content+'\n'+f'({msg.attachments[0].url})'+'\n\n')
                        if not msg.content and msg.attachments:
                            f2.write(f'{msg.author} [{str(msg.created_at)[:-7]}]\n'+f'({msg.attachments[0].url})'+'\n\n')
                    numdms=numdms+1
                    with open(os.path.join(os.path.abspath(f'{client.user.id}'),'NEXTFILE.ignore'),'w+') as fp:
                        fp.write(str(numdms))
            print(Fore.CYAN+"Done logging "+Fore.BLUE+str(chtxt)+"."+Style.RESET_ALL)
        if type=="3":
            if not os.path.exists(f'{client.user.id}/SERVERLOGS'):os.mkdir(f'{client.user.id}/SERVERLOGS')
            if not os.path.exists(f'{client.user.id}/NEXTFILESERVER.ignore'):
                with open(os.path.join(os.path.abspath(f'{client.user.id}'),'NEXTFILESERVER.ignore'),'w+') as fp:
                    fp.write('1')
            svtxt=client.get_guild(int(input('enter server id: ')))
            print(Fore.CYAN+f"Logging all of {svtxt.name}..."+Style.RESET_ALL)
            numdms=int(open(os.path.join(os.path.abspath(f'{client.user.id}'),'NEXTFILESERVER.ignore'),'r').readline())
            with open(os.path.join(os.path.abspath(f'{client.user.id}'),'SERVERLOGS.txt'),'a', encoding='utf-8') as f1:
                f1.write(str(numdms)+' - '+str(svtxt)+'\n')
                with open(os.path.join(os.path.abspath(f'{client.user.id}/SERVERLOGS'),str(numdms)+'.txt'),'w+', encoding='utf-8') as f2:
                    f2.write(str(svtxt)+'\n\n')
                    for svch in svtxt.channels:
                        if isinstance(svch,discord.channel.TextChannel):
                            try:
                                async for msg in svch.history(limit=999999999,oldest_first=True):
                                    if msg.content and not msg.attachments:
                                        f2.write(f'{msg.author} [{str(msg.created_at)[:-7]}]\n'+msg.content+'\n\n')
                                    if msg.content and msg.attachments:
                                        f2.write(f'{msg.author} [{str(msg.created_at)[:-7]}]\n'+msg.content+'\n'+f'({msg.attachments[0].url})'+'\n\n')
                                    if not msg.content and msg.attachments:
                                        f2.write(f'{msg.author} [{str(msg.created_at)[:-7]}]\n'+f'({msg.attachments[0].url})'+'\n\n')
                            except discord.errors.Forbidden:
                                pass
                    numdms=numdms+1
                    with open(os.path.join(os.path.abspath(f'{client.user.id}'),'NEXTFILESERVER.ignore'),'w+') as fp:
                        fp.write(str(numdms))
            print(Fore.CYAN+"Done logging all channels in "+Fore.BLUE+svtxt.name+"."+Style.RESET_ALL)
        if type=="4":
            if not os.path.exists(f'{client.user.id}/filtering'):os.mkdir(f'{client.user.id}/filtering')
            y=input('file name: ')
            z=input('find what: ')
            if os.path.exists(f'{client.user.id}/TEXTLOGS'):
                for a in glob(f'{client.user.id}/TEXTLOGS/*.txt'):
                    line_num=1
                    with open(a, "r", encoding='utf8') as f:
                        lines = f.readlines()
                    with open(os.path.join(os.path.abspath(f'{client.user.id}/filtering'),y+'.txt'), "w+",encoding='utf8') as f:
                        print(a)
                        for line in lines:
                            b=line.split()
                            if not len(b)==0:
                                b=' '.join(b)
                                if z in b:
                                    f.write('list by catnip - '+b+'\n')
                            line_num=line_num+1
            if os.path.exists(f'{client.user.id}/DMLOGS'):
                for a in glob(f'{client.user.id}/DMLOGS/*.txt'):
                    line_num=1
                    with open(a, "r", encoding='utf8') as f:
                        lines = f.readlines()
                    with open(os.path.join(os.path.abspath(f'{client.user.id}/filtering'),y+'.txt'), "a+",encoding='utf8') as f:
                        print(a)
                        for line in lines:
                            b=line.split()
                            if not len(b)==0:
                                b=' '.join(b)
                                if z in b:
                                    f.write('list by catnip - '+b+'\n')
                            line_num=line_num+1
            if os.path.exists(f'{client.user.id}/SERVERLOGS'):
                for a in glob(f'{client.user.id}/SERVERLOGS/*.txt'):
                    line_num=1
                    with open(a, "r", encoding='utf8') as f:
                        lines = f.readlines()
                    with open(os.path.join(os.path.abspath(f'{client.user.id}/filtering'),y+'.txt'), "w+",encoding='utf8') as f:
                        print(a)
                        for line in lines:
                            b=line.split()
                            if not len(b)==0:
                                b=' '.join(b)
                                if z in b:
                                    f.write('list by catnip - '+b+'\n')
                            line_num=line_num+1
            print('Done.')


#token=getpass.getpass("Enter User Token (right click to paste): ")
token='NjEzMzQ0MjQ3NTU0MjQ0NjEw.X3YYZA.QvNeUdQ42vr-XRFKqeJRdTnWSag'
client.run(token,bot=False)

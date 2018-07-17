from KRISNA import *
from datetime import datetime
from time import sleep
from bs4 import BeautifulSoup
from gtts import gTTS
from googletrans import Translator
from multiprocessing import Pool, Process
from ffmpy import FFmpeg
import time, random, asyncio, timeit, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, urllib, urllib.parse, ast, pytz, wikipedia, pafy, youtube_dl, atexit

print ("\n\n ---  WELCOME TO kris Fatner  ---\n")

cab = KRIS()
#cab = KRIS(authTokenkris="")
cab.log("YOUR TOKEN : {}".format(str(cab.authToken)))
channel = KRISChannel(cab,cab.server.CHANNEL_ID['LINE_TIMELINE'])
cab.log("CHANNEL TOKEN : " + str(channel.getChannelResult()))

cab1 = KRIS()
#cab1 = KRIS(authTokenkris="YOUR TOKEN")
cab1.log("YOUR TOKEN : {}".format(str(cab1.authToken)))
channel = KRISChannel(cab1,cab1.server.CHANNEL_ID['LINE_TIMELINE'])
cab1.log("CHANNEL TOKEN : " + str(channel.getChannelResult()))

cab2 = KRIS()
#cab2 = KRIS(authTokenkris="YOUR TOKEN")
cab2.log("YOUR TOKEN : {}".format(str(cab2.authToken)))
channel = KRISChannel(cab2,cab2.server.CHANNEL_ID['LINE_TIMELINE'])
cab2.log("CHANNEL TOKEN : " + str(channel.getChannelResult()))

cab3 = KRIS()
#cab3 = KRIS(authTokenkris="YOUR TOKEN")
cab3.log("YOUR TOKEN : {}".format(str(cab3.authToken)))
channel = KRISChannel(cab3,cab3.server.CHANNEL_ID['LINE_TIMELINE'])
cab3.log("CHANNEL TOKEN : " + str(channel.getChannelResult()))

cab4 = KRIS()
#cab4 = KRIS(authTokenkris="YOUR TOKEN")
cab4.log("YOUR TOKEN : {}".format(str(cab4.authToken)))
channel = KRISChannel(cab4,cab4.server.CHANNEL_ID['LINE_TIMELINE'])
cab4.log("CHANNEL TOKEN : " + str(channel.getChannelResult()))

print ("LOGIN SUCCESS kris")

cabProfile = cab.getProfile()
cabSettings = cab.getSettings()
KRIS = KRISPoll(cab)

kris = [cab,cab1,cab2,cab3,cab4]
mid = cab.profile.mid
krMID1 = cab1.profile.mid
krMID2 = cab2.profile.mid
krMID3 = cab3.profile.mid
krMID4 = cab4.profile.mid
krisBot=[mid,krMID1,krMID2,krMID3,krMID4]
ghost = [krMID4]
Owner=["u35459f1e84ad208cc56025c259cb1628","u9cc2323f5b84f9df880c33aa9f9e3ae1"]
krisFatner = krisBot + kris + Owner

contact = cab.getProfile()
backup = cab.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

Cyber = {
    "UnsendPesan":False,
    "SpamInvite":False,
    "Contact":False,
    "GName":"Kris",
    "AutoRespon":False,
    "KickRespon":False,
    "KillOn":False,
    "KickOn":False,
    "Upfoto":False,
    "UpfotoBot":False,
    "UpfotoGroup":False,
    "Steal":False,
    "Invite":False,
    "Copy":False,
    "autoAdd":True,
    "PesanAdd":"Terima Kasih Sudah Add Saya",
    "ContactAdd":{},
    "autoBlock":False,
    "autoJoin":True,
    "AutojoinTicket":False,
    "AutoReject":False,
    "autoRead":False,
    "IDSticker":False,
    "Timeline":False,
    "Welcome":False,
    "BackupBot":True,
    "WcText": "Welcome",
    "Leave":False,
    "WvText": "See You Next Time (-_-)",
    "Mic":False,
    "MicDel":False,
    "Adminadd":False,
    "AdminDel":False,
    "Gift":False,
    "readMember":{},
    "readPoint":{},
    "readTime":{},
    "ROM":{},
    "Blacklist":{},
    "Ban":False,
    "Unban":False,
    "AddMention":True,
    "Admin": {
        "u35459f1e84ad208cc56025c259cb1628":True,  
        "u9cc2323f5b84f9df880c33aa9f9e3ae1":True
    },
}

Mozilla = {
    "userAgent": [
        "Mozilla/5.0 (X11; U; Linux i586; de; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)",
        "Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 FirePHP/0.5",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux ppc; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux AMD64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1.1; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; U; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; rv:5.0) Gecko/20100101 Firefox/5.0"
    ],
    "mimic": {
        "copy": False,
        "conpp": False,
        "status": False,
        "target": {}
    }
}

setTime = {}
setTime = Cyber['readTime']
mulai = time.time() 
msg_dict = {}

ProfileMe = {
    "displayName": "",
	"statusMessage": "",
	"pictureStatus": ""
}
ProfileMe["displayName"] = cabProfile.displayName
ProfileMe["statusMessage"] = cabProfile.statusMessage
ProfileMe["pictureStatus"] = cabProfile.pictureStatus

krisProtect = {
    'protect':False,
    'linkprotect':False,
    'inviteprotect':False,
    'cancelprotect':False,
    'ProtectCancelled':False,
}

krisCctv={
    "Point1":{},
    "Point2":{},
    "Point3":{}
}

Help ="""
╔═════════════
║CYBER ARMY COMMAND
╚═════════════
╔═════════════
║ ✰ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰
╠═════════════
║ Owner : Kris
║ line://ti/p/~krissthea
╠═════════════
║╔════════════
║╠❂➣me
║╠❂➣my name
║╠❂➣my bio
║╠❂➣my picture
║╠❂➣my cover
║╠❂➣my video
║╠❂➣speed
║╠❂➣responsename
║╠❂➣my bot
║╠❂➣my team
║╠❂➣spam on [jmlah teks]
║╠❂➣cekmkd: [mid]
║╠❂➣banlock [@]
║╠❂➣banlist
║╠❂➣contact ban
║╠❂➣ban:on
║╠❂➣unban:on
║╠❂➣clear ban
║╠❂➣blocklist
║╠❂➣friendlist
║╠❂➣friendlist mid
║╠❂➣mid [@]
║╠❂➣profile [@]
║╠❂➣runtime
║╠❂➣broadcast:
║╠❂➣contactbc:
║╠❂➣adminadd [@]
║╠❂➣admindel [@]
║╠❂➣admin:add-on
║╠❂➣admin:del-on
║╠❂➣changename:
║╠❂➣changenameall:
║╠❂➣changebio:
║╠❂➣changebioall:
║╠❂➣remove pesan
║╠❂➣restart
║╠❂➣bot logout
║╠❂➣kick [@]
║╠❂➣status
║╠❂➣allprotect on/off
║╠❂➣backup on/off
║╠❂➣unsend on/off
║╠❂➣changepp on/off
║╠❂➣changeppbot on/off
║╠❂➣timeline on/off
║╠❂➣autojoin on/off
║╠❂➣autoreject on/off
║╠❂➣auto jointicket on/off
║╠❂➣gift:on/off
║╠❂➣copy on/off
║╠❂➣clone [@]
║╠❂➣comeback
║╠❂➣steal on/off
║╠❂➣contact on/off
║╠❂➣mic:add-on
║╠❂➣mic:del-on
║╠❂➣mimic on/off
║╠❂➣mimiclist
║╠❂➣refresh
║╚════════════
║ ✰ GRUP ✰
║╔════════════
║╠❂➣Masuk
║╠❂➣@bye
║╠❂➣leaveall grup
║╠❂➣kick [on,off->kickall]
║╠❂➣invite on/off
║╠❂➣kill on/off
║╠❂➣rejectall grup
║╠❂➣lurking on/off/reset
║╠❂➣lurking read
║╠❂➣sider on/off
║╠❂➣tagall
║╠❂➣welcome on/off
║╠❂➣changewelcome: [teks]
║╠❂➣leave on/off
║╠❂➣changeleave: [teks]
║╠❂➣memberlist
║╠❂➣link on/off
║╠❂➣my grup
║╠❂➣r1 grup
║╠❂➣r2 grup
║╠❂➣r3 grup
║╠❂➣gurl
║╠❂➣gcreator
║╠❂➣invite gcreator
║╠❂➣ginfo
║╠❂➣grup id
║╠❂➣cfotogrup on/off
║╠❂➣spaminvite on/off
║╚════════════
║ ✰ MEDIA ✰
║╔════════════
║╠❂➣topnews
║╠❂➣data birth:
║╠❂➣urban:
║╠❂➣sslink:
║╠❂➣maps:
║╠❂➣cekcuaca:
║╠❂➣jadwalshalat:
║╠❂➣idline:
║╠❂➣say-id:
║╠❂➣say-en:
║╠❂➣say-jp:
║╠❂➣say-ar:
║╠❂➣say-ko:
║╠❂➣apakah:
║╠❂➣kapan:
║╠❂➣wikipedia:
║╠❂➣kalender
║╠❂➣image:
║╠❂➣youtube:
║╚════════════
║ ✰ TRANSLATOR ✰
║╔════════════
║╠❂➣indonesian:
║╠❂➣english:
║╠❂➣korea:
║╠❂➣japan:
║╠❂➣thailand:
║╠❂➣arab:
║╠❂➣malaysia:
║╠❂➣jawa:
║╚════════════
║     THANKS TO 
║ kris Fatner & Team
╚═════════════
"""

#------------------------------------------------ SCRIP DEF ----------------------------------------------------------#

def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours,24)
    month, days = divmod(days,30)
    year, month = divmod(month,12)
    century, year = divmod(year,100)
    return '\n%02d Abad\n%02d Tahun\n%02d Bulan\n%02d Hari\n%02d Jam\n%02d Menit\n%02d Detik' % (century, year, month, days, hours, mins, secs)

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def KRIS_FAST_USER(fast):
    global time
    global ast
    global groupParam
    try:
        if fast.type == 0:
            return
        if fast.type == 5:
            if Cyber["autoAdd"] == True:
                if (Cyber["PesanAdd"] in [""," ","\n",None]):
                    pass
                else:
                    Cyber["ContactAdd"][fast.param2] = True
                    usr = cab.getContact(fast.param2)
                    cab.sendMessage(fast.param1, "Haii {} " + str(Cyber["PesanAdd"]).format(usr.displayName))
                    cab.sendMessage(fast.param1, None, contentMetadata={'mid':mid}, contentType=13)

        if fast.type == 5:
            if Cyber['autoBlock'] == True:
                try:
                    usr = cab.getContact(fast.param2)
                    cab.sendMessage(fast.param1, "Haii {} Sorry Auto Block , Komen di TL dulu ya kalo akun asli baru di unblock".format(usr.displayName))
                    cab.talk.blockContact(0, fast.param1)
                    Cyber["Blacklist"][fast.param2] = True
                except Exception as e:
                	cab.log("[SEND_MESSAGE] ERROR : " + str(e))

#--------------------------------------------- PARAM SCRIP AUTO JOIN BOT & AUTO REJECT ------------------------------------------------#

        if fast.type == 13:
            if mid in fast.param3:
              if Cyber['autoJoin'] == True:
                if fast.param2 in krisFatner and fast.param2 in Cyber["Admin"]:
                    cab.acceptGroupInvitation(fast.param1)
                    print ("ANDA JOIN DI GRUP")
            if krMID1 in fast.param3:
              if Cyber['autoJoin'] == True:
                if fast.param2 in krisFatner and fast.param2 in Cyber["Admin"]:
                    cab1.acceptGroupInvitation(fast.param1)
                    print ("BOT 1 JOIN GRUP")
            if krMID2 in fast.param3:
              if Cyber['autoJoin'] == True:
                if fast.param2 in krisFatner and fast.param2 in Cyber["Admin"]:
                    cab2.acceptGroupInvitation(fast.param1)
                    print ("BOT 2 JOIN GRUP")
            if krMID3 in fast.param3:
              if Cyber['autoJoin'] == True:
                if fast.param2 in krisFatner and fast.param2 in Cyber["Admin"]:
                    cab3.acceptGroupInvitation(fast.param1)
                    print ("BOT 3 JOIN GRUP")
                    pass

        if fast.type == 13:
            if mid in fast.param3:
              if Cyber['AutoReject'] == True:
                if fast.param2 not in krisFatner and fast.param2 not in Owner and fast.param2 not in Cyber["Admin"]:
                    gid = cab.getGroupIdsInvited()
                    for i in gid:
                        cab.rejectGroupInvitation(i)
            if krMID1 in fast.param3:
              if Cyber["AutoReject"] == True:
                if fast.param2 not in krisFatner and fast.param2 not in Owner and fast.param2 not in Cyber["Admin"]:
                    gid = cab1.getGroupIdsInvited()
                    for i in gid:
                        cab1.rejectGroupInvitation(i)
            if krMID2 in fast.param3:
              if Cyber["AutoReject"] == True:
                if fast.param2 not in krisFatner and fast.param2 not in Owner and fast.param2 not in Cyber["Admin"]:
                    gid = cab2.getGroupIdsInvited()
                    for i in gid:
                        cab2.rejectGroupInvitation(i)
            if krMID3 in fast.param3:
              if Cyber["AutoReject"] == True:
                if fast.param2 not in krisFatner and fast.param2 not in Owner and fast.param2 not in Cyber["Admin"]:
                    gid = cab3.getGroupIdsInvited()
                    for i in gid:
                        cab3.rejectGroupInvitation(i)
                        pass

#------------------- ( 1 ) ------------------------- PEMBATAS SCRIP SIDER & WC LV ------------------------------------------------#

        elif fast.type == 55:
            try:
                if krisCctv['Point1'][fast.param1]==True:
                    if fast.param1 in krisCctv['Point2']:  
                        Name = cab.getContact(fast.param2).displayName
                        if Name in krisCctv['Point3'][fast.param1]:
                            pass
                        else:
                            krisCctv['Point3'][fast.param1] += "\n~" + Name
                            if " " in Name:
                                nick = Name.split(' ')
                                if len(nick) == 2:
                                    cab.mentionWithkris(fast.param1,fast.param2," Hii\n","" + "\n Nyimak yah kak?" )
                                else:
                                    cab.mentionWithkris(fast.param1,fast.param2," Nah\n","" + "\n Nongol Sini Chat kak ??" )
                            else:
                                cab.mentionWithkris(fast.param1,fast.param2," Hey\n","" + "\n What Are You Doing?" )
                    else:
                        pass
                else:
                    pass
            except:
                pass

        if fast.type == 55:
            try:
                if fast.param1 in Cyber['readPoint']:
                    if fast.param2 in Cyber['readMember'][fast.param1]:
                        pass
                    else:
                        Cyber['readMember'][fast.param1] += fast.param2
                    Cyber['ROM'][fast.param1][fast.param2] = fast.param2
                else:
                   pass
            except:
                pass   

        if fast.type == 17:
            if Cyber["Welcome"] == True:
                if fast.param2 not in kris:
                    ginfo = cab.getGroup(fast.param1)
                    cab.mentionWithkris(fast.param1,fast.param2," Hii","" + "\n " + str(Cyber['WcText']))
                    cab.sendMessage(fast.param1, None, contentMetadata={'mid':fast.param2}, contentType=13)
                    print ("MEMBER HAS JOIN THE GROUP")

        if fast.type == 15:
            if Cyber["Leave"] == True:
                if fast.param2 not in kris:
                    ginfo = cab.getGroup(fast.param1)
                    cab.mentionWithkris(fast.param1,fast.param2," Hii","" + "\n " + str(Cyber['LvText']))
                    cab.sendMessage(fast.param1, None, contentMetadata={'mid':fast.param2}, contentType=13)
                    print ("MEMBER HAS LEFT THE GROUP")

#--------------------------------------------- PARAM SCRIP FOR BACKUP BOT ------------------------------------------------#

        if fast.type == 19:
          if Cyber["BackupBot"] == True:
            if mid in fast.param3:
              if fast.param2 in krisBot:
                if fast.param2 not in krisFatner and fast.param2 not in Owner and fast.param2 not in Cyber["Admin"]:
                    pass
                else:
                    Cyber["Blacklist"][fast.param2] = True
                    f=codecs.open('st2__b.json','w','utf-8')
                    json.dump(Cyber, f, sort_keys=True, indent=4,ensure_ascii=False)
                    try:
                        cab1.findAndAddContactsByMid(fast.param3)
                        cab1.kickoutFromGroup(fast.param1,[fast.param2])
                        cab1.inviteIntoGroup(fast.param1,[fast.param3])
                        cab.acceptGroupInvitation(fast.param1)
                    except:
                        try:
                            cab2.findAndAddContactsByMid(fast.param3)
                            cab2.kickoutFromGroup(fast.param1,[fast.param2])
                            cab2.inviteIntoGroup(fast.param1,[fast.param3])
                            cab.acceptGroupInvitation(fast.param1)
                        except:
                            try:
                                cab3.findAndAddContactsByMid(fast.param3)
                                cab3.kickoutFromGroup(fast.param1,[fast.param2])
                                cab3.inviteIntoGroup(fast.param1,[fast.param3])
                                cab.acceptGroupInvitation(fast.param1)
                            except:
                                try:
                                    x = cab1.getGroup(fast.param1)
                                    x.preventedJoinByTicket = False
                                    cab1.updateGroup(x)
                                    Kris = cab1.reissueGroupTicket(fast.param1)
                                    cab.acceptGroupInvitationByTicket(fast.param1,Kris)
                                    cab1.acceptGroupInvitationByTicket(fast.param1,Kris)
                                    cab2.acceptGroupInvitationByTicket(fast.param1,Kris)
                                    cab3.acceptGroupInvitationByTicket(fast.param1,Kris)
                                    x = cab.getGroup(fast.param1)
                                    x.preventedJoinByTicket = True
                                    cab.updateGroup(x)
                                    cab1.kickoutFromGroup(fast.param1,[fast.param2])
                                    Kris = cab.reissueGroupTicket(fast.param1)
                                except:
                                    pass
                return
            
            if krMID1 in fast.param3:
              if fast.param2 in krisBot:
                if fast.param2 not in krisFatner and fast.param2 not in Owner and fast.param2 not in Cyber["Admin"]:
                    pass
                else:
                    Cyber["Blacklist"][fast.param2] = True
                    f=codecs.open('st2__b.json','w','utf-8')
                    json.dump(Cyber, f, sort_keys=True, indent=4,ensure_ascii=False)
                    try:
                        cab2.findAndAddContactsByMid(fast.param3)
                        cab2.kickoutFromGroup(fast.param1,[fast.param2])
                        cab2.inviteIntoGroup(fast.param1,[fast.param3])
                        cab1.acceptGroupInvitation(fast.param1)
                    except:
                        try:
                            cab3.findAndAddContactsByMid(fast.param3)
                            cab3.kickoutFromGroup(fast.param1,[fast.param2])
                            cab3.inviteIntoGroup(fast.param1,[fast.param3])
                            cab1.acceptGroupInvitation(fast.param1)
                        except:
                            try:
                                cab.findAndAddContactsByMid(fast.param3)
                                cab.kickoutFromGroup(fast.param1,[fast.param2])
                                cab.inviteIntoGroup(fast.param1,[fast.param3])
                                cab1.acceptGroupInvitation(fast.param1)
                            except:
                                try:
                                    x = cab2.getGroup(fast.param1)
                                    x.preventedJoinByTicket = False
                                    cab2.updateGroup(x)
                                    Kris = cab2.reissueGroupTicket(fast.param1)
                                    cab1.acceptGroupInvitationByTicket(fast.param1,Kris)
                                    x = cab1.getGroup(fast.param1)
                                    x.preventedJoinByTicket = True
                                    cab1.updateGroup(x)
                                    cab2.kickoutFromGroup(fast.param1,[fast.param2])
                                    Ticket = cab1.reissueGroupTicket(fast.param1)
                                except:
                                    pass
                return

            if krMID2 in fast.param3:
              if fast.param2 in krisBot:
                if fast.param2 not in krisFatner and fast.param2 not in Owner and fast.param2 not in Cyber["Admin"]:
                    pass
                else:
                    Cyber["Blacklist"][fast.param2] = True
                    f=codecs.open('st2__b.json','w','utf-8')
                    json.dump(Cyber, f, sort_keys=True, indent=4,ensure_ascii=False)
                    try:
                        cab.findAndAddContactsByMid(fast.param3)
                        cab.kickoutFromGroup(fast.param1,[fast.param2])
                        cab.inviteIntoGroup(fast.param1,[fast.param3])
                        cab2.acceptGroupInvitation(fast.param1)
                    except:
                        try:
                            cab1.findAndAddContactsByMid(fast.param3)
                            cab1.kickoutFromGroup(fast.param1,[fast.param2])
                            cab1.inviteIntoGroup(fast.param1,[fast.param3])
                            cab2.acceptGroupInvitation(fast.param1)
                        except:
                            try:
                                cab3.findAndAddContactsByMid(fast.param3)
                                cab3.kickoutFromGroup(fast.param1,[fast.param2])
                                cab3.inviteIntoGroup(fast.param1,[fast.param3])
                                cab2.acceptGroupInvitation(fast.param1)
                            except:
                                try:
                                    x = cab.getGroup(fast.param1)
                                    x.preventedJoinByTicket = False
                                    cab.updateGroup(x)
                                    Kris = cab.reissueGroupTicket(fast.param1)
                                    cab2.acceptGroupInvitationByTicket(fast.param1,Kris)
                                    x = cab2.getGroup(fast.param1)
                                    x.preventedJoinByTicket = True
                                    cab2.updateGroup(x)
                                    cab3.kickoutFromGroup(fast.param1,[fast.param2])
                                    Ticket = cab2.reissueGroupTicket(fast.param1)
                                except:
                                    pass
                return

            if krMID3 in fast.param3:
              if fast.param2 in krisBot:
                if fast.param2 not in krisFatner and fast.param2 not in Owner and fast.param2 not in Cyber["Admin"]:
                    pass
                else:
                    Cyber["Blacklist"][fast.param2] = True
                    f=codecs.open('st2__b.json','w','utf-8')
                    json.dump(Cyber, f, sort_keys=True, indent=4,ensure_ascii=False)
                    try:
                        cab.findAndAddContactsByMid(fast.param3)
                        cab.kickoutFromGroup(fast.param1,[fast.param2])
                        cab.inviteIntoGroup(fast.param1,[fast.param3])
                        cab3.acceptGroupInvitation(fast.param1)
                    except:
                        try:
                            cab1.findAndAddContactsByMid(fast.param3)
                            cab1.kickoutFromGroup(fast.param1,[fast.param2])
                            cab1.inviteIntoGroup(fast.param1,[fast.param3])
                            cab3.acceptGroupInvitation(fast.param1)
                        except:
                            try:
                                cab2.findAndAddContactsByMid(fast.param3)
                                cab2.kickoutFromGroup(fast.param1,[fast.param2])
                                cab2.inviteIntoGroup(fast.param1,[fast.param3])
                                cab3.acceptGroupInvitation(fast.param1)
                            except:
                                try:
                                    x = cab.getGroup(fast.param1)
                                    x.preventedJoinByTicket = False
                                    cab.updateGroup(x)
                                    Kris = cab.reissueGroupTicket(fast.param1)
                                    cab3.acceptGroupInvitationByTicket(fast.param1,Kris)
                                    x = cab3.getGroup(fast.param1)
                                    x.preventedJoinByTicket = True
                                    cab2.updateGroup(x)
                                    cab.kickoutFromGroup(fast.param1,[fast.param2])
                                    Ticket = cab3.reissueGroupTicket(fast.param1)
                                except:
                                    pass
                return

        if fast.type == 13:
          if fast.param3 in Cyber["Blacklist"]: # AUTO KICK JIKA YG DI BLACKLIST MASUK
            if fast.param2 not in krisFatner and fast.param2 not in Owner and fast.param2 not in Cyber["Admin"]:
                random.choice(kris).cancelGroupInvitation(fast.param1,[fast.param3])
                random.choice(kris).kickoutFromGroup(fast.param1,[fast.param2])
                random.choice(kris).kickoutFromGroup(fast.param1,[fast.param3])
                G = random.choice(kris).getGroup(fast.param1)
                G.preventedJoinByTicket = True
                random.choice(kris).updateGroup(G)
                random.choice(kris).sendMessage(fast.param1, None, contentMetadata={'mid': fast.param2}, contentType=13)
                random.choice(kris).sendMessage(fast.param1, "User Added Blacklist, Please to Unfollow blacklist first.\n")

#---------------------------------- SCRIP PROTECT GRUP -------------------------------------#

        if fast.type == 19:
            if fast.param2 not in krisFatner and fast.param2 not in Owner and fast.param2 not in Cyber["Admin"]:
                if fast.param2 in krisBot:
                    pass
                elif krisProtect["protect"] == True:
                    random.choice(kris).kickoutFromGroup(fast.param1,[fast.param2])
                    cab.findAndAddContactsByMid(fast.param3)
                    cab.inviteIntoGroup(fast.param1,[fast.param3])
                    Cyber["Blacklist"][fast.param2] = True
                    random.choice(kris).sendMessage(fast.param1, None, contentMetadata={'mid': fast.param2}, contentType=13)
                    random.choice(kris).sendMessage(fast.param1, "User Added Blacklist (*-_-)/")

        if fast.type == 11:
            if fast.param2 not in krisFatner and fast.param2 not in Owner and fast.param2 not in Cyber["Admin"]:
                if fast.param2 in krisBot:
                    pass
                elif krisProtect["linkprotect"] == True:
                    Cyber["Blacklist"][fast.param2] = True
                    G = random.choice(kris).getGroup(fast.param1)
                    G.preventedJoinByTicket = True
                    random.choice(kris).updateGroup(G)
                    random.choice(kris).kickoutFromGroup(fast.param1,[fast.param2])
                    Cyber["Blacklist"][fast.param2] = True

        if fast.type == 13:
          if fast.param2 not in krisFatner and fast.param2 not in Owner and fast.param2 not in Cyber["Admin"]:
            if fast.param2 in krisBot:
                pass
            elif krisProtect["inviteprotect"] == True:
                Cyber["Blacklist"][fast.param2] = True
                random.choice(kris).cancelGroupInvitation(fast.param1,[fast.param3])
                random.choice(kris).kickoutFromGroup(fast.param1,[fast.param2])
                random.choice(kris).kickoutFromGroup(fast.param1,[fast.param3])
                random.choice(kris).sendMessage(fast.param1, None, contentMetadata={'mid': fast.param2}, contentType=13)
                random.choice(kris).sendMessage(fast.param1, "User Added Blacklist (*-_-)/")
                G = random.choice(kris).getGroup(fast.param1)
                G.preventedJoinByTicket = True
                random.choice(kris).updateGroup(G)
                if fast.param2 not in krisFatner and fast.param2 not in Owner and fast.param2 not in Cyber["Admin"]:
                    if fast.param2 in krisBot:
                        pass
                    elif krisProtect["inviteprotect"] == True:
                        Cyber["Blacklist"][fast.param2] = True
                        random.choice(kris).cancelGroupInvitation(fast.param1,[fast.param3])
                        random.choice(kris).kickoutFromGroup(fast.param1,[fast.param2])
                        random.choice(kris).kickoutFromGroup(fast.param1,[fast.param3])
                        random.choice(kris).sendMessage(fast.param1, None, contentMetadata={'mid': fast.param2}, contentType=13)
                        random.choice(kris).sendMessage(fast.param1, "User Added Blacklist (*-_-)/")
                        G = random.choice(kris).getGroup(fast.param1)
                        G.preventedJoinByTicket = True
                        random.choice(kris).updateGroup(G)
                        if fast.param2 not in krisFatner and fast.param2 not in Owner and fast.param2 not in Cyber["Admin"]:
                            if fast.param2 in krisBot:
                                pass
                            elif krisProtect["cancelprotect"] == True:
                                Cyber["Blacklist"][fast.param2] = True
                                random.choice(kris).cancelGroupInvitation(fast.param1,[fast.param3])
                                random.choice(kris).kickoutFromGroup(fast.param1,[fast.param3])
                                random.choice(kris).sendMessage(fast.param1, None, contentMetadata={'mid': fast.param2}, contentType=13)
                                random.choice(kris).sendMessage(fast.param1, "User Added Blacklist (*-_-)/")
                                G = random.choice(kris).getGroup(fast.param1)
                                G.preventedJoinByTicket = True
                                random.choice(kris).updateGroup(G)

        if fast.type == 32:
            if fast.param2 not in krisFatner and fast.param2 not in Owner and fast.param2 not in Cyber["Admin"]:
                if fast.param2 in krisBot:
                    pass
                elif krisProtect["ProtectCancelled"] == True:
                    random.choice(kris).kickoutFromGroup(fast.param1,[fast.param2])
                    cab.findAndAddContactsByMid(fast.param3)
                    cab.inviteIntoGroup(fast.param1,[fast.param3])
                    Cyber["Blacklist"][fast.param2] = True
                    random.choice(kris).sendMessage(fast.param1, None, contentMetadata={'mid': fast.param2}, contentType=13)
                    random.choice(kris).sendMessage(fast.param1, "User Added Blacklist (*-_-)/")

        if fast.type == 19:
            if fast.param3 in Cyber["Admin"]:        # JIKA ADMIN KE KICK
              if fast.param2 not in krisFatner and fast.param2 not in Owner and fast.param2 not in Cyber["Admin"]:
                  random.choice(kris).kickoutFromGroup(fast.param1,[fast.param2])
                  cab1.findAndAddContactsByMid(fast.param3)
                  cab1.inviteIntoGroup(fast.param1,[fast.param3])
                  G = random.choice(kris).getGroup(fast.param1)
                  G.preventedJoinByTicket = True
                  random.choice(kris).updateGroup(G)
                  Cyber["Blacklist"][fast.param2] = True
                  cab1.sendMessage(fast.param1, None, contentMetadata={'mid': fast.param2}, contentType=13)
                  cab1.sendMessage(fast.param1, "User Added Blacklist (*-_-)/")

        if fast.type == 13:
          if fast.param2 and fast.param3 in Cyber["Blacklist"]: # AUTO KICK JIKA YG DI BLACKLIST MASUK
            if fast.param2 not in krisFatner and fast.param2 not in Owner and fast.param2 not in Cyber["Admin"]:
                random.choice(kris).cancelGroupInvitation(fast.param1,[fast.param3])
                random.choice(kris).kickoutFromGroup(fast.param1,[fast.param2])
                random.choice(kris).kickoutFromGroup(fast.param1,[fast.param3])
                G = random.choice(kris).getGroup(fast.param1)
                G.preventedJoinByTicket = True
                random.choice(kris).updateGroup(G)
                random.choice(kris).sendMessage(fast.param1, None, contentMetadata={'mid': fast.param2}, contentType=13)
                random.choice(kris).sendMessage(fast.param1, "User Added Blacklist, Please to Unfollow blacklist first.\n")

        if fast.type == 17:
          if fast.param2 not in krisFatner and fast.param2 not in Owner and fast.param2 not in Cyber["Admin"]:
            if fast.param2 in Cyber["Blacklist"]: # AUTO KICK JIKA YG DI BLACKLIST MASUK
                random.choice(kris).kickoutFromGroup(fast.param1,[fast.param2])
                G = random.choice(kris).getGroup(fast.param1)
                G.preventedJoinByTicket = True
                random.choice(kris).updateGroup(G)
                Cyber["Blacklist"][fast.param2] = True
                random.choice(kris).sendMessage(fast.param1, None, contentMetadata={'mid': fast.param2}, contentType=13)
                random.choice(kris).sendMessage(fast.param1, "User Added Blacklist, Please to Unfollow blacklist first.\n")

        if fast.type == 55:
          if fast.param2 not in krisFatner and fast.param2 not in Owner and fast.param2 not in Cyber["Admin"]:
            if fast.param2 in Cyber["Blacklist"]: # AUTO KICK JIKA YG DI BLACKLIST MASUK
                random.choice(kris).kickoutFromGroup(fast.param1,[fast.param2])
                G = random.choice(kris).getGroup(fast.param1)
                G.preventedJoinByTicket = True
                random.choice(kris).updateGroup(G)
                Cyber["Blacklist"][fast.param2] = True
                random.choice(kris).sendMessage(fast.param1, None, contentMetadata={'mid': fast.param2}, contentType=13)
                random.choice(kris).sendMessage(fast.param1, "User Added Blacklist, Please to Unfollow blacklist first.\n")

        if fast.type == 46:
            if fast.param2 in krisBot:
                cab.removeAllMessages()
                cab1.removeAllMessages()
                cab2.removeAllMessages()
                cab3.removeAllMessages()

#------------------- ( 2 ) ------------------------- PEMBATAS SCRIP ------------------------------------------------#

        if fast.type == 26:
            msg = fast.message
            text = msg.text
            krisText = msg.text
            msg_id = msg.id
            kirim = msg.to           
            user = msg._from
            if msg.toType == 0 or msg.toType == 2:
                if msg.toType == 0:
                    to = kirim
                elif msg.toType == 2:
                    to = kirim
                if msg.contentType == 0:
                    if Cyber["autoRead"] == True:
                        cab.sendChatChecked(kirim, msg_id)
                        cab1.sendChatChecked(kirim, msg_id)
                        cab2.sendChatChecked(kirim, msg_id)
                        cab3.sendChatChecked(kirim, msg_id)
                    if kirim in Cyber["readPoint"]:
                        if user not in Cyber["ROM"][kirim]:
                            Cyber["ROM"][kirim][user] = True
                    if user in Mozilla["mimic"]["target"] and Mozilla["mimic"]["status"] == True and Mozilla["mimic"]["target"][user] == True:
                        text = msg.text
                        if text is not None:
                            cab.sendMessage(kirim,text)
                    if Cyber["UnsendPesan"] == True:
                        msg = fast.message
                        if msg.toType == 0:
                            cab.log(" {} - {} ".format(str(user), str(krisText)))
                        else:
                            cab.log(" {} - {} ".format(str(kirim), str(krisText)))
                            msg_dict[msg.id] = {"rider": krisText, "pelaku": user, "createdTime": msg.createdTime, "contentType": msg.contentType, "contentMetadata": msg.contentMetadata}
#                    if Cyber["Unsend"] == True:
#                        msg = fast.message
#                        if msg.toType == 0:
#                            cab.log(" {} - {} ".format(str(user), str(krisText)))
#                        else:
#                            cab.log(" {} - {} ".format(str(kirim), str(krisText)))
#                            msg_dict[msg.id] = {"rider": krisText, "from": user, "createdTime": msg.createdTime, "contentType": msg.contentType, "contentMetadata": msg.contentMetadata}
                    if Cyber["Timeline"] == True:
                       if msg.contentType == 16:
                            ret_ = "Info Postingan\n"
                            if msg.contentMetadata["serviceType"] == "GB":
                                contact = cab.getContact(user)
                                auth = "\n Penulis : {}".format(str(contact.displayName))
                            else:
                                auth = "\n Penulis : {}".format(str(contact.displayName))
                                ret_ += auth
                            if "stickerId" in msg.contentMetadata:
                                stck = "\n Stiker : https://line.me/R/shop/detail/{}".format(str(msg.contentMetadata["packageId"]))
                                ret_ += stck
                            if "mediaOid" in msg.contentMetadata:
                                object_ = msg.contentMetadata["mediaOid"].replace("svc=myhome|sid=h|","")
                                if msg.contentMetadata["mediaType"] == "V":
                                    if msg.contentMetadata["serviceType"] == "GB":
                                        ourl = "\n Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                        murl = "\n Media URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(msg.contentMetadata["mediaOid"]))
                                    else:
                                        ourl = "\n Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                        murl = "\n Media URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(object_))
                                    ret_ += murl
                                else:
                                    if msg.contentMetadata["serviceType"] == "GB":
                                        ourl = "\n Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                    else:
                                        ourl = "\n Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                ret_ += ourl
                            if "text" in msg.contentMetadata:
                                dia = cab.getContact(user)
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan = 'Pengirim: '
                                xteam = str(dia.displayName)
                                pesan = ''
                                pesan2 = pesan+"@KRIS_MANIS\n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':dia.mid}
                                zx2.append(zx)
                                kata = "\n Tulisan : {}".format(str(msg.contentMetadata["text"]))
                                purl = "\n Post URL : {}".format(str(msg.contentMetadata["postEndUrl"]).replace("line://","https://line.me/R/"))
                                ret_ += purl
                                ret_ += kata
                                zxc += pesan2
                                pesan = xpesan + zxc + ret_ + ""
                                cab.sendMessage(kirim, pesan, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)

        if fast.type == 65:
            if Cyber['UnsendPesan'] == True:
                try:
                    you = fast.param1
                    msg.id = fast.param2
                    user = msg._from
                    if msg.id in msg_dict:
                        if msg_dict[msg.id]["pelaku"]:
                            pelaku = cab.getContact(msg_dict[msg.id]["pelaku"])
                            nama = pelaku.displayName
                            dia = "Detect Pesan Terhapus\n"
                            dia += "\n1. Name : " + nama
                            dia += "\n2. Taken : {}".format(str(msg_dict[msg.id]["createdTime"]))
                            dia += "\n3. Pesannya : {}".format(str(msg_dict[msg.id]["rider"]))
                            cab.mentionWithkris(you,user," Nah","\n\n" +str(dia))
                            #cab.mentionWithkris(you,user," Nah","")
                            cab.sendMessage(you, str(dia))
                            cab.sendImage(you, msg_dict[msg.id]["data"]) 
                            del msg_dict[msg.id]
                            
                except:
                    you = fast.param1 
                    msg_id = fast.param2 
                    if msg_id in msg_dict: 
                        if msg_dict[msg_id]["pelaku"]: 
                            ginfo = cab.getGroup(you) 
                            adekris = cab.getContact(msg_dict[msg_id]["pelaku"]) 
                            ret_ = "╭━━━╦════╦━━━━╮\n▶[Pesan Dihapus ]◀\n╰━━━╩━━━━╩━━━━╯\n\n╭══════════════╮" 
                            ret_ += "\n┣[]► Pengirim : {}".format(str(adekris.displayName)) 
                            ret_ += "\n┣[]► Nama Grup : {}".format(str(ginfo.name)) 
                            ret_ += "\n┣[]► Taken : {}".format(str(msg_dict[msg_id]["createdTime"]))
                            ret_ += "\n┣[]► Pesannya : {}".format(str(msg_dict[msg_id]["rider"]))+ "\n╰━━━╩━━━━╩━━━━╯"
                            cab.sendMessage(you, str(ret_)) 
                            cab.sendImage(you, msg_dict[msg_id]["data"]) 
                            del msg_dict[msg_id] 
                  #cab.sendMessage(you, "Return")

#        if fast.type == 65: 
#            if wait["unsend"] == True: 
#                try: 
#                    at = fast.param1 
#                    msg_id = fast.param2 
#                    if msg_id in msg_dict: 
#                        if msg_dict[msg_id]["from"]: 
#                        ginfo = cab.getGroup(at) 
#                        adekris = cab.getContact(msg_dict[msg_id]["from"]) 
#                        ret_ = "╭━━━╦════╦━━━━╮\n▶[Sticker Dihapus ]◀\n╰━━━╩━━━━╩━━━━╯\n\n╭══════════════╮" 
#                        ret_ += "┣[]► Pengirim : {}".format(str(adekris.displayName)) 
#                        ret_ += "\n┣[]► Nama Grup : {}".format(str(ginfo.name)) 
#                        ret_ += "\n┣[]► Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"]))) 
#                        ret_ += "{}".format(str(msg_dict[msg_id]["text"])) 
#                        cab.sendMessage(at, str(ret_)) 
#                        cab.sendImage(at, msg_dict[msg_id]["data"]) 
#                        del msg_dict[msg_id] 
#                except Exception as e: 
#                    print(e)

        if fast.type in [25,26]:
            msg = fast.message
            user = msg._from
            kirim = msg.to
            if msg.contentType == 7:
                if Cyber['IDSticker'] == True:
                    stk_id = msg.contentMetadata['STKID']
                    stk_ver = msg.contentMetadata['STKVER']
                    pkg_id = msg.contentMetadata['STKPKGID']
                    filler = "STICKER CHECKS\nSTKID : %s\nSTKPKGID : %s\nSTKVER : %s\n\nTHIS IS LINK\n\nline://shop/detail/%s" % (stk_id,pkg_id,stk_ver,pkg_id)
                    cab.mentionWithkris(kirim,user,"My Code Sticker\n","" + "\n\n" + str(filler))
                else:
                    pass

        if fast.type == 25 or fast.type == 26:
            msg = fast.message
            user = msg._from
            kirim = msg.to
            if msg.contentType == 1:
              if Cyber['Upfoto'] == True:
                if user in Owner:
                    path = cab.downloadObjectMsg(msg.id)
                    cab.updateProfilePicture(path)
                    cab.mentionWithkris(kirim,user," Update Picture Success ","")
                    Cyber['Upfoto'] = False

        if fast.type == 25 or fast.type == 26:
            msg = fast.message
            user = msg._from
            kirim = msg.to
            if msg.contentType == 1:
              if Cyber['UpfotoBot'] == True:
                if user in krisFatner or user in Cyber["Admin"]:
                    path1 = cab1.downloadObjectMsg(msg.id)
                    path2 = cab2.downloadObjectMsg(msg.id)
                    path3 = cab3.downloadObjectMsg(msg.id)
                    cab1.updateProfilePicture(path1)
                    cab2.updateProfilePicture(path2)
                    cab3.updateProfilePicture(path3)
                    cab1.mentionWithkris(kirim,user," Update Picture Success ","")
                    cab2.mentionWithkris(kirim,user," Update Picture Success ","")
                    cab3.mentionWithkris(kirim,user," Update Picture Success ","")
                    Cyber['UpfotoBot'] = False

        if fast.type == 25 or fast.type == 26:
            msg = fast.message
            user = msg._from
            kirim = msg.to
            if msg.contentType == 1:
              if Cyber['UpfotoGroup'] == True:
                if user in krisFatner or user in Cyber["Admin"]:
                    path = cab.downloadObjectMsg(msg.id)
                    cab.updateGroupPicture(kirim, path)
                    cab.mentionWithkris(kirim,user," Update Picture Grup Success ","")
                    Cyber['UpfotoGroup'] = False

        if fast.type in [25,26]:
          if Cyber['Contact'] == True:
              msg = fast.message
              user = msg._from
              kirim = msg.to
              if msg.contentType == 13:
                if 'displayName' in msg.contentMetadata:
                    contact = cab.getContact(msg.contentMetadata["mid"])
                    try:
                        cover = cab.getProfileCoverURL(user)
                    except:
                        cover = ""
                    cab.sendMessage(kirim,"Nama:\n" + msg.contentMetadata["displayName"] + "\n\nMid:\n" + msg.contentMetadata["mid"] + "\n\nBio:\n" + contact.statusMessage + "\n\nPicture URL:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\nCover URL:\n" + str(cover))
                else:
                    contact = cab.getContact(msg.contentMetadata["mid"])
                    try:
                        cover = cab.getProfileCoverURL(user)
                    except:
                        cover = ""
                    cab.sendText(kirim,"Nama:\n" + contact.displayName + "\n\nMid:\n" + msg.contentMetadata["mid"] + "\n\nBio:\n" + contact.statusMessage + "\n\nPicture URL\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\nCover URL:\n" + str(cover))

        if fast.type == 25 or fast.type == 26:
            msg = fast.message
            user = msg._from
            kirim = msg.to
            if msg.contentType == 13:
                try:
                    if user in krisFatner or user in Cyber["Admin"]:
                      if Cyber["Ban"] == True:
                        if msg.contentMetadata["mid"] in Cyber["Blacklist"]:
                            name = msg.contentMetadata["displayName"]
                            cab.sendMessage(kirim, name + str(" Sudah di daftar Blacklist"))
                            Cyber['Ban'] = False
                        else:
                            Cyber["Blacklist"][msg.contentMetadata["mid"]] = True
                            name = msg.contentMetadata["displayName"]
                            cab.sendMessage(kirim, name + str(" Added in Blacklist"))
                            Cyber['Ban'] = False
                      if Cyber["Unban"] == True:
                        if msg.contentMetadata["mid"] in Cyber["Blacklist"]:
                            del Cyber["Blacklist"][msg.contentMetadata["mid"]]
                            name = msg.contentMetadata["displayName"]
                            cab.sendMessage(kirim, name + str(" Succes dellete in Blacklist"))
                            Cyber['Unban'] = False
                        else:
                            name = msg.contentMetadata["displayName"]
                            cab.sendMessage(kirim, name + str(" Nothing in Blacklist"))
                            Cyber['Unban'] = False
                      if Cyber["Adminadd"] == True:
                        if msg.contentMetadata["mid"] in Cyber["Admin"]:
                            name = msg.contentMetadata["displayName"]
                            cab.sendMessage(kirim, name + str(" Sudah di daftar Admin"))
                            Cyber['Adminadd'] = False
                        else:
                            Cyber["Admin"][msg.contentMetadata["mid"]] = True
                            name = msg.contentMetadata["displayName"]
                            cab.sendMessage(kirim, name + str(" Added in Admin"))
                            Cyber['Adminadd'] = False
                      if Cyber["AdminDel"] == True:
                        if msg.contentMetadata["mid"] in Cyber["Admin"]:
                            del Cyber["Admin"][msg.contentMetadata["mid"]]
                            name = msg.contentMetadata["displayName"]
                            cab.sendMessage(kirim, name + str(" Succes dellete in Admin"))
                            Cyber['AdminDel'] = False
                        else:
                            name = msg.contentMetadata["displayName"]
                            cab.sendMessage(kirim, name + str(" Nothing in Admin"))
                            Cyber['AdminDel'] = False
                except Exception as error:
                    cab.sendText(kirim, str(error))

        if fast.type == 25 or fast.type == 26:
          if Cyber['Invite'] == True:
            msg = fast.message
            user = msg._from
            kirim = msg.to
            if msg.contentType == 13:
                if user in krisFatner or user in Cyber["Admin"]:
                    _name = msg.contentMetadata["displayName"]
                    invite = msg.contentMetadata["mid"]
                    groups = cab.getGroup(kirim)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            cab.sendText(msg.to, _name + " Sudah Berada DiGrup Ini")
                        else:
                            targets.append(invite)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            try:
                                cab.findAndAddContactsByMid(target)
                                cab.inviteIntoGroup(kirim,[target])
                                cab.sendText(kirim,"Invite " + _name + "\nSUCCESS..")
                                Cyber['Invite'] = False
                                break
                            except:             
                                 cab.sendText(kirim, 'Contact error')
                                 Cyber['Invite'] = False
                                 break

        if fast.type == 25 or fast.type == 26:
          if Cyber['Steal'] == True:
            msg = fast.message
            user = msg._from
            kirim = msg.to
            if msg.contentType == 13:
                if user in krisFatner or user in Cyber["Admin"]:
                    _name = msg.contentMetadata["displayName"]
                    copy = msg.contentMetadata["mid"]
                    groups = cab.getGroup(kirim)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            print ("[Target] Stealed")
                            break             
                        else:
                            targets.append(copy)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            try:
                                contact = cab.getContact(target)
                                cab.sendText(kirim,"Nama :\n" + msg.contentMetadata["displayName"] + "\n\nBio :\n" + contact.statusMessage+ "\n\nMid :\n" + msg.contentMetadata["mid"] + "\n\nSteal Succes..")
                                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                                cab.sendImageWithURL(kirim,image)
                                cover = cab.getProfileCoverURL(target)
                                cab.sendImageWithURL(kirim, cover)
                                Cyber['Steal'] = False
                                break                     
                            except:             
                                 cab.sendText(kirim, 'Contact error')
                                 Cyber['Steal'] = False
                                 break

        if fast.type == 25 or fast.type == 26:
          if Cyber['KillOn'] == True:
            msg = fast.message
            user = msg._from
            kirim = msg.to
            if msg.contentType == 13:
                if user in krisFatner or user in Cyber["Admin"]:
                    _name = msg.contentMetadata["displayName"]
                    copy = msg.contentMetadata["mid"]
                    groups = cab.getGroup(kirim)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            print ("[Target] Kick Via Contact")
                            break             
                        else:
                            targets.append(copy)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            if target not in krisFatner:
                                try:
                                    cab.kickoutFromGroup(kirim,[target])
                                    Cyber['KillOn'] = False
                                    break
                                except:             
                                     cab.sendText(kirim, 'Target Not Found')
                                     Cyber['KillOn'] = False
                                     break

        if fast.type == 25 or fast.type == 26:
          if Cyber['Gift'] == True:
            msg = fast.message
            user = msg._from
            kirim = msg.to
            if msg.contentType == 13:
                if user in krisFatner or user in Cyber["Admin"]:
                    _name = msg.contentMetadata["displayName"]
                    copy = msg.contentMetadata["mid"]
                    groups = cab.getGroup(kirim)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            print ("[Target] Send Gift")
                            break             
                        else:
                            targets.append(copy)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            try:
                                cab.sendMessage(target, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58','PRDTYPE': 'THEME','MSGTPL': '12'}, contentType = 9)
                                cab1.sendMessage(target, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58','PRDTYPE': 'THEME','MSGTPL': '12'}, contentType = 9)
                                cab2.sendMessage(target, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58','PRDTYPE': 'THEME','MSGTPL': '12'}, contentType = 9)
                                cab3.sendMessage(target, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58','PRDTYPE': 'THEME','MSGTPL': '12'}, contentType = 9)
                                Cyber['Gift'] = False
                                break
                            except:             
                                 cab.sendText(kirim, 'Target Error')
                                 Cyber['Gift'] = False
                                 break

        if fast.type == 25 or fast.type == 26:
          if Cyber["Mic"] == True:
            msg = fast.message
            user = msg._from
            kirim = msg.to
            if msg.contentType == 13:
                if user in krisFatner or user in Cyber["Admin"]:
                    _name = msg.contentMetadata["displayName"]
                    copy = msg.contentMetadata["mid"]
                    groups = cab.getGroup(kirim)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            print ("[Target] Mimic Add")
                            break             
                        else:
                            targets.append(copy)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            try:
                                Mozilla["mimic"]["target"][target] = True
                                cab.sendText(kirim,"Target ditambahkan!")
                                Squas['Mic'] = False
                                break
                            except:             
                                 cab.sendText(kirim, 'Silahkan untuk on kan kembali & Send Contact Again\nKami akan memuat ulang program')
                                 break

        if fast.type == 25 or fast.type == 26:
          if Cyber["MicDel"] == True:
            msg = fast.message
            user = msg._from
            kirim = msg.to
            if msg.contentType == 13:
                if user in krisFatner or user in Cyber["Admin"]:
                    _name = msg.contentMetadata["displayName"]
                    copy = msg.contentMetadata["mid"]
                    groups = cab.getGroup(kirim)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            print ("[Target] Mimic Add")
                            break             
                        else:
                            targets.append(copy)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            try:
                                del Mozilla["mimic"]["target"][target]
                                cab.sendText(kirim,"Target is Dellete!")
                                Cyber['MicDel'] = False
                                break
                            except:             
                                 cab.sendText(kirim, 'Silahkan untuk on kan kembali & Send Contact Again\nKami akan memuat ulang program')
                                 break

        if fast.type == 25 or fast.type == 26:
          if Cyber['Copy'] == True:
            msg = fast.message
            user = msg._from
            kirim = msg.to
            if msg.contentType == 13:
                if user in krisFatner or user in Cyber["Admin"]:
                    _name = msg.contentMetadata["displayName"]
                    copy = msg.contentMetadata["mid"]
                    groups = cab.getGroup(kirim)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            print ("[Target] Stealed")
                            break             
                        else:
                            targets.append(copy)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            try:
                                cab.cloneContactProfile(target)
                                cab.sendText(kirim, "Copy Contact Success")
                                Cyber['Copy'] = False
                                break
                            except:             
                                 cab.sendText(kirim, "Contact Error")
                                 Cyber['Copy'] = False
                                 break
                                 
                                 
#======= AUTO TAG & CHAT BATAS SCRIP ========
        if fast.type == 26:
            msg = fast.message
            user = msg._from
            kirim = msg.to
            if msg.contentType == 0 and user not in mid and msg.toType == 2:
                if "MENTION" in msg.contentMetadata.keys() != None:
                    if Cyber['AutoRespon'] == True:
                        contact = cab.getContact(user)
                        cName = contact.displayName
                        balas = [cName + "\n" + str(Cyber['MentionText'])]
                        ret_ = "" + random.choice(balas)
                        name = re.findall(r'@(\w+)', msg.text)
                        mention = ast.literal_eval(msg.contentMetadata["MENTION"])
                        mentionees = mention['MENTIONEES']
                        for mention in mentionees:
                              if mention['M'] in mid:
                                  cab.mentionWithkris(kirim,user,"","" +str(ret_))
                                  break

        if fast.type == 26:
            msg = fast.message
            user = msg._from
            kirim = msg.to
            if msg.contentType == 0 and user not in krisFatner or user not in Cyber["Admin"]:
                if "MENTION" in msg.contentMetadata.keys() != None:
                    if Cyber['KickRespon'] == True:
                        contact = cab.getContact(user)
                        cName = contact.displayName
                        balas = [cName + "Dont Tag Me","Sorry Dont Tag Me"]
                        ret_ = "" + random.choice(balas)
                        name = re.findall(r'@(\w+)', msg.text)
                        mention = ast.literal_eval(msg.contentMetadata["MENTION"])
                        mentionees = mention['MENTIONEES']
                        for mention in mentionees:
                              if mention['M'] in mid:
                                  cab.mentionWithkris(kirim,user,"","" +str(ret_))
                                  cab.kickoutFromGroup(kirim,[user])
                                  break

        if fast.type == 25 or fast.type == 26:
          if Cyber['SpamInvite'] == True:
            msg = fast.message
            user = msg._from
            kirim = msg.to
            if msg.contentType == 13:
                if user in krisFatner or user in Cyber["Admin"]:
                    korban = msg.contentMetadata["displayName"]
                    invite = msg.contentMetadata["mid"]
                    groups = cab.getGroup(kirim)
                    pending = groups.invitee
                    targets = []
                    for x in groups.members:
                        if korban in x.displayName:
                            cab.sendText(kirim, korban + " Sudah Berada DiGrup Ini")
                        else:
                            targets.append(invite)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            try:
                                cab.findAndAddContactsByMid(target)
                                cab1.findAndAddContactsByMid(target)
                                cab2.findAndAddContactsByMid(target)
                                cab3.findAndAddContactsByMid(target)
                                cab.createGroup("SPAM GROUP",[target]) # KALAU MAU BUAT BANYAK SILAHKAN TAMBAHIN SESUKA KALIAN :>
                                cab.createGroup("SPAM GROUP",[target]) # HANYA SPAM VIA CONTACT
                                cab.createGroup("SPAM GROUP",[target])
                                cab1.createGroup("SPAM GROUP",[target])
                                cab1.createGroup("SPAM GROUP",[target])
                                cab1.createGroup("SPAM GROUP",[target])
                                cab2.createGroup("SPAM GROUP",[target])
                                cab2.createGroup("SPAM GROUP",[target])
                                cab2.createGroup("SPAM GROUP",[target])
                                cab3.createGroup("SPAM GROUP",[target])
                                cab3.createGroup("SPAM GROUP",[target])
                                cab3.createGroup("SPAM GROUP",[target])
                                cab.sendText(kirim,"Spam Invite ke " + korban + "\nSUCCESS..")
                                Cyber['SpamInvite'] = False
                            except:             
                                 cab.sendText(kirim, 'Contact error')
                                 Cyber['SpamInvite'] = False
                                 break


#------------------- ( 3 ) ------------------------- PEMBATAS SCRIP ------------------------------------------------#

        if fast.type == 25 or fast.type == 26:
            msg = fast.message
            text = msg.text
            krisText = msg.text
            msg_id = msg.id
            kirim = msg.to           
            user = msg._from
            if msg.toType == 0 or msg.toType == 2:
                if msg.toType == 0:
                    to = kirim
                elif msg.toType == 2:
                    to = kirim
                if msg.contentType == 0:
                    if Cyber["autoRead"] == True:
                        cab.sendChatChecked(0, msg_id)

                    elif krisText is None:
                        return
                    else:               
                        if krisText.lower() == 'PROSES TRANSISI':
                            cab.sendMessage(0, user)

                        elif krisText.lower() == "me":
                            if user in krisFatner or user in Cyber["Admin"]:
                                cab.sendMessage(kirim, None, contentMetadata={'mid': mid}, contentType=13)
                                cab.mentionWithkris(kirim,mid," Hay","")

                        elif krisText.lower() == "help":
                            if user in krisFatner or user in Cyber["Admin"]:
                                 cab.sendMessage(kirim, str(Help))

                        elif krisText.lower() == "speed":
                            if user in krisFatner or user in Cyber["Admin"]:
                                no = time.time()
                                cab.sendText("u35459f1e84ad208cc56025c259cb1628", ' ')
                                elapsed_time = time.time() - no
                                cab.sendText(kirim, "%s" % (elapsed_time))
                                no1 = time.time()
                                cab1.sendText("u35459f1e84ad208cc56025c259cb1628", ' ')
                                elapsed_time = time.time() - no1
                                cab1.sendText(kirim, "%s" % (elapsed_time))
                                no2 = time.time()
                                cab2.sendText("u35459f1e84ad208cc56025c259cb1628", ' ')
                                elapsed_time = time.time() - no2
                                cab2.sendText(kirim, "%s" % (elapsed_time))
                                no3 = time.time()
                                cab3.sendText("u35459f1e84ad208cc56025c259cb1628", ' ')
                                elapsed_time = time.time() - no3
                                cab3.sendText(kirim, "%s" % (elapsed_time))

                        elif krisText.lower() == "responsename":
                            if user in krisFatner or user in Cyber["Admin"]:
                                team1 = cab.getContact(mid).displayName
                                team2 = cab1.getContact(krMID1).displayName
                                team3 = cab2.getContact(krMID2).displayName
                                team4 = cab3.getContact(krMID3).displayName
                                owner = "u35459f1e84ad208cc56025c259cb1628"
                                cab.mentionWithkris(kirim,owner," Ready On ","" + str(" ("+team1+")"))
                                cab1.mentionWithkris(kirim,owner," Ready On ","" + str(" ("+team2+")"))
                                cab2.mentionWithkris(kirim,owner," Ready On ","" + str(" ("+team3+")"))
                                cab3.mentionWithkris(kirim,owner," Ready On ","" + str(" ("+team4+")"))

                        elif krisText.lower() == "my bot":
                            if user in krisFatner or user in Cyber["Admin"]:
                               cab.sendMessage(kirim, None, contentMetadata={'mid': mid}, contentType=13)
                               cab.sendMessage(kirim, None, contentMetadata={'mid': krMID1}, contentType=13)
                               cab.sendMessage(kirim, None, contentMetadata={'mid': krMID2}, contentType=13)
                               cab.sendMessage(kirim, None, contentMetadata={'mid': krMID3}, contentType=13)

                        elif krisText.lower() == "my team":
                            if user in krisFatner or user in Cyber["Admin"]:
                                kris = ""
                                Fatner = ""
                                wa = 0
                                wi = 0
                                for m_id in Owner:
                                    wa = wa + 1
                                    end = '\n'
                                    kris += str(wa) + ". " +cab.getContact(m_id).displayName + "\n"
                                for m_id in Cyber["Admin"]:
                                    wi = wi + 1
                                    end = '\n'
                                    Fatner += str(wi) + ". " +cab.getContact(m_id).displayName + "\n"
                                cab.sendText(kirim,"kris Fatner\n\nOwner:\n"+kris+"\nAdmin:\n"+Fatner+"\n( %s ) TEAM CAB Fatner" %(str(len(Owner)+len(Cyber["Admin"]))))                                

                        elif krisText.lower() == "masuk":
                            if user in krisFatner or user in Cyber["Admin"]:
                                X = cab.getGroup(kirim)
                                X.preventedJoinByTicket = False
                                cab.updateGroup(X)
                                invsend = 0
                                Kris = cab.reissueGroupTicket(kirim)
                                cab1.acceptGroupInvitationByTicket(kirim,Kris)
                                cab2.acceptGroupInvitationByTicket(kirim,Kris)
                                cab3.acceptGroupInvitationByTicket(kirim,Kris)
                                X = cab.getGroup(kirim)
                                X.preventedJoinByTicket = True
                                cab.updateGroup(X)
                                X.preventedJoinByTicket(X)
                                cab.updateGroup(X)

                        elif krisText.lower() == "@bye":
                            if user in krisFatner or user in Cyber["Admin"]:
                                ginfo = cab.getGroup(kirim)
                                owner = "u35459f1e84ad208cc56025c259cb1628"
                                cab1.mentionWithkris(kirim,owner," Oke ","\n Good Bye" + str(" ("+ginfo.name+")"))
                                cab3.leaveGroup(kirim)
                                cab2.leaveGroup(kirim)
                                cab1.leaveGroup(kirim)
                                cab.leaveGroup(kirim)

                        elif krisText.lower() == "leaveall grup":
                            if user in krisFatner or user in Cyber["Admin"]:
                                gid = cab.getGroupIdsJoined()
                                gid = cab1.getGroupIdsJoined()
                                gid = cab2.getGroupIdsJoined()
                                gid = cab3.getGroupIdsJoined()
                                for i in gid:
                                    cab.leaveGroup(i)
                                    cab1.leaveGroup(i)
                                    cab2.leaveGroup(i)
                                    cab3.leaveGroup(i)
                                    print ("Kicker Leave All group")

                        elif krisText in ["Kick on"]:
                            if user in krisFatner or user in Cyber["Admin"]:
                                Cyber["KickOn"] = True
                                cab.sendText(kirim,"Status:\n{''cancel'':0,''kick'':1}")
                        elif krisText in ["Kick off"]:
                            if user in krisFatner or user in Cyber["Admin"]:
                                Cyber["KickOn"] = False
                                cab.sendText(kirim,"Status:\n{''cancel'':0,''kick'':0}")

                        elif "Kickall" in krisText:
                            if user in krisFatner or user in Cyber["Admin"]:
                              if msg.toType == 2:
                                if Cyber["KickOn"]:
                                    _name = msg.text.replace("Kickall","")
                                    gs = cab.getGroup(kirim)
                                    targets = []
                                    for g in gs.members:
                                        if _name in g.displayName:
                                            targets.append(g.mid)
                                    if targets == []:
                                        cab.sendText(kirim,"Target Not found.")
                                    else:
                                        for target in targets:
                                          if target not in krisFatner and target not in Cyber["Admin"]:
                                            try:
                                                klist=[cab,cab1,cab2,cab3]
                                                kicker=random.choice(klist)
                                                kicker.kickoutFromGroup(kirim,[target])
                                                print (kirim,[g.mid])
                                            except Exception as error:
                                                cab.sendText(kirim, str(error))

                        elif "Spam " in krisText:
                            if user in krisFatner or user in Cyber["Admin"]:
                                txt = krisText.split(" ")
                                jmlh = int(txt[2])
                                teks = krisText.replace("Spam "+str(txt[1])+" "+str(jmlh)+" ","")
                                tulisan = jmlh * (teks+"\n")
                                if txt[1] == "on":
                                    if jmlh <= 500:
                                       for x in range(jmlh):
                                           cab.sendText(kirim, teks)
                                    else:
                                       cab.sendText(kirim, "Maksimal 500 SpamTeks!")
                                elif txt[1] == "off":
                                    if jmlh <= 500:
                                        cab.sendText(kirim, tulisan)
                                    else:
                                        cab.sendText(kirim, "Maksimal 500 SpamTeks!")

                        elif "Cekmid: " in krisText:
                            if user in krisFatner or user in Cyber["Admin"]:
                                krisna = krisText.replace("Cekmid: ","")
                                cab.sendMessage(kirim, None, contentMetadata={'mid': krisna}, contentType=13)
                                contact = cab.getContact(krisna)
                                ganteng = cab.getProfileCoverURL(krisna)
                                path = str(ganteng)
                                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                                try:
                                    cab.sendText(kirim,"Nama :\n" + contact.displayName + "\n\nBio :\n" + contact.statusMessage)
                                    cab.sendText(kirim,"Profile Picture " + contact.displayName)
                                    cab.sendImageWithURL(kirim,image)
                                    cab.sendText(kirim,"Cover Picture " + contact.displayName)
                                    cab.sendImageWithURL(kirim,path)
                                except:
                                    pass

                        elif ("Banlock " in krisText):
                            if user in krisFatner or user in Cyber["Admin"]:
                                key = eval(msg.contentMetadata["MENTION"])
                                key["MENTIONEES"][0]["M"]
                                targets = []
                                for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                                for target in targets:
                                    try:
                                        Cyber["Blacklist"][target] = True
                                        cab.sendText(kirim,"Succes Banned ")
                                    except:
                                        pass

                        elif krisText.lower() == "banlist":
                            if user in krisFatner or user in Cyber["Admin"]:
                                if Cyber["Blacklist"] == {}:
                                    cab.sendText(kirim,"Nothing in Blacklist")
                                else:
                                    mc = "Daftar Blacklist "
                                    num=1
                                    ragets = cab.getContacts(Cyber["Blacklist"])
                                    for mi_d in ragets:
                                        mc+="\n%i. %s" % (num, mi_d.displayName)
                                        num=(num+1)
                                    mc+="\n\n Total %i Blacklist " % len(ragets)
                                    cab.sendText(kirim, mc)

                        elif krisText in ["Contact ban"]:
                            if user in krisFatner or user in Cyber["Admin"]:
                              if Cyber["Blacklist"] == {}:
                                  cab.sendText(kirim,"Tidak Ada Blacklist")
                              else:
                                  cab.sendText(kirim,"Contact Blacklist")
                                  h = ""
                                  for i in Cyber["Blacklist"]:
                                      h = cab.getContact(i)
                                      cab.sendMessage(kirim, None, contentMetadata={'mid': i}, contentType=13)

                        elif krisText in ["Clear ban"]:
                            if user in krisFatner or user in Cyber["Admin"]:
                                Cyber["Blacklist"] = {}
                                cab.sendText(kirim,"Succes clear Blacklist is nothing??")
                                print ("Clear Ban")

                        elif krisText in ["Ban:on"]:
                            if user in krisFatner or user in Cyber["Admin"]:
                                Cyber["Ban"] = True
                                cab.sendText(kirim,"Send Contact to BlackList..")
                        elif krisText in ["Unban:on"]:
                            if user in krisFatner or user in Cyber["Admin"]:
                                Cyber["Unban"] = True
                                cab.sendText(kirim,"Send Contact to UnBlackList..")

                        elif krisText.lower() == 'link on':
                            if user in krisFatner or user in Cyber["Admin"]:
                                if msg.toType == 2:
                                    group = cab.getGroup(kirim)
                                    group.preventedJoinByTicket = False
                                    cab.updateGroup(group)

                        elif krisText.lower() == 'link off':
                            if user in krisFatner or user in Cyber["Admin"]:
                                if msg.toType == 2:
                                    group = cab.getGroup(kirim)
                                    group.preventedJoinByTicket = True
                                    cab.updateGroup(group)

                        elif krisText.lower() == 'gurl':
                          if user in krisFatner or user in Cyber["Admin"]:
                            if msg.toType == 2:
                                grup = cab.getGroup(kirim)
                                if grup.preventedJoinByTicket == False:
                                    set = cab.reissueGroupTicket(kirim)
                                    cab.sendMessage(kirim, "Group Ticket : \nhttps://line.me/R/ti/g/{}".format(str(set)))
                                else:
                                    cab.sendMessage(kirim, "Ketik Link on Dulu kaka")

                        elif krisText.lower() == 'gcreator':
                            if user in krisFatner or user in Cyber["Admin"]:
                                try:
                                    group = cab.getGroup(kirim)
                                    GS = group.creator.mid
                                    cab.sendMessage(kirim, None, contentMetadata={'mid': GS}, contentType=13)
                                    cab.mentionWithkris(kirim,GS,"Group Creator","")
                                    contact = cab.getContact(GS.mid)
                                except:
                                    W = group.members[0].mid
                                    cab.sendMessage(kirim, None, contentMetadata={'mid': W}, contentType=13)
                                    cab.mentionWithkris(kirim,W,"Group Creator","")

                        elif "invite gcreator" == krisText:
                            if user in krisFatner or user in Cyber["Admin"]:
                                try:
                                    group = cab.getGroup(kirim)
                                    GS = group.creator.mid
                                    cab.sendMessage(kirim, None, contentMetadata={'mid': GS}, contentType=13)
                                    cab.mentionWithkris(kirim,GS,"Group Creator","")
                                    cab.findAndAddContactsByMid(GS)
                                    cab.inviteIntoGroup(kirim,[GS])
                                    cab.mentionWithkris(kirim,user,"Invite Done","")
                                    contact = cab.getContact(GS.mid)
                                except:
                                    W = group.members[0].mid
                                    cab.sendMessage(kirim, None, contentMetadata={'mid': W}, contentType=13)
                                    cab.mentionWithkris(kirim,W,"Group Creator","")
                                    cab.findAndAddContactsByMid(W)
                                    cab.inviteIntoGroup(kirim,[W])
                                    cab.mentionWithkris(kirim,user,"Invite Done","")

                        elif krisText.lower() == 'ginfo':
                            if user in krisFatner or user in Cyber["Admin"]:
                                group = cab.getGroup(kirim)
                                try:
                                    gCreator = group.creator.displayName
                                except:
                                    gCreator = "Tidak ditemukan"
                                if group.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(group.invitee))
                                if group.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(line.reissueGroupTicket(group.id)))
                                cuki = "INFO GRUP"
                                cuki += "\nNama Group : {}".format(str(group.name))
                                cuki += "\nID Group :\n? {}".format(group.id)
                                cuki += "\nPembuat : {}".format(str(gCreator))
                                cuki += "\nJumlah Member : {}".format(str(len(group.members)))
                                cuki += "\nJumlah Pending : {}".format(gPending)
                                cuki += "\nGroup Qr : {}".format(gQr)
                                cuki += "\nGroup Ticket : {}".format(gTicket)
                                cab.sendMessage(kirim, str(cuki))

                        elif krisText in ["Memberlist"]:
                            if user in krisFatner or user in Cyber["Admin"]:
                                kontak = cab.getGroup(kirim)
                                group = kontak.members
                                num=1
                                msgs="LIST MEMBER\n"
                                for ids in group:
                                    msgs+="\n%i. %s" % (num, ids.displayName)
                                    num=(num+1)
                                msgs+="\n\nTOTAL MEMBER ( %i )" % len(group)
                                cab.sendText(kirim, msgs)

                        elif krisText in ["Blocklist"]:
                            if user in krisFatner or user in Cyber["Admin"]:
                                blockedlist = cab.getBlockedContactIds()
                                kontak = cab.getContacts(blockedlist)
                                num=1
                                msgs="My Blocked\n"
                                for ids in kontak:
                                    msgs+="\n%i. %s" % (num, ids.displayName)
                                    num=(num+1)
                                msgs+="\n\nTotal Blocked : %i" % len(kontak)
                                cab.sendText(kirim, msgs)

                        elif krisText in ["Friendlist mid"]: 
                            if user in krisFatner or user in Cyber["Admin"]:
                                gruplist = cab.getAllContactIds()
                                kontak = cab.getContacts(gruplist)
                                num=1
                                msgs="List Mid Friend\n"
                                for ids in kontak:
                                    msgs+="\n%i. %s" % (num, ids.mid)
                                    num=(num+1)
                                msgs+="\n\nTotal Mid Friend : %i" % len(kontak)
                                cab.sendText(kirim, msgs)

                        elif "Grup id" in krisText:
                            if user in krisFatner or user in Cyber["Admin"]:
                                saya = krisText.replace('Grup id','')
                                gid = cab.getGroup(kirim)
                                cab.sendText(kirim, "ID Grup : \n" + gid.id + "\nName Grup : \n" + str(gid.name))

                        elif 'mid ' in krisText.lower():
                          if user in krisFatner or user in Cyber["Admin"]:
                              try:
                                  key = eval(msg.contentMetadata["MENTION"])
                                  u = key["MENTIONEES"][0]["M"]
                                  cmid = cab.getContact(u).mid
                                  cab.sendText(kirim, str(cmid))
                              except Exception as e:
                                  cab.sendText(kirim, str(e))

                        elif "Profile" in krisText:
                            if user in krisFatner or user in Cyber["Admin"]:
                                key = eval(msg.contentMetadata["MENTION"])
                                key1 = key["MENTIONEES"][0]["M"]
                                contact = cab.getContact(key1)
                                cover = cab.getProfileCoverURL(key1)
                                path = str(cover)
                                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                                try:
                                    cab.sendText(kirim,"Nama :\n" + contact.displayName + "\n\nBio :\n" + contact.statusMessage)
                                    cab.sendImageWithURL(kirim,image)
                                    cab.sendImageWithURL(kirim,path)
                                except Exception as error:
                                    cab.sendMessage(kirim, str(error))

                        elif krisText.lower() == 'lurking on':
                            if user in krisFatner or user in Cyber["Admin"]:
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                if kirim in Cyber['readPoint']:
                                        try:
                                            del Cyber['readPoint'][kirim]
                                            del Cyber['readMember'][kirim]
                                            del Cyber['readTime'][kirim]
                                        except:
                                            pass
                                        Cyber['readPoint'][kirim] = msg.id
                                        Cyber['readMember'][kirim] = ""
                                        Cyber['readTime'][kirim] = datetime.now().strftime('%H:%M:%S')
                                        Cyber['ROM'][kirim] = {}
                                        with open('sider.json', 'w') as fp:
                                            json.dump(Cyber, fp, sort_keys=True, indent=4)
                                            cab.sendMessage(kirim,"Lurking already on")
                                else:
                                    try:
                                        del read['readPoint'][kirim]
                                        del read['readMember'][kirim]
                                        del read['readTime'][kirim]
                                    except:
                                        pass
                                    Cyber['readPoint'][kirim] = msg.id
                                    Cyber['readMember'][kirim] = ""
                                    Cyber['readTime'][kirim] = datetime.now().strftime('%H:%M:%S')
                                    Cyber['ROM'][kirim] = {}
                                    with open('sider.json', 'w') as fp:
                                        json.dump(Cyber, fp, sort_keys=True, indent=4)
                                        cab.sendMessage(kirim, "Set reading point:\n" + readTime)
                                        
                        elif krisText.lower() == 'lurking off':
                            if user in krisFatner or user in Cyber["Admin"]:
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                if kirim not in Cyber['readPoint']:
                                    cab.sendMessage(kirim,"Lurking already off..")
                                else:
                                    try:
                                            del Cyber['readPoint'][kirim]
                                            del Cyber['readMember'][kirim]
                                            del Cyber['readTime'][kirim]
                                    except:
                                          pass
                                    cab.sendMessage(kirim, "Delete reading point:\n" + readTime)
                
                        elif krisText.lower() == 'lurking reset':
                            if user in krisFatner or user in Cyber["Admin"]:
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                if kirim in Cyber["readPoint"]:
                                    try:
                                        Cyber["readPoint"][kirim] = True
                                        Cyber["readMember"][kirim] = {}
                                        Cyber["readTime"][kirim] = readTime
                                        Cyber["ROM"][kirim] = {}
                                    except:
                                        pass
                                    cab.sendMessage(kirim, "Reset reading point:\n" + readTime)
                                else:
                                    cab.sendMessage(kirim, "Lurking on dulu kaka..")
                                    
                        elif krisText.lower() == 'lurking read':
                            if user in krisFatner or user in Cyber["Admin"]:
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                if kirim in Cyber['readPoint']:
                                    if Cyber["ROM"][kirim].items() == []:
                                        cab.sendMessage(kirim,"[ Reader ]:\nNone")
                                    else:
                                        chiya = []
                                        for rom in Cyber["ROM"][kirim].items():
                                            chiya.append(rom[1])
                                        cmem = cab.getContacts(chiya) 
                                        zx = ""
                                        zxc = ""
                                        zx2 = []
                                        xpesan = 'Pembaca Pesan:\n'
                                    for x in range(len(cmem)):
                                        xname = str(cmem[x].displayName)
                                        pesan = ''
                                        pesan2 = pesan+"@KRIS_MANIS\n"
                                        xlen = str(len(zxc)+len(xpesan))
                                        xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                        zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                                        zx2.append(zx)
                                        zxc += pesan2
                                    text = xpesan+ zxc + "\nLurking time: \n" + readTime
                                    try:
                                        cab.sendMessage(kirim, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                    except Exception as error:
                                        print (error)
                                    pass
                                else:
                                    cab.sendMessage(kirim,"Lurking on dulu kaka ??")

                        elif krisText.lower() == 'sider on':
                            if user in krisFatner or user in Cyber["Admin"]:
                                try:
                                    del krisCctv['Point2'][kirim]
                                    del krisCctv['Point3'][kirim]
                                    del krisCctv['Point1'][kirim]
                                except:
                                    pass
                                krisCctv['Point2'][kirim] = msg.id
                                krisCctv['Point3'][kirim] = ""
                                krisCctv['Point1'][kirim]=True
                                cab.sendText(kirim,"Sider Set to On..")

                        elif krisText.lower() == 'sider off':
                            if user in krisFatner or user in Cyber["Admin"]:
                                if kirim in krisCctv['Point2']:
                                    krisCctv['Point1'][kirim]=False
                                    cab.sendText(kirim, krisCctv['Point3'][kirim])
                                else:
                                    cab.sendText(kirim, "Off not Going")

                        elif krisText.lower() == 'tagall':
                            if user in krisFatner or user in Cyber["Admin"]:
                                group = cab.getGroup(kirim)
                                nama = [contact.mid for contact in group.members]
                                nm1, nm2, nm3, nm4, nm5, jml = [], [], [], [], [], len(nama)
                                if jml <= 100:
                                    cab.mention(kirim, nama)
                                if jml > 100 and jml < 200:
                                    for i in range(0, 100):
                                        nm1 += [nama[i]]
                                    cab.mention(kirim, nm1)
                                    for j in range(101, len(nama)):
                                        nm2 += [nama[j]]
                                    cab.mention(kirim, nm2)
                                if jml > 200 and jml < 300:
                                    for i in range(0, 100):
                                        nm1 += [nama[i]]
                                    cab.mention(kirim, nm1)
                                    for j in range(101, 200):
                                        nm2 += [nama[j]]
                                    cab.mention(kirim, nm2)
                                    for k in range(201, len(nama)):
                                        nm3 += [nama[k]]
                                    cab.mention(kirim, nm3)
                                if jml > 300 and jml < 400:
                                    for i in range(0, 100):
                                        nm1 += [nama[i]]
                                    cab.mention(kirim, nm1)
                                    for j in range(101, 200):
                                        nm2 += [nama[j]]
                                    cab.mention(kirim, nm2)
                                    for k in range(201, len(nama)):
                                        nm3 += [nama[k]]
                                    cab.mention(kirim, nm3)
                                    for l in range(301, len(nama)):
                                        nm4 += [nama[l]]
                                    cab.mention(kirim, nm4)
                                if jml > 400 and jml < 501:
                                    for i in range(0, 100):
                                        nm1 += [nama[i]]
                                    cab.mention(kirim, nm1)
                                    for j in range(101, 200):
                                        nm2 += [nama[j]]
                                    cab.mention(kirim, nm2)
                                    for k in range(201, len(nama)):
                                        nm3 += [nama[k]]
                                    cab.mention(kirim, nm3)
                                    for l in range(301, len(nama)):
                                        nm4 += [nama[l]]
                                    cab.mention(kirim, nm4)
                                    for m in range(401, len(nama)):
                                        nm5 += [nama[m]]
                                    cab.mention(kirim, nm5)             
                                cab.sendText(kirim, "Jumlah Members :"+str(jml))

                        elif krisText in ["Welcome on"]:
                          if user in krisFatner or user in Cyber["Admin"]:
                            if user in krisFatner:
                                Cyber['Welcome'] = True
                                cab.sendText(kirim,"Cek Welcome Already ON")
                        elif krisText in ["Welcome off"]:
                          if user in krisFatner or user in Cyber["Admin"]:
                            if user in krisFatner:
                                Cyber['Welcome'] = False
                                cab.sendText(kirim,"Cek Welcome Already Off")

                        elif "changewelcome: " in krisText.lower():
                            if user in krisFatner or user in Cyber["Admin"]:
                                teks = krisText.split(": ")
                                data = krisText.replace(teks[0] + ": ","")
                                try:
                                    Cyber["WcText"] = data
                                    cab.sendText(kirim,"Name Welcome Change to:\n" +str("(" +data+ ")"))
                                except:
                                    cab.sendText(kirim,"Name Error")

                        elif krisText in ["Leave on"]:
                            if user in krisFatner or user in Cyber["Admin"]:
                                Cyber['Leave'] = True
                                cab.sendText(kirim,"Cek Leave Already ON")
                        elif krisText in ["Leave off"]:
                            if user in krisFatner or user in Cyber["Admin"]:
                                Cyber['Leave'] = False
                                cab.sendText(kirim,"Cek Leave Already Off")

                        elif "changeleave: " in krisText.lower():
                            if user in krisFatner or user in Cyber["Admin"]:
                                teks = krisText.split(": ")
                                data = krisText.replace(teks[0] + ": ","")
                                try:
                                    Cyber["LvText"] = data
                                    cab.sendText(kirim,"Name Leave Change to:\n" +str("(" +data+ ")"))
                                except:
                                    cab.sendText(kirim,"Name Error")

                        elif krisText.lower() == "runtime":
                            if user in krisFatner or user in Cyber["Admin"]:
                                eltime = time.time() - mulai                                
                                opn = " "+waktu(eltime)
                                cab.sendText(kirim,"Connect to kris Fatner\nBot Active\n" + opn)                

                        elif "Broadcast: " in krisText:
                            if user in krisFatner or user in Cyber["Admin"]:
                                bc = msg.text.replace("Broadcast: ","")
                                gid = cab.getGroupIdsJoined()
                                owner = "u35459f1e84ad208cc56025c259cb1628"
                                for i in gid:
                                    cab.mentionWithkris(i,owner," BROADCAST BY:","\n" + str(" ("+bc+")"))

                        elif "Contactbc: " in krisText:
                            if user in krisFatner or user in Cyber["Admin"]:
                                bc = msg.text.replace("Contactbc: ","")
                                gid = cab.getAllContactIds()
                                owner = "u35459f1e84ad208cc56025c259cb1628"
                                for i in gid:
                                    cab.mentionWithkris(i,owner," BROADCAST BY:","\n" + str(" ("+bc+")"))

                        elif "adminadd " in krisText.lower():
                            if user in krisFatner:
                                key = eval(msg.contentMetadata["MENTION"])
                                key["MENTIONEES"][0]["M"]
                                targets = []
                                for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                                for target in targets:
                                    if target in Cyber["Admin"]:
                                        cab.sendText(kirim, "Sudah Terdaftar di Admin")
                                    else:
                                        try:
                                            Cyber["Admin"][target] = True
                                            cab.sendText(kirim, "Terdaftar Menjadi Admin ")
                                        except Exception as e:
                                            cab.sendText(kirim, str(error))

                        elif "admindell " in krisText.lower():
                            if user in Owner:
                                key = eval(msg.contentMetadata["MENTION"])
                                key["MENTIONEES"][0]["M"]
                                targets = []
                                for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                                for target in targets:
                                    if target not in Cyber["Admin"]:
                                        cab.sendText(kirim, "Belum Terdaftar di Admin")
                                    else:
                                        try:
                                            del Cyber["Admin"][target]
                                            cab.sendText(kirim, "Succes Dihapus menjadi admin")
                                        except Exception as e:
                                            cab.sendText(kirim, str(error))

                        elif "changename: " in krisText.lower():
                            if user in krisFatner:
                                name = krisText.split(": ")
                                change = krisText.replace(name[0] + ": ","")
                                cll = cab.getProfile()
                                cll.displayName = change
                                cab.updateProfile(cll)
                                owner = "u35459f1e84ad208cc56025c259cb1628"
                                cab.mentionWithkris(kirim,owner," Update Name Success","\n Change to " + str(change))

                        elif "changebio: " in krisText.lower():
                            if user in krisFatner:
                                proses = krisText.split(": ")
                                teks = krisText.replace(proses[0] + ": ","")
                                no1 = cab.getProfile()
                                no1.statusMessage = teks
                                cab.updateProfile(no1)
                                cab.sendText(kirim,"My Bio Change To : " + teks)

                        elif "changenameall: " in krisText.lower():
                            if user in krisFatner:
                                name = krisText.split(": ")
                                change = krisText.replace(name[0] + ": ","")
                                cll = cab.getProfile()
                                cll1 = cab1.getProfile()
                                cll2 = cab2.getProfile()
                                cll3 = cab3.getProfile()
                                cll.displayName = change
                                cll1.displayName = change
                                cll2.displayName = change
                                cll3.displayName = change
                                cab.updateProfile(cll)
                                cab1.updateProfile(cll1)
                                cab2.updateProfile(cll2)
                                cab3.updateProfile(cll3)
                                cab.mentionWithkris(kirim,user," Update Name Success","\n Change to " + str(change))
                                cab1.mentionWithkris(kirim,user," Update Name Success","\n Change to " + str(change))
                                cab2.mentionWithkris(kirim,user," Update Name Success","\n Change to " + str(change))
                                cab3.mentionWithkris(kirim,user," Update Name Success","\n Change to " + str(change))

                        elif "changebioall: " in krisText.lower():
                            if user in krisFatner:
                                proses = krisText.split(": ")
                                teks = krisText.replace(proses[0] + ": ","")
                                no = cab.getProfile()
                                no1 = cab1.getProfile()
                                no2 = cab2.getProfile()
                                no3 = cab3.getProfile()
                                no.statusMessage = teks
                                no1.statusMessage = teks
                                no2.statusMessage = teks
                                no3.statusMessage = teks
                                cab.updateProfile(no)
                                cab1.updateProfile(no1)
                                cab2.updateProfile(no2)
                                cab3.updateProfile(no3)
                                cab.sendText(kirim,"My Bio Change To : " + teks)
                                cab1.sendText(kirim,"My Bio Change To : " + teks)
                                cab2.sendText(kirim,"My Bio Change To : " + teks)
                                cab3.sendText(kirim,"My Bio Change To : " + teks)

                        elif krisText.lower() == "remove pesan":
                            if user in krisFatner or user in Cyber["Admin"]:
                                try:
                                    cab.removeAllMessages(fast.param2)
                                    cab1.removeAllMessages(fast.param2)
                                    cab2.removeAllMessages(fast.param2)
                                    cab3.removeAllMessages(fast.param2)
                                    ginfo = cab.getGroup(kirim)
                                    owner = "u35459f1e84ad208cc56025c259cb1628"
                                    cab.mentionWithkris(kirim,owner," Remove Message Success ","\n In Grup" + str(" ("+ginfo.name+")"))
                                    cab1.mentionWithkris(kirim,owner," Remove Message Success ","\n In Grup" + str(" ("+ginfo.name+")"))
                                    cab2.mentionWithkris(kirim,owner," Remove Message Success ","\n In Grup" + str(" ("+ginfo.name+")"))
                                    cab3.mentionWithkris(kirim,owner," Remove Message Success ","\n In Grup" + str(" ("+ginfo.name+")"))
                                except:
                                    pass

                        elif krisText.lower() == 'restart':
                            if user in krisFatner:
                                cab.sendText(kirim, 'Restarting Server Prosses..')
                                print ("Restarting Server")
                                restart_program()

                        elif krisText.lower() == 'bot logout':
                            if user in krisFatner:
                                cab.mentionWithkris(kirim,user," Akses Off","")
                                print ("Selfbot Off")
                                exit(1)

                        elif "kick " in krisText.lower():
                            if user in krisFatner or user in Cyber["Admin"]:
                                key = eval(msg.contentMetadata["MENTION"])
                                key["MENTIONEES"][0]["M"]
                                targets = []
                                for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                                for target in targets:
                                    if target in kris:
                                        pass
                                    else:
                                        try:
                                            klist=[cab,cab1,cab2,cab3]
                                            kicker=random.choice(klist)
                                            kicker.kickoutFromGroup(kirim,[target])
                                            Cyber["Blacklist"][target] = True
                                        except Exception as e:
                                            cab.sendText(kirim, str(error))

                        elif krisText.lower() == 'my grup':
                            if user in krisFatner or user in Cyber["Admin"]:
                                groups = cab.groups
                                ret_ = "GRUP JOIN"
                                no = 0 + 1
                                for gid in groups:
                                    group = cab.getGroup(gid)
                                    ret_ += "\n\n{}. {} ".format(str(no), str(group.name))
                                    no += 1
                                ret_ += "\n\nTOTAL {} GRUP JOIN".format(str(len(groups)))
                                cab.sendText(kirim, str(ret_))

                        elif krisText.lower() == 'r1 grup':
                            if user in krisFatner or user in Cyber["Admin"]:
                                groups = cab1.groups
                                ret_ = "GRUP JOIN"
                                no = 0 + 1
                                for gid in groups:
                                    group = cab1.getGroup(gid)
                                    ret_ += "\n\n{}. {} ".format(str(no), str(group.name))
                                    no += 1
                                ret_ += "\n\nTOTAL {} GRUP JOIN".format(str(len(groups)))
                                cab1.sendText(kirim, str(ret_))

                        elif krisText.lower() == 'r2 grup':
                            if user in krisFatner or user in Cyber["Admin"]:
                                groups = cab2.groups
                                ret_ = "GRUP JOIN"
                                no = 0 + 1
                                for gid in groups:
                                    group = cab2.getGroup(gid)
                                    ret_ += "\n\n{}. {} ".format(str(no), str(group.name))
                                    no += 1
                                ret_ += "\n\nTOTAL {} GRUP JOIN".format(str(len(groups)))
                                cab2.sendText(kirim, str(ret_))

                        elif krisText.lower() == 'r3 grup':
                            if user in krisFatner or user in Cyber["Admin"]:
                                groups = cab3.groups
                                ret_ = "GRUP JOIN"
                                no = 0 + 1
                                for gid in groups:
                                    group = cab3.getGroup(gid)
                                    ret_ += "\n\n{}. {} ".format(str(no), str(group.name))
                                    no += 1
                                ret_ += "\n\nTOTAL {} GRUP JOIN".format(str(len(groups)))
                                cab3.sendText(kirim, str(ret_))

                        elif krisText.lower().startswith("rejectall grup"):
                            if user in krisFatner or user in Cyber["Admin"]:
                                ginvited = cab.getGroupIdsInvited()
                                ginvited = cab1.getGroupIdsInvited()
                                ginvited = cab2.getGroupIdsInvited()
                                ginvited = cab3.getGroupIdsInvited()
                                if ginvited != [] and ginvited != None:
                                    for gid in ginvited:
                                        cab.rejectGroupInvitation(gid)
                                        cab1.rejectGroupInvitation(gid)
                                        cab2.rejectGroupInvitation(gid)
                                        cab3.rejectGroupInvitation(gid)
                                    cab.sendMessage(kirim, "Succes Cancell {} Invite Grup".format(str(len(ginvited))))
                                    cab1.sendMessage(kirim, "Succes Cancell {} Invite Grup".format(str(len(ginvited))))
                                    cab2.sendMessage(kirim, "Succes Cancell {} Invite Grup".format(str(len(ginvited))))
                                    cab3.sendMessage(kirim, "Succes Cancell {} Invite Grup".format(str(len(ginvited))))
                                else:
                                    cab.sendMessage(kirim, "Nothing Invited")
                                    cab1.sendMessage(kirim, "Nothing Invited")
                                    cab2.sendMessage(kirim, "Nothing Invited")
                                    cab3.sendMessage(kirim, "Nothing Invited")

                        elif krisText.lower() == 'status':
                            if user in krisFatner or user in Cyber["Admin"]:
                                try:
                                    hasil = "Status Bot\n"
                                    if Cyber["autoAdd"] == True: hasil += "\nAuto Add ( on )"
                                    else: hasil += "\nAuto Add ( off )"
                                    if Cyber["autoJoin"] == True: hasil += "\nAuto Join ( on )"
                                    else: hasil += "\nAuto Join ( off )"
                                    if Cyber["AutoReject"] == True: hasil += "\nAuto Reject Room ( on )"
                                    else: hasil += "\nAuto Reject Room ( off )"
                                    if Cyber["AutojoinTicket"] == True: hasil += "\nAuto Join Ticket ( on )"
                                    else: hasil += "\nAuto Join Ticket ( off )"
                                    if Cyber["autoRead"] == True: hasil += "\nAuto Read ( on )"
                                    else: hasil += "\nAuto Read ( off )"
                                    if Cyber["AutoRespon"] == True: hasil += "\nDetect Mention ( on )"
                                    else: hasil += "\nDetect Mention ( off )"
                                    if Cyber["KickRespon"] == True: hasil += "\nDetect Mention ( on )"
                                    else: hasil += "\nDetect Kick Mention ( off )"
                                    if Cyber["Contact"] == True: hasil += "\nCheck Contact ( on )"
                                    else: hasil += "\nCheck Contact ( off )"
                                    if Cyber["Timeline"] == True: hasil += "\nCheck Post Timeline ( on )"
                                    else: hasil += "\nCheck Post ( off )"
                                    if Cyber["IDSticker"] == True: hasil += "\nCheck Sticker ( on )"
                                    else: hasil += "\nCheck Sticker ( off )"
                                    if Cyber["UnsendPesan"] == True: hasil += "\nUnsend Message ( on )"
                                    else: hasil += "\nUnsend Message ( off )"
                                    if krisProtect["protect"] == True: hasil += "\nProtect Grup ( on )"
                                    else: hasil += "\nProtect Grup ( off )"
                                    if krisProtect["linkprotect"] == True: hasil += "\nProtect Link Grup ( on )"
                                    else: hasil += "\nProtect Link Grup ( off )"
                                    if krisProtect["inviteprotect"] == True: hasil += "\nProtect Invite Grup ( on )"
                                    else: hasil += "\nProtect Invite Grup ( off )"
                                    if krisProtect["cancelprotect"] == True: hasil += "\nProtect Cancel Grup ( on )"
                                    else: hasil += "\nProtect Cancel Grup ( off )"
                                    if krisProtect["ProtectCancelled"] == True: hasil += "\nProtect Cancel Member ( on )"
                                    else: hasil += "\nProtect Cancel Member ( off )"
                                    if Cyber["BackupBot"] == True: hasil += "\nBackup Bot ( on )"
                                    else: hasil += "\nBackup Bot ( off )"
                                    if Cyber["KickOn"] == True: hasil += "\nKick All Member ( on )"
                                    else: hasil += "\nKick All Member ( off )"
                                    if Cyber["SpamInvite"] == True: hasil += "\nSpam invite via contact ( on )"
                                    else: hasil += "\nSpam invite Via Contact ( off )"
                                    hasil += "\n\nStatus Bot"
                                    cab.sendMessage(kirim, str(hasil))
                                except Exception as error:
                                    cab.sendMessage(kirim, str(error))

                        elif krisText in ["Allprotect on"]:
                            if user in krisFatner or user in Cyber["Admin"]:
                                try:
                                    krisProtect['protect'] = True
                                    krisProtect['linkprotect'] = True
                                    krisProtect['inviteprotect'] = True
                                    krisProtect['cancelprotect'] = True
                                    krisProtect['ProtectCancelled'] = True
                                    grup = cab.getGroup(kirim)
                                    cab.sendText(kirim,"AllProtect Already On in Grup : " +str(grup.name))
                                except Exception as e:
                                    cab.sendText(kirim, str(error))
                        elif krisText in ["Allprotect off"]:
                            if user in krisFatner or user in Cyber["Admin"]:
                                try:
                                    krisProtect['protect'] = False
                                    krisProtect['linkprotect'] = False
                                    krisProtect['inviteprotect'] = False
                                    krisProtect['cancelprotect'] = False
                                    krisProtect['ProtectCancelled'] = False
                                    grup = cab.getGroup(kirim)
                                    cab.sendText(kirim,"AllProtect Already Off in Grup : " +str(grup.name))
                                except Exception as e:
                                    cab.sendText(kirim, str(error))

                        elif krisText in ["Backup on"]:
                            if user in krisFatner or user in Cyber["Admin"]:
                                Cyber['BackupBot'] = True
                                cab.sendText(kirim,"Backup Bot Ready On")
                        elif krisText in ["Backup off"]:
                            if user in krisFatner or user in Cyber["Admin"]:
                                Cyber['BackupBot'] = False
                                cab.sendText(kirim,"Backup Bot Nonactive")

                        elif krisText in ["Unsend on"]:
                            if user in krisFatner or user in Cyber["Admin"]:
                                Cyber['UnsendPesan'] = True
                                cab.sendText(kirim,"Cek UnsendMessage Set to on..")
                        elif krisText in ["Unsend off"]:
                            if user in krisFatner or user in Cyber["Admin"]:
                                Cyber['UnsendPesan'] = False
                                cab.sendText(kirim,"Cek UnsendMessage Set to off..")

                        elif krisText in ["Changepp on"]:
                            if user in krisFatner or user in Cyber["Admin"]:
                                Cyber['Upfoto'] = True
                                cab.sendText(kirim,"Send Pict For UpPict")
                        elif krisText in ["Changepp off"]:
                            if user in krisFatner or user in Cyber["Admin"]:
                                Cyber['Upfoto'] = False
                                cab.sendText(kirim,"Send Pict Already Off")

                        elif krisText in ["Changeppbot on"]:
                            if user in krisFatner or user in Cyber["Admin"]:
                                Cyber['UpfotoBot'] = True
                                cab1.sendText(kirim,"Send Pict For UpPict")
                                cab2.sendText(kirim,"Send Pict For UpPict")
                                cab3.sendText(kirim,"Send Pict For UpPict")
                        elif krisText in ["Changeppbot off"]:
                            if user in krisFatner or user in Cyber["Admin"]:
                                Cyber['UpfotoBot'] = False
                                cab1.sendText(kirim,"Send Pict Already Off")
                                cab2.sendText(kirim,"Send Pict Already Off")
                                cab3.sendText(kirim,"Send Pict Already Off")

                        elif krisText in ["Cfotogrup on"]:
                            if user in krisFatner or user in Cyber["Admin"]:
                                Cyber['UpfotoGrup'] = True
                                cab.sendText(kirim,"Send Pict For Change Foto Grup")
                        elif krisText in ["Cfotogrup off"]:
                            if user in krisFatner or user in Cyber["Admin"]:
                                Cyber['UpfotoGrup'] = False
                                cab.sendText(kirim,"Send Pict Already Off")

                        elif krisText in ["Timeline on"]:
                            if user in krisFatner or user in Cyber["Admin"]:
                                Cyber['Timeline'] = True
                                cab.sendText(kirim,"Cek Post Set to on..")
                        elif krisText in ["Timeline off"]:
                            if user in krisFatner or user in Cyber["Admin"]:
                                Cyber['Timeline'] = False
                                cab.sendText(kirim,"Cek Post Set to off..")

                        elif krisText in ["Autojoin on"]:
                            if user in krisFatner or user in Cyber["Admin"]:
                                Cyber['autoJoin'] = True
                                cab.sendText(kirim,"Join Set To On..")
                        elif krisText in ["Autojoin off"]:
                            if user in krisFatner or user in Cyber["Admin"]:
                                Cyber['autoJoin'] = False
                                cab.sendText(kirim,"Join Set To Off..")

                        elif krisText in ["Autoreject on"]:
                            if user in krisFatner or user in Cyber["Admin"]:
                                Cyber['AutoReject'] = True
                                cab.sendText(msg.to,"Reject Set To On..")
                        elif krisText in ["Autoreject off"]:
                            if user in krisFatner or user in Cyber["Admin"]:
                                Cyber['AutoReject'] = False
                                cab.sendText(msg.to,"Reject Set To Off..")

                        elif krisText in ["Admin:add-on"]:
                            if user in krisFatner or user in Cyber["Admin"]:
                                Cyber["Adminadd"] = True
                                cab.sendText(kirim,"Send Contact to added Admin..")
                        elif krisText in ["Admin:add-off"]:
                            if user in krisFatner or user in Cyber["Admin"]:
                                Cyber["Adminadd"] = False
                                cab.sendText(kirim,"Send Contact to added Admin in Off..")

                        elif krisText in ["Admin:del-on"]:
                            if user in krisFatner or user in Cyber["Admin"]:
                                Cyber["AdminDel"] = True
                                cab.sendText(kirim,"Send Contact to Dellete Admin..")
                        elif krisText in ["Admin:del-off"]:
                            if user in krisFatner or user in Cyber["Admin"]:
                                Cyber["AdminDel"] = False
                                cab.sendText(kirim,"Send Contact to Dellete Admin in Off..")

                        elif krisText in ["Gift:on"]:
                            if user in krisFatner or user in Cyber["Admin"]:
                                Cyber["Gift"] = True
                                cab.sendText(kirim,"Send Contact to send Gift..")
                        elif krisText in ["Gift:off"]:
                            if user in krisFatner or user in Cyber["Admin"]:
                                Cyber["Gift"] = False
                                cab.sendText(kirim,"Send Contact to Gift in Off..")

                        elif krisText in ["Spaminvite on"]:
                            if user in krisFatner or user in Cyber["Admin"]:
                                Cyber["SpamInvite"] = True
                                cab.sendText(kirim,"Send Contact to spam grup..")
                        elif krisText in ["Spaminvite off"]:
                            if user in krisFatner or user in Cyber["Admin"]:
                                Cyber["Gift"] = False
                                cab.sendText(kirim,"Send Contact to send grup Off..")

                        elif krisText in ["Auto jointicket on"]:
                            if user in krisFatner or user in Cyber["Admin"]:
                                Cyber["AutojoinTicket"] = True
                                cab.sendText(kirim,"Join Ticket Set To On")
                        elif krisText in ["Auto jointicket off"]:
                            if user in krisFatner or user in Cyber["Admin"]:
                                Cyber["AutojoinTicket"] = False
                                cab.sendText(kirim,"Join Ticket Set To Off")
                        elif '/ti/g/' in krisText.lower():
                            if user in krisFatner or user in Cyber["Admin"]:
                                link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                                links = link_re.findall(msg.text)
                                n_links=[]
                                for l in links:
                                    if l not in n_links:
                                        n_links.append(l)
                                for ticket_id in n_links:
                                    if Cyber["AutojoinTicket"] == True:
                                        group=cab.findGroupByTicket(ticket_id)
                                        cab.acceptGroupInvitationByTicket(group.id,ticket_id)
                                        cab.sendText(kirim,"Success Masuk %s" % str(group.name))

                        elif krisText in ["Copy on"]:
                            if user in krisFatner or user in Cyber["Admin"]:
                                Cyber['Copy'] = True
                                cab.sendText(kirim,"Send Contact For Copy User")
                        elif krisText in ["Copy off"]:
                            if user in krisFatner or user in Cyber["Admin"]:
                                Cyber['Copy'] = False
                                cab.sendText(kirim,"Send Contact Already Off")

                        elif krisText.lower().startswith("clone "):
                            if user in krisFatner or user in Cyber["Admin"]:
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        contact = cab.getContact(ls)
                                        cab.cloneContactProfile(ls)
                                        cab.sendMessage(kirim, "Berhasil mengclone profile {}".format(contact.displayName))

                        elif krisText.lower() == 'comeback':
                            if user in krisFatner or user in Cyber["Admin"]:
                                try:
                                    clProfile.displayName = str(ProfileMe["displayName"])
                                    clProfile.statusMessage = str(ProfileMe["statusMessage"])
                                    clProfile.pictureStatus = str(ProfileMe["pictureStatus"])
                                    cab.updateProfileAttribute(8, clProfile.pictureStatus)
                                    cab.updateProfile(clProfile)
                                    cab.sendMessage(kirim, "Already back to my account")
                                except:
                                    cab.sendMessage(kirim, "Error Come Back")

                        elif krisText in ["Steal on"]:
                            if user in krisFatner or user in Cyber["Admin"]:
                                Cyber['Steal'] = True
                                cab.sendText(kirim,"Send Contact For Cek Contact")
                        elif krisText in ["Steal off"]:
                            if user in krisFatner or user in Cyber["Admin"]:
                                Cyber['Steal'] = False
                                cab.sendText(kirim,"Send Contact Already Off")

                        elif krisText in ["Contact on"]:
                            if user in krisFatner or user in Cyber["Admin"]:
                                Cyber['Contact'] = True
                                cab.sendText(kirim,"Contact Set to on")
                        elif krisText in ["Contact off"]:
                            if user in krisFatner or user in Cyber["Admin"]:
                                Cyber['Contact'] = False
                                cab.sendText(kirim,"Contact Already Off")

                        elif krisText in ["Invite on"]:
                            if user in krisFatner or user in Cyber["Admin"]:
                                Cyber['Invite'] = True
                                cab.sendText(kirim,"Send Contact For Invite Target")
                        elif krisText in ["Invite off"]:
                            if user in krisFatner or user in Cyber["Admin"]:
                                Cyber['Invite'] = False
                                cab.sendText(kirim,"Send Contact Set Off")

                        elif krisText.lower() == 'kill on':
                            if user in krisFatner or user in Cyber["Admin"]:
                                Cyber["KillOn"] = True
                                cab.sendMessage(kirim, "SendContact For Kick Taget")
                        elif krisText.lower() == 'kill off':
                            if user in krisFatner or user in Cyber["Admin"]:
                                Cyber["KillOn"] = False
                                cab.sendMessage(kirim, "SendContact For Kick Taget in Off")

                        elif krisText in ["Mic:add-on"]:
                            if user in krisFatner or user in Cyber["Admin"]:
                                Target["Mic"] = True
                                cab.sendText(kirim,"Send Contact To Clone Message User")
                        elif krisText in ["Mic:del-on"]:
                            if user in krisFatner or user in Cyber["Admin"]:
                                Target["MicDel"] = True
                                cab.sendText(kirim,"Send Contact Dellete Clone Message User")
                        elif "mimic" in krisText.lower():
                            if user in krisFatner or user in Cyber["Admin"]:
                                sep = krisText.split(" ")
                                mic = krisText.replace(sep[0] + " ","")
                                if mic == "on":
                                    if Mozilla["mimic"]["status"] == False:
                                        Mozilla["mimic"]["status"] = True
                                        cab.sendText(kirim,"Mimic Set to on")
                                elif mic == "off":
                                    if Mozilla["mimic"]["status"] == True:
                                        Mozilla["mimic"]["status"] = False
                                        cab.sendText(kirim,"Mimic Message off")

                        elif krisText.lower() == 'mimiclist':
                            if user in krisFatner or user in Cyber["Admin"]:
                                if Mozilla["mimic"]["target"] == {}:
                                    cab.sendText(kirim,"Tidak Ada Target")
                                else:
                                    mc = "Mimic List"
                                    for mi_d in Mozilla["mimic"]["target"]:
                                        mc += "\n? "+cab.getContact(mi_d).displayName
                                    cab.sendText(kirim,mc + "\nFinish")

                        elif krisText.lower() == 'refresh':
                            if user in krisFatner or user in Cyber["Admin"]:
                                try:
                                    Cyber['Mic'] = False
                                    Cyber['MicDel'] = False
                                    Cyber['Gift'] = False
                                    Cyber['Steal'] = False
                                    Cyber['Invite'] = False
                                    Cyber['Contact'] = False
                                    Cyber['Copy'] = False
                                    Cyber['autoJoin'] = False
                                    Cyber['autoAdd'] = False
                                    Cyber['AutojoinTicket'] = False
                                    Cyber['UnsendPesan'] = False
                                    Cyber['AutoReject'] = False
                                    Cyber['Timeline'] = False
                                    Cyber['Upfoto'] = False
                                    Cyber['UpfotoBot'] = False
                                    Cyber['UpfotoGrup'] = False
                                    Cyber['Adminadd'] = False
                                    Cyber['AdminDel'] = False
                                    Cyber['Welcome'] = False
                                    Cyber['Leave'] = False
                                    Cyber['Ban'] = False
                                    Cyber['Unban'] = False
                                    Cyber['KillOn'] = False
                                    Cyber['KickOn'] = False
                                    Cyber['SpamInvite'] = False
                                    cab.sendText(kirim,"Refresh Success")
                                except Exception as e:
                                    cab.sendText(kirim, str(error))

                        elif krisText.lower().startswith("my name"):
                            if user in krisFatner or user in Cyber["Admin"]:
                                contact = cab.getContact(user)
                                cab.sendMessage(kirim, "MyName : {}".format(contact.displayName))
                        elif krisText.lower().startswith("my bio"):
                            if user in krisFatner or user in Cyber["Admin"]:
                                contact = cab.getContact(user)
                                cab.sendMessage(kirim, "My Status : \n{}".format(contact.statusMessage))
                        elif krisText.lower().startswith("my picture"):
                            if user in krisFatner or user in Cyber["Admin"]:
                                contact = cab.getContact(user)
                                cab.sendImageWithURL(kirim,"http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus))
                        elif krisText.lower().startswith("my video"):
                            if user in krisFatner or user in Cyber["Admin"]:
                                contact = cab.getContact(user)
                                cab.sendVideoWithURL(kirim,"http://dl.profile.line-cdn.net/{}/vp".format(contact.pictureStatus))
                        elif krisText.lower().startswith("my cover"):
                            if user in krisFatner or user in Cyber["Admin"]:
                                channel = cab.getProfileCoverURL(user)          
                                path = str(channel)
                                cab.sendImageWithURL(kirim, path)

#------------------------------------------ SOCIAL MEDIA ----------------------------------------------------#

                        elif krisText.lower().startswith("topnews"):
                              if user in krisFatner or user in Cyber["Admin"]:
                                  kris=requests.get("https://newsapi.org/v2/top-headlines?country=id&apiKey=1214d6480f6848e18e01ba6985e2008d")
                                  data=kris.text
                                  data=json.loads(data)
                                  hasil = "Top News\n\n"
                                  hasil += "(1) " + str(data["articles"][0]["title"])                                                        
                                  hasil += "\n     Sumber : " + str(data["articles"][0]["source"]["name"])
                                  hasil += "\n     Penulis : " + str(data["articles"][0]["author"])
                                  hasil += "\n     Link : " + str(data["articles"][0]["url"])
                                  hasil += "\n\n(2) " + str(data["articles"][1]["title"])                                                        
                                  hasil += "\n     Sumber : " + str(data["articles"][1]["source"]["name"])
                                  hasil += "\n     Penulis : " + str(data["articles"][1]["author"])   
                                  hasil += "\n     Link : " + str(data["articles"][1]["url"])
                                  hasil += "\n\n(3) " + str(data["articles"][2]["title"])                                                        
                                  hasil += "\n     Sumber : " + str(data["articles"][2]["source"]["name"])
                                  hasil += "\n     Penulis : " + str(data["articles"][2]["author"])
                                  hasil += "\n     Link : " + str(data["articles"][2]["url"])
                                  hasil += "\n\n(4) " + str(data["articles"][3]["title"])                                                        
                                  hasil += "\n     Sumber : " + str(data["articles"][3]["source"]["name"])
                                  hasil += "\n     Penulis : " + str(data["articles"][3]["author"])
                                  hasil += "\n     Link : " + str(data["articles"][3]["url"])
                                  hasil += "\n\n(5) " + str(data["articles"][4]["title"])                                                        
                                  hasil += "\n     Sumber : " + str(data["articles"][4]["source"]["name"])
                                  hasil += "\n     Penulis : " + str(data["articles"][4]["author"])
                                  hasil += "\n     Link : " + str(data["articles"][4]["url"])
                                  hasil += "\n\n(6) " + str(data["articles"][5]["title"])                                                        
                                  hasil += "\n     Sumber : " + str(data["articles"][5]["source"]["name"])
                                  hasil += "\n     Penulis : " + str(data["articles"][5]["author"])
                                  hasil += "\n     Link : " + str(data["articles"][5]["url"])
                                  path = data["articles"][3]["urlToImage"]
                                  cab.sendText(kirim, str(hasil))
                                  cab.sendImageWithURL(kirim, str(path))

                        elif "Data birth: " in krisText:
                            if user in krisFatner or user in Cyber["Admin"]:
                                tanggal = krisText.replace("Data birth: ","")
                                r=requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                                data=r.text
                                data=json.loads(data)
                                lahir = data["data"]["lahir"]
                                usia = data["data"]["usia"]
                                ultah = data["data"]["ultah"]
                                zodiak = data["data"]["zodiak"]
                                cab.sendText(kirim," I N F O R M A S I \n"+"Date Of Birth : "+lahir+"\nAge : "+usia+"\nUltah : "+ultah+"\nZodiak : "+zodiak+"\n  I N F O R M A S I ")

                        elif krisText.lower().startswith("urban: "):
                            if user in krisFatner or user in Cyber["Admin"]:
                                sep = krisText.split(" ")
                                judul = krisText.replace(sep[0] + " ","")
                                url = "http://api.urbandictionary.com/v0/define?term="+str(judul)
                                with requests.session() as s:
                                    s.headers["User-Agent"] = random.choice(Mozilla["userAgent"])
                                    r = s.get(url)
                                    data = r.text
                                    data = json.loads(data)
                                    cu = "Urban Result\n\n"
                                    cu += "\nText: "+ data["tags"][0]
                                    cu += ","+ data["tags"][1]
                                    cu += ","+ data["tags"][2]
                                    cu += ","+ data["tags"][3]
                                    cu += ","+ data["tags"][4]
                                    cu += ","+ data["tags"][5]
                                    cu += ","+ data["tags"][6]
                                    cu += ","+ data["tags"][7]
                                    cu += "\n[1]\nAuthor: "+str(data["list"][0]["author"])+"\n"
                                    cu += "\nWord: "+str(data["list"][0]["word"])+"\n"
                                    cu += "\nLink: "+str(data["list"][0]["permalink"])+"\n"
                                    cu += "\nDefinition: "+str(data["list"][0]["definition"])+"\n"
                                    cu += "\nExample: "+str(data["list"][0]["example"])+"\n"
                                    cab.sendText(kirim, str(cu))

                        elif "Sslink: " in krisText:
                            if user in krisFatner or user in Cyber["Admin"]:
                                 website = msg.text.replace("Sslink: ","")
                                 response = requests.get("http://rahandiapi.herokuapp.com/sswebAPI?key=betakey&link="+website+"")
                                 data = response.json()
                                 pictweb = data['result']
                                 cab.sendImageWithURL(kirim, pictweb)

                        elif krisText.lower().startswith("maps: "):
                            if user in krisFatner or user in Cyber["Admin"]:
                                location = krisText.lower().replace("maps: ","")
                                with requests.session() as web:
                                    web.headers["user-agent"] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
                                    kris = web.get("http://api.corrykalam.net/apiloc.php?lokasi={}".format(urllib.parse.quote(location)))
                                    data = kris.text
                                    data = json.loads(data)
                                    if data[0] != "" and data[1] != "" and data[2] != "":
                                        link = "https://www.google.co.id/maps/@{},{},15z".format(str(data[1]), str(data[2]))
                                        ret_ = "Check Location\n"
                                        ret_ += "\n Lokasi : " + data[0]
                                        ret_ += "\n Google Maps : " + link
                                        ret_ += "\n\nSearch Location Success"
                                    else:
                                        ret_ = "Searching Location Error or Location Tidak Ditemukan"
                                    cab.sendText(kirim,str(ret_))

                        elif krisText.lower().startswith("cekcuaca: "):
                            if user in krisFatner or user in Cyber["Admin"]:
                                weather = krisText.lower().replace("cekcuaca: ","")
                                with requests.session() as web:
                                    web.headers["user-agent"] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
                                    kris = web.get("http://api.corrykalam.net/apicuaca.php?kota={}".format(urllib.parse.quote(weather)))
                                    data = kris.text
                                    data = json.loads(data)
                                    if "result" not in data:
                                        ret_ = "Cheking Weather\n"
                                        ret_ += "\nSuhu : " + data[1].replace("Suhu : ","")
                                        ret_ += "\nLokasi : " + data[0].replace("Temperatur di kota ","")
                                        ret_ += "\nKelembaban : " + data[2].replace("Kelembaban : ","")
                                        ret_ += "\nTekanan Udara : " + data[3].replace("Tekanan udara : ","")
                                        ret_ += "\nKecepatan Angin : " + data[4].replace("Kecepatan angin : ","")
                                        ret_ += "\n\nSearching Weather Success"
                                    else:
                                        ret_ = "Checking Weather Error or Not Found Location"
                                    cab.sendText(kirim, str(ret_))

                        elif krisText.lower().startswith("jadwalshalat: "):
                            if user in krisFatner or user in Cyber["Admin"]:
                                shalat = krisText.lower().replace("jadwalshalat: ","")
                                with requests.session() as web:
                                    web.headers["user-agent"] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
                                    kris = web.get("http://api.corrykalam.net/apisholat.php?lokasi={}".format(urllib.parse.quote(shalat)))
                                    data = kris.text
                                    data = json.loads(data)
                                    if data[1] != "Subuh : " and data[2] != "Dzuhur : " and data[3] != "Ashar : " and data[4] != "Maghrib : " and data[5] != "Isha : ":
                                        ret_ = "Jadwal Shalat\n"
                                        ret_ += "\nLocation : " + data[0]
                                        ret_ += "\n " + data[1]
                                        ret_ += "\n " + data[2]
                                        ret_ += "\n " + data[3]
                                        ret_ += "\n " + data[4]
                                        ret_ += "\n " + data[5]
                                        ret_ += "\n\nJadwal Shalat Wilayah"
                                    else:
                                        ret_ = "Jadwa Shalat Wilayah Error or Not Found Location" 
                                    cab.sendText(kirim, str(ret_))

                        elif "Idline: " in krisText:
                            if user in krisFatner or user in Cyber["Admin"]:
                                 msgg = krisText.replace('Idline: ','')
                                 conn = cab.findContactsByUserid(msgg)
                                 if True:
                                    cab.sendText(kirim,"Link User : https://line.me/ti/p/~" + msgg)
                                    cab.sendMessage(kirim, None, contentMetadata={'mid': conn.mid}, contentType=13)
                                    contact = cab.getContact(conn.mid)
                                    cab.sendImageWithURL(kirim,"http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                                    cover = cab.getProfileCoverURL(conn.mid)
                                    cab.sendImageWithURL(kirim, cover)
                                    cab.mentionWithkris(kirim,conn.mid,"Tag User\n","")

                        elif 'say-id: ' in krisText.lower():
                            if user in krisFatner or user in Cyber["Admin"]:
                                try:
                                    isi = krisText.lower().replace('say-id: ','')
                                    tts = gTTS(text=isi, lang='id', slow=False)
                                    tts.save('temp.mp3')
                                    cab.sendAudio(kirim, 'temp.mp3')
                                except Exception as e:
                                    cab.sendText(kirim, str(e))

                        elif 'say-en: ' in krisText.lower():
                            if user in krisFatner or user in Cyber["Admin"]:
                                try:
                                    isi = krisText.lower().replace('say-en: ','')
                                    tts = gTTS(text=isi, lang='en', slow=False)
                                    tts.save('temp.mp3')
                                    cab.sendAudio(kirim, 'temp.mp3')
                                except Exception as e:
                                    cab.sendText(kirim, str(e))

                        elif 'say-jp: ' in krisText.lower():
                            if user in krisFatner or user in Cyber["Admin"]:
                                try:
                                    isi = krisText.lower().replace('say-jp: ','')
                                    tts = gTTS(text=isi, lang='ja', slow=False)
                                    tts.save('temp.mp3')
                                    cab.sendAudio(kirim, 'temp.mp3')
                                except Exception as e:
                                    cab.sendText(kirim, str(e))

                        elif 'say-ar: ' in krisText.lower():
                            if user in krisFatner or user in Cyber["Admin"]:
                                try:
                                    isi = krisText.lower().replace('say-ar: ','')
                                    tts = gTTS(text=isi, lang='ar', slow=False)
                                    tts.save('temp.mp3')
                                    cab.sendAudio(kirim, 'temp.mp3')
                                except Exception as e:
                                    cab.sendText(kirim, str(e))

                        elif 'say-ko: ' in krisText.lower():
                            if user in krisFatner or user in Cyber["Admin"]:
                                try:
                                    isi = krisText.lower().replace('say-ko: ','')
                                    tts = gTTS(text=isi, lang='ko', slow=False)
                                    tts.save('temp.mp3')
                                    cab.sendAudio(kirim, 'temp.mp3')
                                except Exception as e:
                                    cab.sendText(kirim, str(e))

                        elif 'apakah: ' in krisText.lower():
                            if user in krisFatner or user in Cyber["Admin"]:
                                try:
                                    txt = ['iya','tidak','bisa jadi','mungkin saja','tidak mungkin','au ah gelap']
                                    isi = random.choice(txt)
                                    tts = gTTS(text=isi, lang='id', slow=False)
                                    tts.save('temp2.mp3')
                                    cab.sendAudio(kirim, 'temp2.mp3')
                                except Exception as e:
                                    cab.sendText(kirim, str(e))

                        elif 'kapan: ' in krisText.lower():
                            if user in krisFatner or user in Cyber["Admin"]:
                                try:
                                    txt = ['kapan kapan','besok','satu abad lagi','Hari ini','Tahun depan','Minggu depan','Bulan depan','Sebentar lagi']
                                    isi = random.choice(txt)
                                    tts = gTTS(text=isi, lang='id', slow=False)
                                    tts.save('temp2.mp3')
                                    cab.sendAudio(kirim, 'temp2.mp3')
                                except Exception as e:
                                    cab.sendText(kirim, str(e))

                        elif "Wikipedia: " in krisText:
                            if user in krisFatner or user in Cyber["Admin"]:
                                try:
                                    wiki = krisText.lower().replace("Wikipedia: ","")
                                    wikipedia.set_lang("id")
                                    pesan="Title ("
                                    pesan+=wikipedia.page(wiki).title
                                    pesan+=")\n\n"
                                    pesan+=wikipedia.summary(wiki, sentences=1)
                                    pesan+="\n"
                                    pesan+=wikipedia.page(wiki).url
                                    cab.sendText(kirim, pesan)
                                except:
                                    try:
                                        pesan="Over Text Limit! Please Click link\n"
                                        pesan+=wikipedia.page(wiki).url
                                        cab.sendText(kirim, pesan)
                                    except Exception as e:
                                        cab.sendText(kirim, str(e))

                        elif krisText.lower() == 'kalender':
                            if user in krisFatner or user in Cyber["Admin"]:
                                tz = pytz.timezone("Asia/Makassar")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                cab.sendMessage(kirim, readTime)

                        elif "gambar: " in krisText.lower():
                            if user in krisFatner or user in Cyber["Admin"]:
                                try:
                                    query = krisText.replace("gambar: ", "")
                                    query = query.replace(" ", "+")
                                    gambar = cab.download_image(query)
                                    cab.sendImageWithURL(kirim, gambar)
                                except Exception as e:
                                    cab.sendText(kirim, str(e))                                    

                        elif "youtube: " in krisText.lower():
                            if user in krisFatner or user in Cyber["Admin"]:
                                try:
                                    query = krisText.replace("youtube: ", "")
                                    query = query.replace(" ", "+")
                                    x = cab.youtube(query)
                                    cab.sendText(kirim, x)
                                except Exception as e:
                                    cab.sendText(kirim, str(e))

#--------------------------------- TRANSLATOR -------------------------------------------------#

                        elif krisText.lower().startswith("indonesian: "):
                            if user in krisFatner or user in Cyber["Admin"]:
                                sep = krisText.split(" ")
                                isi = krisText.replace(sep[0] + " ","")
                                translator = Translator()
                                hasil = translator.translate(isi, dest='id')
                                text = hasil.text
                                cab.sendMessage(kirim, "Translator Indonesian\n\n" + str(text))

                        elif krisText.lower().startswith("english: "):
                            if user in krisFatner or user in Cyber["Admin"]:
                                sep = krisText.split(" ")
                                isi = krisText.replace(sep[0] + " ","")
                                translator = Translator()
                                hasil = translator.translate(isi, dest='en')
                                text = hasil.text
                                cab.sendMessage(kirim, "Translator English\n\n" + str(text))

                        elif krisText.lower().startswith("korea: "):
                            if user in krisFatner or user in Cyber["Admin"]:
                                    sep = krisText.split(" ")
                                    isi = krisText.replace(sep[0] + " ","")
                                    translator = Translator()
                                    hasil = translator.translate(isi, dest='ko')
                                    text = hasil.text
                                    cab.sendMessage(kirim, "Translator Korea\n\n" + str(text))

                        elif krisText.lower().startswith("japan: "):
                            if user in krisFatner or user in Cyber["Admin"]:
                                sep = krisText.split(" ")
                                isi = krisText.replace(sep[0] + " ","")
                                translator = Translator()
                                hasil = translator.translate(isi, dest='ja')
                                text = hasil.text
                                cab.sendMessage(kirim, "Translator Japan\n\n" + str(text))

                        elif krisText.lower().startswith("thailand: "):
                            if user in krisFatner or user in Cyber["Admin"]:
                                sep = krisText.split(" ")
                                isi = krisText.replace(sep[0] + " ","")
                                translator = Translator()
                                hasil = translator.translate(isi, dest='th')
                                text = hasil.text
                                cab.sendMessage(kirim, "Translator Thailand\n\n" + str(text))

                        elif krisText.lower().startswith("arab: "):
                            if user in krisFatner or user in Cyber["Admin"]:
                                sep = krisText.split(" ")
                                isi = krisText.replace(sep[0] + " ","")
                                translator = Translator()
                                hasil = translator.translate(isi, dest='ar')
                                text = hasil.text
                                cab.sendMessage(kirim, "Translator Saudi Arabia\n\n" + str(text))

                        elif krisText.lower().startswith("malaysia: "):
                            if user in krisFatner or user in Cyber["Admin"]:
                                sep = krisText.split(" ")
                                isi = krisText.replace(sep[0] + " ","")
                                translator = Translator()
                                hasil = translator.translate(isi, dest='ms')
                                text = hasil.text
                                cab.sendMessage(kirim, "Translator Malaysia\n\n" + str(text))

                        elif krisText.lower().startswith("jawa: "):
                            if user in krisFatner or user in Cyber["Admin"]:
                                sep = krisText.split(" ")
                                isi = krisText.replace(sep[0] + " ","")
                                translator = Translator()
                                hasil = translator.translate(isi, dest='jw')
                                text = hasil.text
                                cab.sendMessage(kirim, "Translator Jawa\n\n" + str(text))

    except Exception as error:
        print (error)

#-------------------------------------------- FINNISHING SCRIP ------------------------------------------------#

while True:
    try:
        Operation = KRIS.singleTrace(count=50)
        if Operation is not None:
            for fast in Operation:
                KRIS.setRevision(fast.revision)
                thread1 = threading.Thread(target=KRIS_FAST_USER, args=(fast,))#self.OpInterrupt[fast.type], args=(fast,)
                thread1.start()
                thread1.join()
    except Exception as KRIS:
        logError(KRIS)
